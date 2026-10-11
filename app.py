import streamlit as st
import json
import os
from agent import generate_qa_artifacts

st.title("QA Triage & Test Case Agent")
st.write("Upload a bug report or requirement text file. It will process it, save it locally, and generate a downloadable JSON report.")

# Ensure local directories exist
os.makedirs("inputs", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# File uploader widget
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file is not None:
    # 1. Save the uploaded file to the local 'inputs/' folder
    input_path = os.path.join("inputs", uploaded_file.name)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    # Read content safely from the uploaded file buffer for processing
    file_content = uploaded_file.getvalue().decode("utf-8")
    
    st.subheader("Input Preview:")
    st.text(file_content[:300] + "..." if len(file_content) > 300 else file_content)
    
    # 2. Generate the QA artifacts using your core logic from agent.py
    artifact = generate_qa_artifacts(file_content)
    
    # 3. Save the output to the local 'outputs/' folder automatically
    base_name = os.path.splitext(uploaded_file.name)[0]
    output_filename = f"{base_name}_report.json"
    output_path = os.path.join("outputs", output_filename)
    
    with open(output_path, "w", encoding="utf-8") as out_f:
        json.dump(artifact, out_f, indent=2)
        
    st.success(f"Successfully saved input to `inputs/{uploaded_file.name}` and output to `outputs/{output_filename}`!")
    
    st.subheader("Generated JSON Output:")
    st.json(artifact)
    
    # Download button for the output JSON
    json_string = json.dumps(artifact, indent=2)
    st.download_button(
        label="Download JSON Report",
        data=json_string,
        file_name=output_filename,
        mime="application/json"
    )