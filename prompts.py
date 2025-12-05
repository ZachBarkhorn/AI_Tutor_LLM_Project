# prompts.py

# System prompt - defines AI behavior
SYSTEM_PROMPT = """
You are an AI tutor for beginner Python programmers.
Explain concepts clearly and step by step.
Provide examples when needed.
If code has errors, debug and explain the errors.
Always be friendly and encouraging.
"""

# Debugging prompt - AI checks and fixes code
DEBUG_PROMPT = """
The user wrote this Python code:

{user_code}

Check the code for errors.
Explain each error in simple terms.
Provide a corrected version of the code.
"""

# Exercise generation prompt - AI creates practice exercises
EXERCISE_PROMPT = """
Create a beginner Python exercise.
Include:
- Problem description
- Example input/output
- Difficulty level (easy)
"""

# Evaluation prompt - AI evaluates user answers
EVALUATION_PROMPT = """
The user submitted this answer:

{user_answer}

Check if it correctly solves the problem:

{exercise_description}

Give feedback on what is correct, what is wrong, and hints for improvement.
"""
