# Chat-Bot-Python-OpenAI-Chat-Bot-using-Python-and-OpenAI
This repository contains a simple Python command-line chatbot that uses the DeepSeek R1-Chimera model through the OpenRouter API. Although the openai Python library is imported, the script does not connect to OpenAI. Instead, it uses a custom base_url to communicate directly with OpenRouter, which supports the same API format.
# Python Command-Line Chatbot Using DeepSeek via OpenRouter

This repository contains a simple Python-based chatbot that uses the **DeepSeek R1-Chimera** model via the **OpenRouter API**. Although the `openai` Python library is used, the chatbot does **not** connect to OpenAI. Instead, it communicates with OpenRouter using the same API format that OpenAI uses, allowing you to interact with DeepSeek efficiently.

## Features
- Interactive command-line chatbot
- Uses **DeepSeek R1-Chimera** model for AI responses
- Securely loads API key from a `.env` file
- Continuous chat until the user types `"bye"`

## Requirements
- Python 3.10 or above
- `openai` Python library
- `python-dotenv` library

You can install the required libraries using:

```bash
pip install openai python-dotenv


##setup
git clone <your-repo-url>
cd <your-repo-folder>
