import streamlit as st
import requests
import io
import time
import random
from PIL import Image

# ==========================================
# 1. 網頁初始化與響應式設定 (Mobile Friendly)
# ==========================================
st.set_page_config(
    page_title="Cosmos3-Super Web Companion",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 注入自定義 Premium 暗色風格與行動端優化 CSS
st.markdown("""
<style>
    /* 全域背景與文字顏色調和 */
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
    }
    
    /* 側邊欄設計優化 */
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid #1e293b;
    }
    
    /* 進階按鈕漸層色 (NVIDIA Green 質感) */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #76b900 0%, #5da300 100%) !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.5rem !important;
        transition: transform 0.2s ease, opacity 0.2s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        opacity: 0.95;
    }
    
    /* 下載按鈕設計 */
    div.stDownloadButton > button:first-child {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 8px !important;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 側邊欄 (Sidebar) 與安全金鑰處理
# ==========================================
st.sidebar.title("🌌 Cosmos3 T2I")
st.sidebar.caption("行動演示與開發助理 (HW3)")
st.sidebar.markdown("---")

# 雙軌密鑰安全機制 (優先讀取 Secrets，若無則顯示密碼輸入框)
api_key = st.secrets.get("HF_TOKEN", "")

if not api_key:
    st.sidebar.warning("🔑 尚未偵測到雲端 Secrets 金鑰")
    api_key = st.sidebar.text_input(
        "請輸入 Hugging Face Token",
        type="password",
        help="請前往 Hugging Face > Settings > Tokens 申請一個擁有 Read 權限的 Token。"
    )
else:
    st.sidebar.success("🔒 已自動載入環境金鑰 (Secrets)")

st.sidebar.markdown("---")

# Steerability 參數控制面板
st.sidebar.subheader("⚙️ 圖像生成參數調整")

style_preset = st.sidebar.selectbox(
    "視覺風格 (Image Style)",
    [
        "電影感 (Cinematic)", 
        "動漫插畫 (Anime Art)", 
        "未來科技 (Cyberpunk/Sci-Fi)", 
        "極簡攝影 (Minimalist Photography)",
        "寫實照片 (Photorealistic)"
    ]
)

aspect_ratio = st.sidebar.radio(
    "長寬比例 (Aspect Ratio)",
    ["1:1 (手機/頭像)", "16:9 (橫幅寬螢幕)", "9:16 (直幅滿版)", "4:3 (傳統比例)"],
    index=0
)

# 隨機種子設定
use_random_seed = st.sidebar.checkbox("使用隨機種子 (Randomize Seed)", value=True)
if use_random_seed:
    current_seed = random.randint(0, 999999)
    st.sidebar.info(f"🎲 目前隨機分配種子: `{current_seed}`")
else:
    current_seed = st.sidebar.number_input("指定種子 (Seed)", min_value=0, max_value=999999, value=42)

# 負面提示詞
negative_prompt = st.sidebar.text_area(
    "排除元素 (Negative Prompt)",
    value="blurry, low quality, low-res, distorted, extra limbs, bad proportions",
    height=80
)

# 演示備用模式開關 (防死角手機 Demo 熱鍵)
mock_mode = st.sidebar.checkbox(
    "開啟免 Key 示範模式 (Mock Mode)", 
    value=False,
    help="當 Hugging Face 節點因負載超載無法回傳，或是手邊沒有金鑰時，勾選此項可直接進行流暢的流程演示！"
)

# ==========================================
# 3. 主頁面 (Main Frame)
# ==========================================
st.title("🚀 NVIDIA Cosmos 3 Super")
st.markdown("### 64B Text-to-Image Generation Portal")

# 作業規範硬性要求：清楚呈現專案資訊與繳交連結
col_meta1, col_meta2 = st.columns(2)
with col_meta1:
    st.markdown("ℹ️ **模型名稱**: `nvidia/Cosmos3-Super-Text2Image`")
    st.markdown("💻 **本地執行**: `streamlit run app.py`")
with col_meta2:
    # 學生部署後需至 GitHub 與 Streamlit Secrets 填寫此處
    st.markdown("🔗 **GitHub 專案**: [點此訪問 Repository](https://github.com/gshan1209-cell/hw3-cosmos-text2image)")
    st.markdown("🚀 **雲端網址**: [點此訪問 Live Demo](https://your-app-name.streamlit.app)")

st.markdown("---")

# 使用者輸入提示詞區塊
prompt_input = st.text_area(
    "🔮 請輸入英文場景描述 (Prompt)",
    placeholder="例如: A majestic glowing dragon flying over Taipei 101 at sunset, highly detailed, cyberpunk anime aesthetic...",
    height=120
)

# Cosmos 3 JSON-upsampled Prompt 輔助資訊
st.caption("💡 *提示：Cosmos 3 對於結構化、細節描述的字句有著極佳的物理世界還原能力，建議添加光線與鏡頭描述。*")

# ==========================================
# 4. API 呼叫與推論邏輯 (Inference Engine)
# ==========================================
API_URL = "https://api-inference.huggingface.co/models/nvidia/Cosmos3-Super-Text2Image"

def call_huggingface_api(payload, token):
    headers = {"Authorization": f"Bearer {token}"}
    # 設定合理超時，防行動端無限掛起
    response = requests.post(API_URL, headers=headers, json=payload, timeout=45)
    return response

# 主按鈕觸發
if st.button("🎨 啟動 Cosmos 3 晶片生成圖像"):
    if not mock_mode and not api_key:
        st.error("❌ 拒絕執行：尚未提供 Hugging Face Token，請於側邊欄輸入金鑰或開啟「示範模式」。")
    elif not prompt_input:
        st.warning("⚠️ 請輸入提示詞以進行影像繪製！")
    else:
        # 開始執行生成動畫與狀態欄
        with st.spinner("⏳ NVIDIA GPU 運算推論中... 這可能需要 15-30 秒，請稍候"):
            
            # A. 模擬示範模式 (Mock Mode) - 確保在手機演練時100%成功
            if mock_mode:
                time.sleep(2.5)  # 模擬運算延迟
                st.success("✅ [演示模式成功] 已成功載入預置的高畫質模擬影像：")
                
                # 採用極具未來感的預置 Unsplash 優質圖像做為演示
                mock_images = [
                    "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80", # 抽象未來
                    "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?auto=format&fit=crop&w=1200&q=80", # 奇幻森林
                    "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?auto=format&fit=crop&w=1200&q=80"  # 數位藝術
                ]
                selected_mock_url = random.choice(mock_images)
                
                try:
                    mock_resp = requests.get(selected_mock_url)
                    demo_img = Image.open(io.BytesIO(mock_resp.content))
                    st.image(demo_img, caption=f"Cosmos3 模擬生成結果 (風格: {style_preset} | 種子: {current_seed})", use_container_width=True)
                    
                    # 下載按鈕支援
                    img_byte_arr = io.BytesIO()
                    demo_img.save(img_byte_arr, format='PNG')
                    st.download_button(
                        label="💾 下載生成圖像 (PNG)",
                        data=img_byte_arr.getvalue(),
                        file_name=f"cosmos3_mock_result_{current_seed}.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"❌ 示範圖庫載入失敗: {e}")
            
            # B. 真實 API 呼叫模式
            else:
                # 組合 Prompt (符合 JSON-upsampled 精神的逗號結構拼接)
                final_prompt = f"{prompt_input}, {style_preset} style, ultra high-res, 8k resolution"
                
                payload = {
                    "inputs": final_prompt,
                    "parameters": {
                        "seed": int(current_seed),
                        "negative_prompt": negative_prompt
                    }
                }
                
                try:
                    response = call_huggingface_api(payload, api_key)
                    
                    if response.status_code == 200:
                        image_bytes = response.content
                        img_result = Image.open(io.BytesIO(image_bytes))
                        
                        st.success("🎉 Cosmos3 圖像生成成功！")
                        st.image(img_result, caption=f"生成結果 (風格: {style_preset} | 種子: {current_seed})", use_container_width=True)
                        
                        # 提供下載功能
                        buf = io.BytesIO()
                        img_result.save(buf, format="PNG")
                        st.download_button(
                            label="💾 下載生成圖像 (PNG)",
                            data=buf.getvalue(),
                            file_name=f"cosmos3_result_{current_seed}.png",
                            mime="image/png"
                        )
                        
                    elif response.status_code == 503:
                        st.error("⚠️ Hugging Face 模型節點目前處於休眠或佇列排隊中 (Error 503)。")
                        st.info("💡 **貼心提示**：由於免費 HF Inference API 常有瞬時載入延遲，您可以直接勾選側邊欄的「開啟免 Key 示範模式 (Mock Mode)」進行無中斷的流暢演示！")
                    elif response.status_code == 401:
                        st.error("❌ 認證失敗 (401)：請檢查您的 Hugging Face Token 權限是否正確。")
                    else:
                        st.error(f"❌ 請求失敗，狀態碼: {response.status_code}")
                        st.text(response.text)
                        
                except requests.exceptions.Timeout:
                    st.error("⏳ API 請求超時：Hugging Face 伺服器響應時間過長，請稍後再試，或使用「示範模式」展示。")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 網路連線失敗：無法解析 Hugging Face 伺服器位址。請檢查您的網路連線、DNS 設定，或確認是否有防火牆/VPN 阻擋。作為替代方案，您可以開啟側邊欄的「示範模式」來進行展示。")
                except Exception as e:
                    st.error(f"❌ 發生系統錯誤: {str(e)}")

# 頁尾
st.markdown("---")
st.caption("© 2026 HW3 Cosmos3-Super-Text2Image App. Assisted by Gemini Canvas.")
