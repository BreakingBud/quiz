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
]

# Add more questions here with explanations
questions.extend([
    {
        "question": "What is the primary purpose of the 'Reading Data' technique in AI Studio?",
        "options": [
            "A) To write the data into a database",
            "B) To load data from external sources into the platform",
            "C) To transform raw data into a structured format",
            "D) To apply statistical analysis to the data"
        ],
        "answer": "B",
        "explanation": "The 'Reading Data' technique is used to load data from external sources into AI Studio for analysis."
    },
    {
        "question": "What is the purpose of the 'Results View' in AI Studio?",
        "options": [
            "A) To visualize raw data before processing",
            "B) To display the outcomes of a process or workflow",
            "C) To select specific data points for transformation",
            "D) To configure data operators"
        ],
        "answer": "B",
        "explanation": "The 'Results View' shows the outcomes of workflows after they have been executed in AI Studio."
    },
    {
        "question": "When selecting attributes from joined ExampleSets in AI Studio, the primary goal is to:",
        "options": [
            "A) Merge all attributes into one column",
            "B) Filter only relevant attributes for analysis",
            "C) Delete unnecessary attributes from the dataset",
            "D) Transform categorical data into numerical form"
        ],
        "answer": "B",
        "explanation": "When selecting attributes, the goal is to filter only relevant attributes from the joined datasets for further analysis."
    },
    {
        "question": "Which of the following is a common technique for transforming or cleansing data in AI Studio?",
        "options": [
            "A) Running machine learning models",
            "B) Normalizing or scaling numerical values",
            "C) Joining ExampleSets from different sources",
            "D) Visualizing data trends"
        ],
        "answer": "B",
        "explanation": "Transforming or cleansing data commonly involves normalizing or scaling numerical values to ensure consistency in analysis."
    },
    {
        "question": "In AI Studio, using an operator allows you to:",
        "options": [
            "A) Modify the user interface",
            "B) Perform specific actions on data like filtering or transforming",
            "C) Manually enter data for analysis",
            "D) Save workflows to an external system"
        ],
        "answer": "B",
        "explanation": "Operators in AI Studio are used to perform specific actions on data, such as filtering, transforming, or aggregating it."
    },
    {
        "question": "What is the primary purpose of 'Writing Data' in AI Studio?",
        "options": [
            "A) To display the workflow results",
            "B) To save processed data to an external file or database",
            "C) To transform data into readable formats",
            "D) To load raw data into the platform for further analysis"
        ],
        "answer": "B",
        "explanation": "The 'Writing Data' technique is used to save processed data to external files or databases for further use or storage."
    },
    {
        "question": "What is the primary purpose of data discovery in AI Studio?",
        "options": [
            "A) To find hidden patterns in data using machine learning",
            "B) To explore and understand the data before performing analysis",
            "C) To visualize the final outcomes of a workflow",
            "D) To create automated workflows for data cleansing"
        ],
        "answer": "B",
        "explanation": "Data discovery is about exploring and understanding the data, identifying trends and patterns before performing deeper analysis."
    },
    {
        "question": "What is the main goal of data mining as a technique?",
        "options": [
            "A) To visualize data trends",
            "B) To discover patterns and relationships in large datasets",
            "C) To clean and prepare data for analysis",
            "D) To merge multiple datasets into one"
        ],
        "answer": "B",
        "explanation": "Data mining aims to discover patterns, relationships, and insights from large datasets, often using advanced techniques."
    },
    {
        "question": "Which aspect is most important when considering data quality in AI Studio?",
        "options": [
            "A) Ensuring that data is processed in real-time",
            "B) Verifying the accuracy, completeness, and consistency of the data",
            "C) Creating visualizations to interpret data",
            "D) Reducing the size of the dataset for efficiency"
        ],
        "answer": "B",
        "explanation": "Data quality focuses on ensuring that the data is accurate, complete, and consistent, which is essential for effective analysis."
    },
    {
        "question": "What is the primary purpose of the 'Drill Down' technique in AI Studio?",
        "options": [
            "A) To focus on a broad overview of the data",
            "B) To analyze data at a more detailed, granular level",
            "C) To filter out irrelevant data points",
            "D) To summarize data across multiple categories"
        ],
        "answer": "B",
        "explanation": "The 'Drill Down' technique helps analyze data at a more granular level, enabling deeper insights into specific data points."
    }
])

# Initialize session state for score and answered questions
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.answered_questions = 0

def main():
    st.title("Diagnostic Analytics Midterm MCQs")
    
    # Display the real-time score in the sidebar
    st.sidebar.header("Real-Time Score")
    st.sidebar.write(f"Score: {st.session_state.score}/{len(questions)}")
    
    # Iterate over the questions
    for i, question in enumerate(questions):
        st.write(f"### Question {i + 1}: {question['question']}")
        user_answer = st.radio(f"Select your answer for Question {i + 1}:", question['options'], key=f"q_{i}")

        # Show the correct answer and explanation if user clicks "Show Answer"
        if st.button(f"Submit Answer for Question {i + 1}", key=f"submit_{i}"):
            if user_answer == question["answer"]:
                st.success(f"Correct! The answer is: {question['answer']}. {question['explanation']}")
                if st.session_state.answered_questions <= i:
                    st.session_state.score += 1  # Increase score for correct answer
                    st.session_state.answered_questions += 1
            else:
                st.error(f"Incorrect. The correct answer is: {question['answer']}. {question['explanation']}")
                if st.session_state.answered_questions <= i:
                    st.session_state.answered_questions += 1

    # Display the final score if all questions are answered
    if st.session_state.answered_questions == len(questions):
        st.write(f"### Your final score is: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()
