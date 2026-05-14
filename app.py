import streamlit as st
from logic import get_interview_questions

st.title("AI Powered Recruiter")
st.write("Get insightful interview questions tailored to your job title in seconds")

# Default used in absense of role input
job_title = "Customer Success Manager"
input_title = st.text_input(
    "Type in your job title",
    placeholder="Customer Success Manager",
)

job_title = input_title if input_title != "" else job_title

# Generate questions when job_title changes or button is clicked
if st.button(label="Submit", type="primary") or job_title:
    with st.spinner():
        questions = get_interview_questions(job_title)
    st.write(questions)
