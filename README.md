# AI-powered Interview Question Generator
Automatically generate interview questions for a provided role in seconds. This app uses artificial inteligence (AI) to understand and generate 3 thoughtful interview questions tailored to a job role provided to it.

## Architecture / Flow
1. It features a simple text input-box where the job title/role is collected.
2. The data is then sent to an AI model with a carefully constructed prompt via provider's API request to the model's server.
3. During this process, a loading spinner is shown to the user on the frontend to inform them of the job being done at the backend.
4. The AI then responds back with a JSON array containing generated interview questions.
5. Loading spinner is removed and questions are shown to the user.

## Technology
* Frontend: Streamlit
* Backend: Python + Ollama client
* Model: Gemma 4 (via Ollama)

## Demo
* **Live at:** [https://interviewer-ai.streamlit.app](https://interviewer-ai.streamlit.app)
* **GitHub repo:** You're already here!
* **Loom video:**

[![Video Title](https://cdn.loom.com/sessions/thumbnails/31b3ca781dd44e7c8ef8f9e8e72e1af5-6c2d31303925ee9d-full-play.gif#t=0.1)](https://www.loom.com/share/31b3ca781dd44e7c8ef8f9e8e72e1af5)
