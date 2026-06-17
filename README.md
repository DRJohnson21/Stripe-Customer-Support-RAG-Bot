# Stripe RAG Chatbot

This is a basic local Streamlit chatbot that connects to an Azure OpenAI model deployment.

## Setup

1. Clone or download this repo.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a new file named `.env` in the project folder.

4. Copy the contents of `.env.template` into `.env`.

5. Fill in the values in `.env`:

```env
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini-stripe-rag
AZURE_OPENAI_API_VERSION=2025-01-01-preview
```

The `.env` file must be in the same folder as `app.py`.

## Run the Chatbot

Run this command from the project folder:

```bash
streamlit run app.py
```

Then open the localhost URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Stop the Chatbot

To stop the app, go back to the terminal and press:

```bash
Ctrl + C
```
