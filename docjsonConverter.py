import streamlit as st
import json
import re

# Function to process the provided text and convert it into JSON structure
def convert_to_json(raw_text):
    question_blocks = re.split(r'\d+\.', raw_text)[1:]  # Split the text into blocks starting from 1.
    question_list = []
    comment_number = 1

    for block in question_blocks:
        lines = block.strip().split('\n')
        
        if len(lines) < 2:  # Ensure there are at least a question and options
            continue
        
        # Extract the question part (first line after splitting by \d+\.)
        question = lines[0].strip()

        # Extract the options
        options = []
        for line in lines[1:]:
            line = line.strip()
            if re.match(r'^[A-D]\.', line):  # Option lines start with A., B., C., D.
                options.append(line[3:].strip())  # Remove 'A. ' or 'B. ' and get the option text
            
            if line.startswith("Answer:"):
                correct_answer = line.replace("Answer:", "").strip()  # Extract the correct answer
        
        # Append the question with its options and the correct answer to the list
        question_list.append({
            "_comment": str(comment_number),
            "question": question,
            "options": [{"answer": opt, "isCorrect": opt == correct_answer} for opt in options]
        })
        
        comment_number += 1

    return json.dumps(question_list, indent=4)

# Streamlit UI
st.title("Document Text to JSON Converter")

# Text input for the document-like format
raw_text = st.text_area("Enter your questions and options text below:", height=400)

if st.button("Convert to JSON"):
    if raw_text:
        json_result = convert_to_json(raw_text)
        st.subheader("Converted JSON")
        st.code(json_result, language='json')
    else:
        st.warning("Please provide some text to convert.")



