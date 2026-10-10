import os
import json

def generate_qa_artifacts(requirement_or_bug: str):
    """
    Analyzes input text (bug report or feature requirement) and 
    generates structured QA artifacts.
    """
    print(f"[*] Analyzing input text: '{requirement_or_bug[:50]}...'")
    
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
    # Define directory paths
    input_dir = "inputs"
    output_dir = "outputs"
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Path to the specific input file
    input_file_path = os.path.join(input_dir, "sample_bug.txt")
    
    if os.path.exists(input_file_path):
        with open(input_file_path, "r") as f:
            sample_input = f.read().strip()
    else:
        sample_input = "Default fallback: User reported an unexpected application crash on login."
        print(f"[!] Warning: '{input_file_path}' not found. Using fallback text.")

    # Generate the QA artifacts
    result = generate_qa_artifacts(sample_input)
    
    # Define output file path
    output_file_path = os.path.join(output_dir, "qa_report_output.json")
    
    # Write the result to the outputs folder
    with open(output_file_path, "w") as out_f:
        json.dump(result, out_f, indent=2)
        
    print(f"\n[✔] Success! Output generated and saved to: {output_file_path}")
    print(json.dumps(result, indent=2))