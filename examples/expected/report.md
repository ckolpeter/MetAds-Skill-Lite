# MetAds Skill Lite｜離線企劃初稿

> 尚未投放、未查詢帳號或網站；所有建議須人工確認。

版本：1.0.0｜資料：synthetic｜產生方式：deterministic\_starter
狀態：PLAN_READY（僅本地結構）｜人工審查：HUMAN_REVIEW_REQUIRED

## 1. 商業資料與證據

- **brand**：範例學院
- **offer**：廣告入門課程
- **audience**：想練習廣告規劃的初學者
- **market**：台灣
- **goal**：leads
- **success\_action**：提交課程諮詢表單
- **landing\_page\_url**：https://example.com/course
- **landing\_page\_text**：合成範例：頁面介紹課程內容，設有課程諮詢表單。未提供價格、保證、開課日或真實成效。
- **currency**：TWD
- **total\_budget**：6000
- **duration\_days**：14
- **video\_duration\_seconds**：30
- **facts**
  - 項目 1
    - **id**：F1
    - **text**：課程內容包含廣告規劃練習。
    - **source**：合成教學範例，不是 AI Ads Academy 的真實課程承諾。
- **constraints**
  - 不得宣稱保證收益。
  - 未提供價格，不得補寫優惠。
- **data\_label**：synthetic

## 2. 預算算術摘要

- **currency**：TWD
- **total\_limit**：6000
- **duration\_days**：14
- **daily\_average**：428.57
- **note**：僅為總額除以天數的規劃均值，不是平台每日預算設定；不得直接四捨五入後乘回作為支出承諾。

## 3. 平台專用產出

- **objective\_reasoning**
  - **planning\_goal**：leads
  - **rationale**：以使用者提供的成功行動反推轉換路徑；這是規劃分類，不是 Meta API 目標值。
  - **live\_objective**：待確認
- **creative\_variants**
  - 項目 1
    - **id**：local-creative-1
    - **angle**：內容導覽
    - **hypothesis**：清楚展示內容，可能幫助使用者判斷是否符合需求。
    - **headline**：先了解廣告入門課程
    - **primary\_text**：正在比較不同選擇？先看看廣告入門課程的完整介紹，再決定是否適合目前的需求。
    - **cta**：了解更多
    - **format\_hint**：single\_image
    - **visual\_brief**：製作一張內容導覽圖；只列出已確認資訊，不加入未提供的價格或保證。
    - **evidence\_ids**
      - 未提供／未設定
  - 項目 2
    - **id**：local-creative-2
    - **angle**：具體內容
    - **hypothesis**：具體資訊可能比空泛形容詞更有助於理解。
    - **headline**：從具體內容開始了解
    - **primary\_text**：關於廣告入門課程：課程內容包含廣告規劃練習。
    - **cta**：了解更多
    - **format\_hint**：single\_image
    - **visual\_brief**：製作與已提供事實一致的示範圖；若無素材先列補拍清單，不偽造使用畫面。
    - **evidence\_ids**
      - F1
  - 項目 3
    - **id**：local-creative-3
    - **angle**：選擇條件
    - **hypothesis**：讓使用者自行評估適用性，可能減少不合適的詢問。
    - **headline**：先確認是否符合需求
    - **primary\_text**：選擇廣告入門課程之前，可以先確認內容、使用情境與下一步流程。把問題問清楚，再做決定。
    - **cta**：了解更多
    - **format\_hint**：single\_image
    - **visual\_brief**：以單張圖呈現選擇條件與如何取得資訊；適用條件未知時保留待確認。
    - **evidence\_ids**
      - 未提供／未設定
- **conversion\_path**
  - 廣告訊息
  - 使用者提供的落地頁或諮詢入口
  - 提交課程諮詢表單
- **landing\_page\_checks**
  - 是否與廣告主張一致
  - 是否有清楚行動入口
  - 是否有完整價格／條件資訊
  - 是否已確認資料告知與追蹤設定
- **test\_plan**
  - 項目 1
    - **id**：local-test-1
    - **variable**：message\_angle
    - **variants**
      - local-creative-1
      - local-creative-2
      - local-creative-3
    - **hold\_constant**
      - 先統一素材格式與版位，避免同時測格式與角度
      - 客群假設
      - 落地頁
      - 量測口徑
    - **decision\_rule**：素材形式只是企劃候選；正式比較訊息角度時先做成相同形式，再以成功行動與名單品質判讀。
    - **budget\_allocation**：待確認
- **review\_notes**
  - 不假設帳號支援任何即時目標、版位、受眾或追蹤事件。
  - 避免直接斷言觀看者的健康、財務或其他敏感個人屬性；需人工政策審查。
  - 沒有真實客戶素材或授權時，不得生成看似真實的見證。

## 4. 量測待辦

- **success\_action**：提交課程諮詢表單
- **tracking\_status**：NOT\_VERIFIED
- **baseline**：待確認
- **target**：待確認
- **attribution\_window**：待確認

## 5. 假設

- 這是固定規則產生的企劃起稿；訊息角度是待驗證假設，不是成效預測。
- 輸入事實由使用者提供，未經本工具外部查證；合成範例不得當作真實案例。
- 平台目標與素材規格未作 live 驗證；人工上線前須在實際帳號確認。

## 6. 檢查與待確認

- **valid**：true
- **validation\_scope**：local\_structure\_only
- **warnings**
  - 尚未驗證模型路由、廣告審核、素材授權或實際投放成效。
  - 通過僅表示本地結構檢查；商品真實性與廣告策略須人工審查。

