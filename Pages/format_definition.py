import streamlit as st

def main():
    st.title("Define Document Format")

    st.subheader("Expected Document Structure")
    st.write("To convert your DOCX files to JSON, please define the following prefixes:")
    
    # Input for prefixes
    question_prefix = st.text_input("Question Prefix (e.g., 'Question:')", "Question:")
    option_prefix = st.text_input("Option Prefix (e.g., 'Option:')", "Option:")
    answer_prefix = st.text_input("Answer Prefix (e.g., 'Answer:')", "Answer:")

    st.subheader("Example DOCX Format")
    st.write("Please format your document as follows:")
    st.write("```\n"
             "Question: Which sorting algorithm has the best average-case time complexity?\n"
             "Option: A. Merge Sort\n"
             "Option: B. Quick Sort\n"
             "Option: C. Bubble Sort\n"
             "Option: D. Insertion Sort\n"
             "Answer: A. Merge Sort\n"
             "```")

    st.subheader("Example JSON Output Structure")
    example_json = {
        "question": "Sample question here",
        "options": [
            {"answer": "Option 1", "isCorrect": False},
            {"answer": "Option 2", "isCorrect": True},
            {"answer": "Option 3", "isCorrect": False}
        ]
    }
    st.json(example_json)

if __name__ == "__main__":
    main()
