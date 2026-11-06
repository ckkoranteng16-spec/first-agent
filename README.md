Writing

---

title: Gemini Function Calling Agent
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false

Gemini Function Calling Agent

A Python-based AI agent that uses Google's Gemini API and function calling to interact with custom Python functions.

The project demonstrates how Large Language Models (LLMs) can go beyond generating text by selecting and executing external functions to perform specific tasks.

Features

- LLM Integration: Uses Google's Gemini API for natural language understanding and response generation.
- Function Calling: Allows Gemini to identify and call appropriate Python functions based on user requests.
- Automatic Function Execution: Executes requested functions and provides their results back to Gemini.
- Interactive Interface: Provides a conversational interface built with Gradio.

Available Functions

The agent currently includes nine custom Python functions:

1. "alxValue"
2. "bpeEncode"
3. "cipher"
4. "decipher"
5. "gridWalker"
6. "isBalanced"
7. "scoreword"
8. "sortAscending"
9. "daysToDeadline"

Technologies Used

- Python
- Google Gemini API
- Gradio
- Hugging Face Spaces

Project Structure

first-agent/
│
├── app.py
├── function_agent.py
├── requirements.txt
├── README.md
└── .gitignore

How It Works

1. A user submits a message through the Gradio interface.
2. The message is passed to the Gemini model.
3. Gemini determines whether one of the available Python functions is needed.
4. The requested function is executed automatically.
5. The function result is returned to Gemini.
6. Gemini generates a response for the user.

Installation

Install the required dependencies:

pip install -r requirements.txt

API Configuration

This project requires a valid Gemini API key.

Set the "GEMINI_API_KEY" environment variable before running the application.

For Hugging Face Spaces, configure the key under:

Settings → Secrets → New Secret

Never commit API keys or other credentials to the repository.

Running Locally

Start the Gradio application:

python app.py

Gradio will provide a local URL where the application can be accessed.

Deployment

The application is configured for deployment on Hugging Face Spaces using the Gradio SDK.

Author

Developed as a practical project exploring Python, Large Language Models, and AI agent development.