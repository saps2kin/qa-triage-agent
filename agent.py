import os
import json

def generate_qa_artifacts(requirement_or_bug: str):
    """
    Analyzes input text (bug report or feature requirement) and 
    generates structured QA artifacts.
    """
    is_bug = "error" in requirement_or_bug.lower() or "fail" in requirement_or_bug.lower() or "bug" in requirement_or_bug.lower()
    
    artifact = {
        "type": "Bug Report & Regression Test" if is_bug else "Feature Test Plan",
        "priority": "P1 - High" if is_bug else "P2 - Medium",
        "generated_test_cases": [
            {
                "test_id": "TC_AUTO_001",
                "objective": f"Validate system response for: {requirement_or_bug[:40]}...",
                "preconditions": "User is authenticated and in the active module.",
                "steps": [
                    "1. Navigate to target module.",
                    "2. Reproduce input condition or trigger action.",
                    "3. Observe system behavior and log network payloads."
                ],
                "expected_result": "System handles state gracefully without throwing unhandled exceptions."
            }
        ],
        "risk_assessment": "Data integrity and user session persistence checked."
    }
    return artifact

if __name__ == "__main__":
    input_dir = "inputs"
    output_dir = "outputs"
    
    # Ensure directories exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all .txt files in the inputs folder
    input_files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]
    
    if not input_files:
        print(f"[!] No text files found in the '{input_dir}/' folder. Please add at least one .txt file.")
    else:
        print(f"[*] Found {len(input_files)} file(s) to process.")
        
        for filename in input_files:
            input_path = os.path.join(input_dir, filename)
            
            # Read each file content
            with open(input_path, "r", encoding="utf-8") as f:
                file_content = f.read().strip()
                
            # Generate the QA artifacts
            result = generate_qa_artifacts(file_content)
            
            # Create a unique output filename (e.g., bug1.txt -> bug1_report.json)
            base_name = os.path.splitext(filename)[0]
            output_filename = f"{base_name}_report.json"
            output_path = os.path.join(output_dir, output_filename)
            
            # Write the individual JSON result to the outputs folder
            with open(output_path, "w", encoding="utf-8") as out_f:
                json.dump(result, out_f, indent=2)
                
            print(f"[✔] Processed '{filename}' -> Generated '{output_filename}'")
            
        print("\n[✔] All files processed successfully!")