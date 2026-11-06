# Gemini Function-Calling Agent

A Python-based AI chatbot powered by Google's Gemini API. The project combines a function-calling agent, a FastAPI backend, and a personal portfolio frontend.

## Project Overview

This project demonstrates how an LLM can interact with predefined Python functions to perform tasks and return useful responses.

The application has three main components:

- **Gemini Agent:** Understands user requests and decides when to call available Python functions.
- **FastAPI Backend:** Exposes the agent and individual functions through HTTP endpoints.
- **Portfolio Frontend:** Provides a web interface where visitors can interact with the chatbot.

## Project Structure

```text
first-agent/
│
├── docs/
│   ├── index.html
│   ├── profile.png
│   ├── gmail.svg
│   ├── github.svg
│   └── linkedin.svg
│
├── backend/
│   ├── api.py
│   ├── app.py
│   ├── function_agent.py
│   └── requirements.txt
│
├── .gitignore
└── .env
```

## Available Python Functions

The agent has nine predefined functions:

1. `alxValue()` – Calculates an ASCII-based value and certification status.
2. `bpeEncode()` – Performs a simplified Byte Pair Encoding process.
3. `cipher()` – Encodes messages using a letter-shifting technique.
4. `decipher()` – Generates possible decoded messages.
5. `gridWalker()` – Analyses movement through a grid.
6. `isBalanced()` – Checks whether brackets are balanced.
7. `scoreword()` – Calculates a score based on repeated and unique letters.
8. `sortAscending()` – Sorts characters in ascending order.
9. `daysToDeadline()` – Calculates the time remaining until a deadline.

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- FastAPI
- Gradio
- Pydantic
- HTML, CSS and JavaScript
- Git and GitHub

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/ckkoranteng16-spec/first-agent.git
cd first-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Configure your API key

Create a `.env` file inside the `backend` folder:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your API key to GitHub.

### 5. Run the FastAPI backend

```bash
cd backend
uvicorn api:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/chat` | Send a message to the Gemini agent |
| POST | `/functions` | Execute a selected Python function |

### Example Chat Request

```json
{
  "message": "Encode HELLO using a shift of 3
