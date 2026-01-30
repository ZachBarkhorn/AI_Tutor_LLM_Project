# AI Python Tutor

An interactive, AI-powered Python tutor designed for beginners.  
This project uses a large language model (LLM) to explain Python concepts, generate examples, debug code, create practice exercises, and evaluate student responses through a command-line interface.

The system focuses on **prompt engineering**, **structured LLM outputs**, and **token-efficient design** to tailor responses for specific educational tasks.

---

## Why I Built This

This project was developed as part of my **Artificial Intelligence coursework**, with the goal of exploring how **prompt engineering and tokenization strategies** can be used to guide large language models toward more accurate, task-specific outputs.

Rather than treating the LLM as a general chatbot, this project emphasizes:
- Designing **task-constrained prompts** based on user intent
- Structuring prompts to maximize clarity while minimizing unnecessary token usage
- Using different prompt templates to optimize model behavior for explanation, debugging, and evaluation tasks

The project demonstrates how LLMs can be adapted into **purpose-built tools** instead of generic conversational systems.

---

## Features

- **Explain a concept**  
  Provides clear, step-by-step explanations of Python topics tailored for beginners.

- **Debug code**  
  Identifies common Python errors and offers guided suggestions for fixing them.

- **Generate examples**  
  Creates simple Python code examples demonstrating specific concepts.

- **Create exercises**  
  Generates beginner-level practice problems for hands-on learning.

- **Evaluate answers**  
  Assesses a user’s solution and provides constructive, targeted feedback.

- **Interaction logging**  
  Automatically logs prompts, responses, and usage metrics for analysis and future improvement.

---

## Technologies Used

- Python  
- Ollama Cloud API (LLM inference)  
- Prompt engineering for task-specific outputs  
- Command-line interface (CLI)

---

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>

2. Install dependencies:

   pip install -r requirements.txt


3. Set your Ollama API key (from ollama.com) as an environment variable.

## Usage

Run the main application:

python main.py


Use the interactive menu to select a mode:

Explain a concept

Debug code

Generate an example

Create an exercise

Evaluate an answer

After selecting a mode, enter your prompt in the terminal.
The application dynamically applies mode-specific prompt templates designed to guide the LLM toward accurate, beginner-friendly responses optimized for the selected task.
