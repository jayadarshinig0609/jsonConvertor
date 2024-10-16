import json
from docx import Document

def parse_doc(doc_file, doc_format):
    document = Document(doc_file)
    doc_data = []
    
    current_data = {}
    options = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        # Split document format logic
        if text.startswith(doc_format["question_prefix"]):
            # Save the previous question data
            if current_data:
                current_data["options"] = options
                doc_data.append(current_data)
                current_data = {}
                options = []

            # Capture question
            current_data["question"] = text[len(doc_format["question_prefix"]):].strip()

        elif text.startswith(doc_format["option_prefix"]):
            # Capture options
            option_text = text[len(doc_format["option_prefix"]):].strip()
            is_correct = doc_format["answer_prefix"] in option_text
            options.append({
                "answer": option_text.replace(doc_format["answer_prefix"], "").strip(),
                "isCorrect": is_correct
            })

    # Append the last question data
    if current_data:
        current_data["options"] = options
        doc_data.append(current_data)

    return doc_data

def convert_to_json(parsed_data):
    return json.dumps(parsed_data, indent=4)

def convert_custom_text_to_json(custom_text, json_structure):
    lines = custom_text.strip().split("\n")
    json_data = []

    for line in lines:
        if json_structure["question_prefix"] in line:
            question = line.replace(json_structure["question_prefix"], "").strip()
            options = []
            # Here we assume options are provided in the next lines
            continue
        
        if json_structure["option_prefix"] in line:
            option = line.replace(json_structure["option_prefix"], "").strip()
            is_correct = json_structure["answer_prefix"] in option
            options.append({
                "answer": option.replace(json_structure["answer_prefix"], "").strip(),
                "isCorrect": is_correct
            })
        
        if question and options:
            json_data.append({
                "question": question,
                "options": options
            })
    
    return json.dumps(json_data, indent=4)
