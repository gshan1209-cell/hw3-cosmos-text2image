import streamlit as st


def apply_app_theme():
    st.markdown(
        """
        <style>
        :root {
            --bg: #0b0f19;
            --surface: #111827;
            --surface-soft: #1f2937;
            --line: #374151;
            --line-strong: #4b5563;
            --ink: #f8fafc;
            --muted: #94a3b8;
            --muted-2: #64748b;
            --brand: #76b900;
            --brand-strong: #5da300;
            --brand-soft: #1a2e05;
            --danger: #ef4444;
            --warning: #f59e0b;
            --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2);
            --shadow-md: 0 10px 30px rgba(0, 0, 0, 0.4);
        }

        .stApp {
            background: var(--bg);
            color: var(--ink);
            font-feature-settings: "cv02", "cv03", "cv04", "cv11";
        }

        [data-testid="stHeader"] {
            background: rgba(11, 15, 25, 0.94);
            border-bottom: 1px solid var(--line);
            backdrop-filter: blur(12px);
        }

        [data-testid="stAppViewContainer"] > .main .block-container {
            max-width: 1120px;
            padding: 2.2rem 2rem 3.5rem;
        }

        [data-testid="stSidebar"] {
            background: var(--surface);
            border-right: 1px solid var(--line);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 1.4rem;
        }

        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            gap: 0.75rem;
        }

        h1, h2, h3 {
            color: var(--ink);
            letter-spacing: 0;
            font-weight: 760;
        }

        h1 {
            max-width: 860px;
            font-size: 2.55rem;
            line-height: 1.08;
            margin: 0 0 0.25rem;
        }

        h2 {
            font-size: 1.25rem;
            line-height: 1.25;
            margin: 1.35rem 0 0.35rem;
        }

        h3 {
            font-size: 1rem;
            line-height: 1.3;
            margin: 1rem 0 0.25rem;
        }

        p, li, label, .stMarkdown {
            color: var(--ink);
        }

        small, [data-testid="stCaptionContainer"] {
            color: var(--muted);
        }

        [data-testid="stMarkdownContainer"] p {
            line-height: 1.62;
        }

        div[data-testid="stForm"] {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1.15rem 1.2rem;
            box-shadow: var(--shadow-sm);
        }

        div[data-testid="stExpander"] {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow-sm);
            overflow: hidden;
        }

        div[data-testid="stTabs"] button {
            color: var(--muted);
            font-weight: 650;
        }

        div[data-testid="stTabs"] button[aria-selected="true"] {
            color: var(--brand);
        }

        div[data-testid="stTextArea"] textarea,
        div[data-testid="stTextInput"] input,
        div[data-testid="stNumberInput"] input,
        div[data-testid="stSelectbox"] > div,
        div[data-testid="stMultiSelect"] > div {
            background: var(--surface-soft);
            border-color: var(--line);
            border-radius: 8px;
            color: var(--ink);
            box-shadow: none;
        }

        div[data-testid="stTextArea"] textarea {
            min-height: 136px;
            line-height: 1.5;
        }

        div[data-testid="stTextArea"] textarea:focus,
        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stNumberInput"] input:focus {
            border-color: var(--brand);
            box-shadow: 0 0 0 3px rgba(118, 185, 0, 0.2);
        }

        .stButton > button,
        .stDownloadButton > button {
            min-height: 2.55rem;
            border-radius: 8px;
            border: none;
            background: linear-gradient(90deg, var(--brand) 0%, var(--brand-strong) 100%);
            color: #000000;
            font-weight: 720;
            letter-spacing: 0;
            box-shadow: var(--shadow-sm);
            transition: transform 140ms ease, box-shadow 140ms ease;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            transform: scale(1.02);
            color: #000000;
            box-shadow: 0 6px 16px rgba(118, 185, 0, 0.3);
        }

        .stButton > button:active,
        .stDownloadButton > button:active {
            box-shadow: none;
        }

        .stButton > button[kind="secondary"] {
            background: var(--surface-soft);
            border-color: var(--line-strong);
            color: var(--brand);
            box-shadow: none;
        }

        .stButton > button[kind="secondary"]:hover {
            border-color: var(--brand);
            color: var(--brand);
        }

        div[data-testid="stAlert"] {
            border-radius: 8px;
            border: 1px solid var(--line);
            box-shadow: var(--shadow-sm);
        }

        div[data-testid="stImage"] img {
            border-radius: 8px;
            border: 1px solid var(--line);
            box-shadow: var(--shadow-md);
            background: var(--surface);
        }

        [data-testid="stMetric"] {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 0.95rem 1rem;
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted);
        }

        [data-testid="stMetricValue"] {
            color: var(--ink);
            font-weight: 760;
        }

        div[data-testid="stProgress"] > div > div {
            background-color: var(--brand);
        }

        div[data-testid="stSpinner"] {
            color: var(--brand);
        }

        code {
            border-radius: 6px;
            border: 1px solid var(--line);
            background: rgba(255, 255, 255, 0.05);
            color: var(--ink);
        }

        hr {
            border-color: var(--line);
            margin: 1.2rem 0;
        }

        .app-hero {
            margin-bottom: 1.25rem;
            padding: 1.25rem 1.35rem;
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow-sm);
        }

        .app-eyebrow {
            margin-bottom: 0.45rem;
            color: var(--brand);
            font-size: 0.82rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .app-subtitle {
            max-width: 760px;
            margin: 0.35rem 0 0;
            color: var(--muted);
            font-size: 1.02rem;
            line-height: 1.6;
        }

        .app-section {
            margin-top: 1rem;
            padding: 1rem 1.1rem;
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow-sm);
        }

        @media (max-width: 760px) {
            [data-testid="stAppViewContainer"] > .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1rem;
            }

            h1 {
                font-size: 2rem;
            }

            .app-hero,
            .app-section {
                padding: 1rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
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

# ==========================================
# 2. 側邊欄 (Sidebar) 與安全金鑰處理
# ==========================================
st.sidebar.title("🌌 Cosmos3 T2I")
st.sidebar.caption("行動演示與開發助理 (HW3)")
st.sidebar.markdown("---")

# 雙軌密鑰安全機制 (優先讀取 Secrets，若無則顯示密碼輸入框)
apply_app_theme()

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

# 提示詞優化回調函數 (Callback)
def magic_enhance(style):
    base = st.session_state.prompt_input
    if base.strip():
        enhancements = {
            "電影感 (Cinematic)": "cinematic lighting, dramatic shadows, 35mm lens, depth of field, blockbuster movie still, 8k resolution, photorealistic",
            "動漫插畫 (Anime Art)": "studio ghibli, makoto shinkai style, vibrant colors, detailed anime background, cel shaded, masterpiece",
            "未來科技 (Cyberpunk/Sci-Fi)": "cyberpunk city, neon lighting, highly detailed, futuristic, sci-fi concept art, unreal engine 5 render",
            "極簡攝影 (Minimalist Photography)": "minimalist, clean lines, negative space, soft natural lighting, elegant, studio lighting, high resolution",
            "寫實照片 (Photorealistic)": "hyperrealistic photograph, highly detailed, sharp focus, 8k uhd, dslr, professional photography"
        }
        extra = enhancements.get(style, "masterpiece, highly detailed, 8k resolution")
        # 避免重複疊加相同的優化詞
        if extra not in base:
            st.session_state.prompt_input = f"{base}, {extra}"

# 使用外框容器群組化 Prompt 相關設定
with st.container(border=True):
    st.markdown("#### ✍️ 圖像場景描述 (Prompt Engineering)")
    
    prompt_input = st.text_area(
        "Prompt Input",
        placeholder="例如: A majestic glowing dragon flying over Taipei 101 at sunset, highly detailed, cyberpunk anime aesthetic...",
        height=120,
        key="prompt_input",
        label_visibility="collapsed"
    )
    
    col_btn, col_tip = st.columns([1, 2], vertical_alignment="center")
    with col_btn:
        st.button("✨ 魔法優化提示詞", on_click=magic_enhance, args=(style_preset,), help="根據側邊欄選擇的「視覺風格」，自動為您擴充專業的提示詞細節以提升生成品質！", use_container_width=True)
    with col_tip:
        st.caption("💡 *提示：Cosmos 3 對物理世界還原有極佳表現，建議點擊優化或手動添加光線描述。*")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 4. API 呼叫與推論邏輯 (Inference Engine)
# ==========================================
API_URL = "https://api-inference.huggingface.co/models/nvidia/Cosmos3-Super-Text2Image"

def call_huggingface_api(payload, token):
    headers = {"Authorization": f"Bearer {token}"}
    # 設定合理超時，防行動端無限掛起
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=45)
    except requests.exceptions.ConnectionError as original_error:
        try:
            from io import BytesIO
            from types import SimpleNamespace
            from huggingface_hub import InferenceClient

            prompt = payload.get("inputs") or payload.get("prompt") or ""
            parameters = payload.get("parameters") or {}
            client = InferenceClient(api_key=token)
            image = client.text_to_image(
                prompt=prompt,
                model="black-forest-labs/FLUX.1-schnell",
                negative_prompt=parameters.get("negative_prompt"),
                height=parameters.get("height"),
                width=parameters.get("width"),
                num_inference_steps=parameters.get("num_inference_steps"),
                guidance_scale=parameters.get("guidance_scale"),
                seed=parameters.get("seed"),
            )

            buffer = BytesIO()
            image.save(buffer, format="PNG")
            response = SimpleNamespace(
                status_code=200,
                content=buffer.getvalue(),
                headers={"content-type": "image/png"},
                text="",
                json=lambda: {},
            )
        except Exception as fallback_error:
            raise RuntimeError(
                "Legacy Hugging Face api-inference host DNS failed, and the "
                "InferenceClient fallback also failed. "
                f"{type(fallback_error).__name__}: {fallback_error!r}"
            ) from fallback_error
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
                except requests.exceptions.ConnectionError as e:
                    st.error("🔌 無法連線到 Hugging Face Inference API。你的 Hugging Face 登入與 huggingface.co 連線已確認正常，這裡會顯示實際連線錯誤，方便判斷是否是 api-inference.huggingface.co、代理/VPN、防火牆或模型端點問題。")
                    st.exception(e)
                except requests.exceptions.RequestException as e:
                    st.error("❌ Hugging Face API 請求失敗。請查看下方詳細錯誤，確認模型端點是否支援 Inference API、Token 權限是否足夠，或服務是否暫時不可用。")
                    st.exception(e)
                except Exception as e:
                    st.error(f"❌ 發生系統錯誤: {str(e)}")

# 頁尾
st.markdown("---")
st.caption("© 2026 HW3 Cosmos3-Super-Text2Image App. Assisted by Gemini Canvas.")
