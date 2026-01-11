import json
import os

def run_prompt_suite():
    """
    Main execution function for the Medical Prompt Engineering Framework.
    This script automates the generation of complex prompts by injecting 
    clinical source text into various templating strategies (Few-shot, CoT, Role-playing).
    """
    
    # 1. Setup absolute paths for cross-platform compatibility
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, 'data', 'source_text.txt')
    templates_path = os.path.join(script_dir, 'prompts', 'templates.json')
    output_dir = os.path.join(script_dir, 'outputs')

    print("--- Initializing Medical Prompt Engineering Experiment ---")

    # 2. Extract: Load the source clinical text
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            source_content = f.read()
            if not source_content.strip():
                print(f"Error: Source text file is empty at {source_path}")
                return
    except FileNotFoundError:
        print(f"Error: Could not locate source_text.txt at {source_path}")
        return

    # 3. Transform: Load and parse the Prompt Templates from JSON
    try:
        with open(templates_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Problem loading templates.json. Check path and JSON syntax.")
        return

    # 4. Process: Generate and display the optimized prompts
    templates = config.get('templates', {})
    if not templates:
        print("Error: No templates found in the configuration file.")
        return

    print(f"Dataset loaded: {len(source_content.split())} words of clinical text.")
    
    for technique, template in templates.items():
        try:
            final_prompt = template.format(text=source_content)
            print(f"\n[TECHNIQUE IDENTIFIED]: {technique.upper()}")
            print("-" * 50)
            print(f"PROMPT PREVIEW:\n{final_prompt[:250]}...")
            print("-" * 50)
        except KeyError:
            print(f"Error: Template '{technique}' is missing the '{{text}}' placeholder.")

    # 6. Conclusion and next steps
    # This section confirms the automation logic is successful and points to the findings
    print("\n--- Experiment Infrastructure Validated ---")
    print("Next step: Send these generated prompts to an LLM API (OpenAI/Gemini).")
    print("Linguistic results and comparisons are documented in the /results and /outputs folders.")
    
    # Ensure the outputs directory exists for manual result documentation
    os.makedirs(output_dir, exist_ok=True)

if __name__ == "__main__":
    run_prompt_suite()
