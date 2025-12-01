# 🧠 Python CLI Chatbot Using DeepSeek via OpenRouter

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-red)](https://openrouter.ai/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A simple **command-line chatbot** built in Python using the **DeepSeek R1-Chimera** model via **OpenRouter**.  
Although the `openai` library is imported, the chatbot **does not use OpenAI servers** — it communicates directly with OpenRouter using an OpenAI-compatible API format.

---

## ⚡ Features
- Interactive command-line chatbot  
- Uses **DeepSeek R1-Chimera** AI model  
- Loads API key securely from a `.env` file  
- Chat loop continues until the user types `"bye"`  
- Easy to extend for GUIs, web apps, or multiple AI models  

---

## 🛠 Requirements
- Python 3.10+  
- `openai` library  
- `python-dotenv` library  

Install dependencies:

```bash
pip install openai python-dotenv
