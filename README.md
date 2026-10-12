# 🚀 GenAI by CampusX - LangChain Models

A hands-on, structured guide and codebase exploring various **Generative AI models and integrations using LangChain**. This repository covers legacy LLMs, modern Chat Models across multiple providers (OpenAI, Anthropic, Google Gemini, Hugging Face), and Embedding Models.

---

## 📂 Project Structure

```text
langchain_models/
│
├── 1.LLMs/
│   └── 1_llms_openai.py             # OpenAI Text Completion (Legacy LLM)
│
├── 2.ChatModels/
│   ├── 1_chatmodel_openai.py        # OpenAI Chat Models (GPT-4)
│   ├── 2_chatmodel_anthropic.py     # Anthropic Claude (Claude 3.5 Sonnet)
│   ├── 3_chatmodel_google.py        # Google Generative AI (Gemini)
│   ├── 4_chatmodel_hf_api.py        # Hugging Face Inference API (Serverless)
│   └── 5_chatmodel_hf_local.py      # Hugging Face Pipeline (Local inference)
│
├── EmbeddingModels/                 # Text Embeddings & Vector Representations (Upcoming)
│
├── .gitignore                       # Git ignore rules for venv, env files, cache
├── .env.example                     # Sample environment variable template
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

---

## 🛠️ Tech Stack & Integrations

- **Orchestration Framework:** [LangChain](https://www.langchain.com/) (`langchain`, `langchain-core`)
- **Model Providers:**
  - **OpenAI:** `langchain-openai` (GPT-4, GPT-3.5)
  - **Anthropic:** `langchain-anthropic` (Claude 3.5 Sonnet)
  - **Google Gemini:** `langchain-google-genai`
  - **Hugging Face:** `langchain-huggingface`, `transformers`, `huggingface-hub`
- **Environment Management:** `python-dotenv`
- **Scientific Computing:** `numpy`, `scikit-learn`

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Apsiingh/GenAI-By-CampusX.git
cd GenAI-By-CampusX
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory (refer to `.env.example`):

```bash
# OpenAI API Key
OPENAI_API_KEY="your-openai-api-key"

# Anthropic API Key
ANTHROPIC_API_KEY="your-anthropic-api-key"

# Google Gemini API Key
GOOGLE_API_KEY="your-google-api-key"

# Hugging Face Token
HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"
```

---

## 📖 Module Overviews

### 1. Legacy LLMs (`1.LLMs/`)
- Demonstrates standard text completion models (`OpenAI`) taking plain text prompts and returning text completions.

### 2. Chat Models (`2.ChatModels/`)
Explores modern conversational models working with structured message formats:
- **OpenAI (`1_chatmodel_openai.py`):** Uses `ChatOpenAI` with configuration parameters such as `temperature` and `max_completion_tokens`.
- **Anthropic (`2_chatmodel_anthropic.py`):** Connects to Claude 3.5 Sonnet via `ChatAnthropic`.
- **Google Gemini (`3_chatmodel_google.py`):** Uses `ChatGoogleGenerativeAI` to interact with Gemini models.
- **Hugging Face API (`4_chatmodel_hf_api.py`):** Leverages `HuggingFaceEndpoint` to interact with cloud-hosted open-source models (e.g., `TinyLlama`).
- **Hugging Face Local (`5_chatmodel_hf_local.py`):** Downloads and runs local open-source models through `HuggingFacePipeline`.

### 3. Embedding Models (`EmbeddingModels/`)
- Demonstrates vector embeddings and similarity computations for downstream tasks like semantic search and RAG.

---

## 🏃 Running the Examples

Run any script directly using Python:

```bash
# Run OpenAI Chat Model example
python 2.ChatModels/1_chatmodel_openai.py

# Run Anthropic Claude example
python 2.ChatModels/2_chatmodel_anthropic.py

# Run Hugging Face Local Pipeline example
python 2.ChatModels/5_chatmodel_hf_local.py
```

---

## 📌 References & Learning Resources
- [CampusX GenAI Course](https://www.campusx.in/)
- [LangChain Documentation](https://python.langchain.com/)
- [Hugging Face Models](https://huggingface.co/models)