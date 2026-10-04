"""Meta creative and conversion-path planning, not live objective mapping."""


def build(brief: dict) -> dict:
    offer = brief["offer"]
    facts = brief["facts"]
    proof = facts[0]["text"] if facts else "實際內容與適用條件待品牌提供；先查看方案介紹。"
    evidence = [facts[0]["id"]] if facts else []
    variants = [
        {"id": "local-creative-1", "angle": "內容導覽", "hypothesis": "清楚展示內容，可能幫助使用者判斷是否符合需求。",
         "headline": f"先了解{offer}", "primary_text": f"正在比較不同選擇？先看看{offer}的完整介紹，再決定是否適合目前的需求。",
         "cta": "了解更多", "format_hint": "single_image", "visual_brief": "製作一張內容導覽圖；只列出已確認資訊，不加入未提供的價格或保證。",
         "evidence_ids": []},
        {"id": "local-creative-2", "angle": "具體內容", "hypothesis": "具體資訊可能比空泛形容詞更有助於理解。",
         "headline": "從具體內容開始了解", "primary_text": f"關於{offer}：{proof}",
         "cta": "了解更多", "format_hint": "single_image", "visual_brief": "製作與已提供事實一致的示範圖；若無素材先列補拍清單，不偽造使用畫面。",
         "evidence_ids": evidence},
        {"id": "local-creative-3", "angle": "選擇條件", "hypothesis": "讓使用者自行評估適用性，可能減少不合適的詢問。",
         "headline": "先確認是否符合需求", "primary_text": f"選擇{offer}之前，可以先確認內容、使用情境與下一步流程。把問題問清楚，再做決定。",
         "cta": "了解更多", "format_hint": "single_image", "visual_brief": "以單張圖呈現選擇條件與如何取得資訊；適用條件未知時保留待確認。",
         "evidence_ids": []},
    ]
    return {
        "objective_reasoning": {"planning_goal": brief["goal"],
                                "rationale": "以使用者提供的成功行動反推轉換路徑；這是規劃分類，不是 Meta API 目標值。",
                                "live_objective": None},
        "creative_variants": variants,
        "conversion_path": ["廣告訊息", "使用者提供的落地頁或諮詢入口", brief["success_action"] or "成功行動待確認"],
        "landing_page_checks": ["是否與廣告主張一致", "是否有清楚行動入口", "是否有完整價格／條件資訊", "是否已確認資料告知與追蹤設定"],
        "test_plan": [{"id": "local-test-1", "variable": "message_angle",
                       "variants": [v["id"] for v in variants],
                       "hold_constant": ["先統一素材格式與版位，避免同時測格式與角度", "客群假設", "落地頁", "量測口徑"],
                       "decision_rule": "素材形式只是企劃候選；正式比較訊息角度時先做成相同形式，再以成功行動與名單品質判讀。",
                       "budget_allocation": None}],
        "review_notes": ["不假設帳號支援任何即時目標、版位、受眾或追蹤事件。",
                         "避免直接斷言觀看者的健康、財務或其他敏感個人屬性；需人工政策審查。",
                         "沒有真實客戶素材或授權時，不得生成看似真實的見證。"],
    }


def validate(value: dict, brief: dict) -> list[str]:
    errors = []
    ids = [variant["id"] for variant in value["creative_variants"]]
    if len(ids) != len(set(ids)):
        errors.append("creative_variants: duplicate local IDs")
    if value["objective_reasoning"]["planning_goal"] != brief["goal"]:
        errors.append("objective_reasoning: goal must match supplied brief")
    for test in value["test_plan"]:
        if any(ref not in ids for ref in test["variants"]):
            errors.append("test_plan: unknown creative reference")
    return errors
