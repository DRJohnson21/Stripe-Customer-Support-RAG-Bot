# Stripe RAG Chatbot

This repo contains a basic local Streamlit chatbot for the Stripe customer support RAG project. The app connects to an Azure OpenAI model deployment using values stored in a local `.env` file.

## 1. Create a Project Folder

Create a folder on your computer where you want to store the project (example folder name: stripe-rag-chatbot).

```bash
mkdir stripe-rag-chatbot
cd stripe-rag-chatbot
```

## 2. Clone the GitHub Repo

From inside the project folder, run:

```bash
git clone https://github.com/DRJohnson21/Stripe-Customer-Support-RAG-Bot
```

Then move into the cloned repo folder:

```bash
cd Stripe-Customer-Support-RAG-Bot
```

## 3. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

For Mac/Linux:

```bash
source .venv/bin/activate
```

After activation, you should see `(.venv)` at the beginning of your terminal line.

## 4. Install Required Packages

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## 5. Create the `.env` File

Create a new file in the project folder named:

```text
.env
```

Copy the contents of `.env.template` into `.env`.

Then fill in the Azure OpenAI values:

```env
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini-stripe-rag
AZURE_OPENAI_API_VERSION=2025-01-01-preview
```

The `.env` file must be in the same folder as `app.py`.

## 6. Run the Chatbot

From the project folder, run:

```bash
streamlit run app.py
```

Streamlit will start a local server and show a localhost URL in the terminal, usually:

```text
http://localhost:8501
```

Open that URL in your browser to use the chatbot.

## 7. Stop the Chatbot

To stop the app, go back to the terminal and press:

```bash
Ctrl + C
```

## Notes

Do not commit the real `.env` file to GitHub. Only `.env.template` should be included in the repo.
