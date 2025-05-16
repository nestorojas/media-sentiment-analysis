# 📰 Political Sentiment Index on Financial News

This project analyzes financial news articles from North America using HuggingFace's `distilBERT` model to assign sentiment scores. The goal is to generate a Political Sentiment Index based on economic news coverage.

## 📦 Project Structure

political-sentiment-index/
├── news_sentiment_pipeline.py     # Main pipeline script
├── .env                           # Stores Newsdata.io API key (not committed)
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/political-sentiment-index.git
cd political-sentiment-index

2. Set Up a Virtual Environment
using conda:

conda create -n senti python=3.10 -y
conda activate senti

Optional: Jupyter Support
pip install notebook ipykernel
python -m ipykernel install --user --name=senti

3. Install Dependencies

pip install transformers torch requests python-dotenv pandas

🔐 API Key Setup (Newsdata.io)
	1.	Register at https://newsdata.io and get a free API key.
	2.	Create a .env file in the project root:

    NEWSDATA_API_KEY=your_api_key_here

🌐 Newsdata API Integration

3.1. Endpoint
https://newsdata.io/api/1/news

Parameter   Required    Description
apikey      ✅          Your Newsdata.io API key
country     ✅          Country code (us, ca, etc.)
language    Optional    Language code (recommended: en)
category    Optional    e.g., business, politics, etc.
