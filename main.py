from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# Define the template
template = """
Answer the question below:

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the model
try:
    model = OllamaLLM(model="llama3", format="json")  # Explicitly set format
except Exception as e:
    print(f"Error initializing the model: {e}")
    exit()

# Create the prompt
prompt = ChatPromptTemplate.from_template(template)

# Chain components
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        # Run the chain and handle output
        try:
            response = chain.invoke({"context": context, "question": user_input})
            if isinstance(response, dict) and "Answer" in response:
                bot_response = response["Answer"]
            else:
                bot_response = response if isinstance(response, str) else "I didn't understand that."

            print("Bot: ", bot_response)
            context += f"\nUser: {user_input}\nAI: {bot_response}"
        except Exception as e:
            print(f"Error invoking the chain: {e}")

if __name__ == "__main__":
    handle_conversation()