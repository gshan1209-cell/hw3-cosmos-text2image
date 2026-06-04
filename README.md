HW3: Cosmos3-Super-Text2Image App

Project Goal

This project is an interactive web application that integrates NVIDIA's state-of-the-art Cosmos3-Super-Text2Image (64B) foundation model via the Hugging Face Inference API. Designed to provide a responsive and mobile-friendly AI generation experience, the app assists students in fulfilling the requirements for HW3.

Model

Core Model: nvidia/Cosmos3-Super-Text2Image

Specialization: 64B parameter text-to-image specialization designed for high-fidelity physical scene simulation.

Key Features

Interactive Controls (Sidebar Steerability): Supports custom Image Style presets, Aspect Ratio options, Seed randomizers, and Negative Prompt exclusions.

Dual-Tier Security Credentials: Prioritizes st.secrets authentication for production and provides a secure, hidden password text input fallback on the sidebar for local runs.

Mock/Demo Fallback Mode: Specifically engineered for physical/mobile presentations. When Hugging Face server nodes are queuing or offline, the toggled Mock Mode delivers simulated high-quality visuals seamlessly to prevent demonstration deadlocks.

How to Run Locally

1. Clone the repository

git clone [https://github.com/yourname/hw3-cosmos-text2image.git](https://github.com/yourname/hw3-cosmos-text2image.git)
cd hw3-cosmos-text2image


2. Install dependencies

pip install -r requirements.txt


3. Setup Secrets

To avoid hardcoding your Hugging Face API keys:

Option A: Input your token directly into the sidebar password field when running the app.

Option B: Create a .streamlit/secrets.toml file locally and add your credentials:

HF_TOKEN = "your_huggingface_read_token_here"


4. Execute the application

streamlit run app.py


Deployment to Streamlit Community Cloud

Push your completed repository code to GitHub (making sure .gitignore excludes your secrets).

Go to Streamlit Share and log in with your GitHub account.

Click "New App", choose your repository, branch, and set the entry file to app.py.

Under "Advanced Settings", find the Secrets section and add your API credentials securely:

HF_TOKEN = "your_huggingface_read_token_here"


Click "Deploy". Your live app will be ready within minutes!

Links

GitHub Repository: https://github.com/yourname/hw3-cosmos-text2image

Streamlit Live Demo: https://your-app-name.streamlit.app

Screenshots

(Add screenshots of your home page and generation results here)