import ollama # type: ignore

PROMPT = """
ONLY Generate an ideal Dockerfile for {language} with best practices. Do not provide any description
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    # Try common model names - will use first available
    models_to_try = ['llama3.2:3b', 'llama3.2', 'llama3.1', 'llama3', 'llama2', 'mistral', 'phi']
    
    for model in models_to_try:
        try:
            response = ollama.chat(model=model, messages=[{'role': 'user', 'content': PROMPT.format(language=language)}])
            print(f"Using model: {model}")
            return response['message']['content']
        except ollama._types.ResponseError:
            continue
    
    # If no models found, raise error with helpful message
    raise Exception("No compatible models found. Run 'ollama list' to see available models or 'ollama pull llama3.2:3b' to download one.")

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)