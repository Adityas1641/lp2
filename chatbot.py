# Define a dictionary of responses
responses = {
    "hello": "Hi there!",
    "how are you": "I'm good, thank you!",
    "goodbye": "Goodbye! Have a great day!",
    "default": "I'm not sure I understand."
}

# Function to respond to user input
def respond(input_text):
    input_text = input_text.lower()
    if input_text in responses:
        return responses[input_text]
    else:
        return responses["default"]

# Main loop for chatting
print("Welcome to Elementary Chatbot!")
print("You can start chatting. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye! Have a great day!")
        break
    response = respond(user_input)
    print("Bot:", response)