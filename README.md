HW3: Cosmos3-Super-Text2Image 應用程式

專案目標

本專案為一個互動式網頁應用程式，透過 Hugging Face Inference API 整合 NVIDIA 最先進的 Cosmos3-Super-Text2Image (64B) 基礎模型。此應用程式旨在提供具備響應式及行動裝置友善的 AI 生成體驗，協助學生完成 HW3 的作業要求。

模型

核心模型：nvidia/Cosmos3-Super-Text2Image

特點：擁有 64B (640 億) 參數的文字轉圖片特化模型，專為高保真物理場景模擬所設計。

主要功能

互動式控制（側邊欄調節）：支援自訂圖片風格預設、長寬比選項、隨機種子設定以及負面提示詞排除功能。

雙層安全憑證機制：在生產環境中優先使用 st.secrets 進行驗證，並在側邊欄提供安全的隱藏式密碼輸入框，作為本機執行的備用方案。

模擬/展示備用模式：專為實體/行動裝置簡報所設計。當 Hugging Face 伺服器節點正在排隊或離線時，切換至「模擬模式」可無縫提供模擬的高畫質影像，避免展示時發生卡頓或中斷。

如何在本地端執行

1. 複製 (Clone) 儲存庫

git clone [https://github.com/gshan1209-cell/hw3-cosmos-text2image.git](https://github.com/gshan1209-cell/hw3-cosmos-text2image.git)
cd hw3-cosmos-text2image


2. 安裝依賴套件

pip install -r requirements.txt


3. 設定金鑰 (Secrets)

為避免將您的 Hugging Face API 金鑰硬編碼在程式中：

選項 A：在執行應用程式時，直接將您的 Token 輸入到側邊欄的密碼欄位中。

選項 B：在本地端建立一個 .streamlit/secrets.toml 檔案，並加入您的憑證：

HF_TOKEN = "your_huggingface_read_token_here"


4. 執行應用程式

streamlit run app.py


部署至 Streamlit 雲端社群 (Streamlit Community Cloud)

將完成的儲存庫程式碼推送到 GitHub (請確認 .gitignore 已經排除您的 secrets 檔案)。

前往 Streamlit Share 並使用您的 GitHub 帳號登入。

點擊「New App」，選擇您的儲存庫、分支，並將進入點檔案設定為 app.py。

在「Advanced Settings」(進階設定) 中，找到 Secrets 區塊並安全地加入您的 API 憑證：

HF_TOKEN = "your_huggingface_read_token_here"


點擊「Deploy」(部署)。您的線上應用程式將在幾分鐘內準備就緒！

相關連結

GitHub 儲存庫：https://github.com/gshan1209-cell/hw3-cosmos-text2image

Streamlit 線上展示：https://your-app-name.streamlit.app

畫面截圖

![Demo](images/demo.png)