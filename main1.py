import json
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        return {}

def initialize_model():
    try:
        model = OllamaLLM(model="llama3", format="json")
        return model
    except Exception as e:
        print(f"Error initializing the model: {e}")
        return None

template = """
Answer the question based on the provided knowledge base.
If the question cannot be answered using the knowledge base, reply with "I don't have an answer for that."

Here is the knowledge base:
{knowledge_base}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

def handle_conversation(model, data):
    knowledge_base = "\n".join([f"{key}: {value}" for key, value in data.items()])
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        try:
            formatted_prompt = prompt.format_prompt(knowledge_base=knowledge_base, question=user_input)
            response = model.invoke(formatted_prompt.to_string())
            try:
                parsed_response = json.loads(response)
                bot_response = parsed_response.get("answer", "I didn't understand that.")
            except json.JSONDecodeError:
                bot_response = "I couldn't process the response."
            print("Bot:", bot_response)
        except Exception as e:
            print(f"Error during conversation: {e}")

if __name__ == "__main__":
    file_path = "input_data.json"
    data = load_data(file_path)
    model = initialize_model()
    if data and model:
        handle_conversation(model, data)
    else:
        print("Chatbot initialization failed.")