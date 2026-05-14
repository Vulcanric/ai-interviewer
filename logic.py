import os
import json
from ollama import Client
from dotenv import load_dotenv

load_dotenv()


def get_interview_questions(job_title: str) -> list[str]:
    """Invokes AI API to generate interview questions

    Args:
      job_title (str): role to generate interview questions for

    Returns:
      list[str]: A list of AI-generated interview questions.
    """
    ollama = Client(
        host="https://ollama.com",
        headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"},
    )
    generated = ollama.generate(
        model="gemma4:31b-cloud",
        system=f"""
        You are an expert technical recruiter and hiring manager. Your task is to generate exactly 3 thoughtful, highly specific, and relevant interview questions for the job title the user will provide.

Instructions:
1. Analyze the core competencies, required technical skills, and typical challenges associated with the job title.
2. Avoid generic behavioral questions like "What are your strengths?" or "Where do you see yourself in 5 years?".
3. Craft exactly 3 distinct questions. Each question must target a different critical dimension of the role (e.g., technical problem-solving, situational judgment, cross-functional collaboration, or leadership).
4. Keep the questions direct, professional, and engaging.

Output Format:
Return ONLY a valid JSON array containing exactly three string elements. Do not include introductory text, markdown formatting, explanations, or trailing text. 

Example Output:
[
  "Question 1 text...",
  "Question 2 text...",
  "Question 3 text..."
]

        """,
        prompt=f"Job Title: {job_title}",
    )

    questions = json.loads(generated.response or "[]")

    return questions
