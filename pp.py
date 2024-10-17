import streamlit as st

# Define the questions, options, correct answers, and explanations
questions = [
    {
        "question": "What is the primary purpose of aggregating or filtering data in AI Studio?",
        "options": [
            "A) To reduce the size of the dataset for performance improvement",
            "B) To clean data by removing duplicate entries",
            "C) To create new insights by summarizing or isolating specific data points",
            "D) To transform raw data into a readable format"
        ],
        "answer": "C",
        "explanation": "Aggregating or filtering data helps create insights by summarizing or isolating specific data points relevant to the analysis."
    },
    {
        "question": "Which of the following is a key technique in creating a process or workflow in AI Studio?",
        "options": [
            "A) Writing SQL queries",
            "B) Dragging and dropping operators into a canvas",
            "C) Performing manual data entry",
            "D) Using pre-built machine learning models"
        ],
        "answer": "B",
        "explanation": "AI Studio allows creating workflows by dragging and dropping operators to visually design processes without manually writing code."
    },
    {
        "question": "In AI Studio, what does the 'Design View' primarily allow users to do?",
        "options": [
            "A) View raw data before any processing",
            "B) Design and visualize workflows using operators",
            "C) Monitor the performance of algorithms in real-time",
            "D) Generate summary statistics from the data"
        ],
        "answer": "B",
        "explanation": "The 'Design View' in AI Studio enables users to visually design and structure workflows using different operators."
    },
    {
        "question": "What is the main function of joining ExampleSets in AI Studio?",
        "options": [
            "A) To merge multiple datasets based on common attributes",
            "B) To clean and transform raw data",
            "C) To apply machine learning algorithms on combined datasets",
            "D) To split datasets into smaller parts for analysis"
        ],
        "answer": "A",
        "explanation": "Joining ExampleSets allows merging multiple datasets based on shared attributes to perform analysis on the combined data."
    },
    {
        "question": "Which of the following best describes the 'Modes / Views / Components' in AI Studio?",
        "options": [
            "A) They refer to different ways to visualize the same dataset",
            "B) They offer options for transforming data into various formats",
            "C) They allow users to switch between different stages of the workflow design",
            "D) They help users in selecting machine learning models"
        ],
        "answer": "C",
        "explanation": "Modes, views, and components in AI Studio allow users to shift between different stages of workflow design for building processes."
    }
    # Add more questions here in the same format
]

def show_question(index):
    st.write(f"**Question {index + 1}: {questions[index]['question']}**")
    user_answer = st.radio("Select your answer:", questions[index]['options'], key=index)
    return user_answer

def main():
    st.title("Diagnostic Analytics Midterm MCQs with Explanations")

    # Initialize session state to track answers
    if "responses" not in st.session_state:
        st.session_state.responses = [""] * len(questions)

    score = 0
    for i, question in enumerate(questions):
        st.markdown("---")
        user_answer = show_question(i)
        if st.button(f"Submit Answer for Question {i + 1}", key=f"submit_{i}"):
            if user_answer == question["answer"]:
                st.success(f"Correct! {question['explanation']}")
                score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {question['answer']}. {question['explanation']}")

    # Display final score
    st.write(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
