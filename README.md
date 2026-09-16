# Stripe Customer Support RAG Bot

A local Streamlit chatbot that answers Stripe customer-support questions using retrieval-augmented generation (RAG). Questions are answered by an Azure OpenAI model deployment that searches a vector store built from 30 Stripe documentation files.

> This is an personal project and is not affiliated with, endorsed by, or supported by Stripe. The files in `knowledge-base` are copies of Stripe's public documentation and remain Stripe's content.

## How it works

1. The user asks a question in the Streamlit chat interface.
2. `app.py` sends the full conversation, along with the system prompt in `system_prompt.py`, to the Azure OpenAI **Responses API** (`client.responses.create`).
3. The request includes the `file_search` tool, pointed at an Azure OpenAI vector store that contains the files in `knowledge-base`. The model retrieves relevant passages and answers from them.
4. The app post-processes the response:
   - **Confidence rating.** The system prompt tells the model to end every answer with `CONFIDENCE: HIGH`, `MEDIUM`, or `LOW`. The app removes this tag from the displayed text and uses it to decide what to show.
   - **Escalation banner.** When confidence is `LOW` or `MEDIUM`, the app shows a banner linking to Stripe Support, the Stripe Help Center, and Stripe Dashboard support.
   - **Source links.** Files returned by `file_search` are mapped to their titles and `docs.stripe.com` URLs and listed under the answer.

Model settings: `temperature=0.2`, `max_output_tokens=1500`.

## Assistant behavior (system prompt)

- Instructed to answer only from the documentation retrieved by file search, not from general knowledge. Unsupported answers are rated `LOW` and escalated.
- Keeps answers to 2–4 sentences with concrete next steps.
- Escalates to a human agent in these cases: missing or delayed funds, suspended or restricted accounts, refunds not received after 10 business days, and disputes involving fraud or unauthorized charges.
- Covers only Stripe payments, refunds, billing, subscriptions, invoices, error codes, payouts, disputes, and webhooks. Out-of-scope questions get a fixed redirect message.
- Refuses requests involving fraud, bypassing security, unauthorized refunds, or exposing card data.
- Opens with an empathetic line when the user sounds frustrated, and asks the user to retype messages that look like gibberish.

## Knowledge base

`knowledge-base` contains 29 Markdown pages from Stripe's documentation and 1 PDF of Stripe's FAQ for customers of businesses using Stripe. Together they cover:

- billing and subscriptions
- invoicing
- disputes
- refunds
- payouts
- webhooks
- error codes

## Project structure

```text
.
├── app.py              # Streamlit UI, Azure OpenAI call, confidence/escalation/citation handling
├── system_prompt.py    # System prompt defining scope, style, confidence, and escalation rules
├── knowledge-base/     # Source documents uploaded to the vector store
├── requirements.txt
├── .env.template
└── .gitignore
```

## Setup

Developed with Python 3.14.

### 1. Clone the repo

```bash
git clone https://github.com/DRJohnson21/Stripe-Customer-Support-RAG-Bot
cd Stripe-Customer-Support-RAG-Bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Azure OpenAI

You need all of the following:

- An Azure OpenAI resource.
- A model deployment.
- A vector store containing the files in `knowledge-base`. Upload those files to a vector store in your Azure OpenAI resource and copy its ID.

### 5. Create the `.env` file

Copy `.env.template` to a new file named `.env` in the same folder as `app.py`, then fill in your values:

```env
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
AZURE_OPENAI_API_VERSION=2025-03-01-preview
AZURE_OPENAI_VECTOR_STORE_ID=your_vector_store_id
```

The app stops with an error message if the endpoint, key, deployment, or vector store ID is missing. Never commit `.env`; it is already listed in `.gitignore`.

### 6. Run the chatbot

```bash
streamlit run app.py
```

Open the localhost URL shown in the terminal (usually `http://localhost:8501`). Press `Ctrl + C` in the terminal to stop the app.
