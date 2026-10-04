from __future__ import annotations
import sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import core, platform_rules


class MetaTests(unittest.TestCase):
    def setUp(self):
        self.brief = core.load_json(ROOT / "examples/brief.synthetic.json")
        self.plan = core.make_plan(self.brief, platform_rules.build)

    def test_three_angles(self):
        self.assertEqual(len(self.plan["deliverables"]["creative_variants"]), 3)

    def test_evidence_reference(self):
        self.assertEqual(self.plan["deliverables"]["creative_variants"][1]["evidence_ids"], ["F1"])

    def test_unknown_evidence_rejected(self):
        self.plan["deliverables"]["creative_variants"][0]["evidence_ids"] = ["F999"]
        with self.assertRaises(core.InputError):
            core.validate_plan(self.plan, platform_rules.validate)

    def test_no_evidence_stays_empty(self):
        p = core.make_plan({"offer": "課程"}, platform_rules.build)
        self.assertTrue(all(not v["evidence_ids"] for v in p["deliverables"]["creative_variants"]))

    def test_no_live_objective(self):
        self.assertIsNone(self.plan["deliverables"]["objective_reasoning"]["live_objective"])
        self.plan["deliverables"]["objective_reasoning"]["live_objective"] = "OUTCOME_SALES"
        with self.assertRaises(core.InputError):
            core.validate_plan(self.plan, platform_rules.validate)

    def test_goal_mismatch(self):
        self.plan["deliverables"]["objective_reasoning"]["planning_goal"] = "sales"
        with self.assertRaises(core.InputError):
            core.validate_plan(self.plan, platform_rules.validate)

    def test_variant_reference(self):
        self.plan["deliverables"]["test_plan"][0]["variants"][0] = "local-unknown"
        with self.assertRaises(core.InputError):
            core.validate_plan(self.plan, platform_rules.validate)

    def test_duplicate_variant_id(self):
        v = self.plan["deliverables"]["creative_variants"]
        v[1]["id"] = v[0]["id"]
        with self.assertRaises(core.InputError):
            core.validate_plan(self.plan, platform_rules.validate)

    def test_uniform_format_for_angle_test(self):
        formats = {v["format_hint"] for v in self.plan["deliverables"]["creative_variants"]}
        self.assertEqual(len(formats), 1)

    def test_no_facts_invented(self):
        p = core.make_plan({"offer": "課程"}, platform_rules.build)
        self.assertEqual(p["input"]["facts"], [])
        self.assertEqual(p["measurement"]["tracking_status"], "NOT_VERIFIED")
