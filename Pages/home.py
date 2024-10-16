import streamlit as st
from utils.converter import parse_doc, convert_to_json, convert_custom_text_to_json

def main():
    st.title("DOC to JSON Converter")
import streamlit as st
import json

# Function to convert the input to the required JSON format
def convert_to_json(question, options):
    options_list = []
    for option in options:
        options_list.append({"answer": option, "isCorrect": False})  # Default all to False

    # Update the correct answer based on user selection
    if correct_option in options:
        options_list[options.index(correct_option)]["isCorrect"] = True

    # Create the final JSON structure
    json_structure = {
        "question": question,
        "options": options_list
    }

    return json_structure

# Streamlit app layout
st.title("Question to JSON Converter")

# Input fields
question = st.text_input("Enter the question:")
options = st.text_area("Enter options (one per line):").splitlines()
correct_option = st.selectbox("Select the correct option:", options)

# Convert and display JSON
if st.button("Convert to JSON"):
    if question and options:
        json_output = convert_to_json(question, options)
        st.json(json_output)
        
        # Optional: Save JSON to a file
        json_file = st.file_uploader("Save JSON file", type='json')
        if json_file is not None:
            with open(json_file.name, 'w') as f:
                json.dump(json_output, f)
            st.success("JSON file saved successfully.")
    else:
        st.warning("Please enter both the question and options.")

if __name__ == "__main__":
    main()
