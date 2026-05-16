import streamlit as st
from logic import get_interview_questions

st.title("AI Interviewer")
st.write("Get thoughtful interview questions tailored to your job title in seconds")

# Default used in absense of role input
job_title = "Customer Success Manager"
input_title = st.text_input(
    "Type in your job title",
    placeholder="Customer Success Manager",
)

# Use default job title only if input title is not provided
job_title = input_title if input_title != "" else job_title

# Generate questions when job_title changes or button is clicked
if st.button(label="Submit", type="primary") or job_title:
    # Showing a loading spinner to inform users of ongoing API request
    with st.spinner():
        questions = get_interview_questions(job_title)
    # Display result
    for i, ques in enumerate(questions):
        col1, col2 = st.columns([0.1, 0.8], vertical_alignment="center")
        col1.write(f"#### {i + 1}")
        col2.write(f"#### {ques}")
    # Display actual API response in an expander
    with st.expander("See API result"):
        st.write(questions)
