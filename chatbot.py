print("🤖 Simple Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! 😊")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks! 💙")

    elif user_input == "what is your name":
        print("Bot: I'm a Python chatbot 🤖")

    elif user_input == "bye":
        print("Bot: Goodbye! 👋")
        break

    elif user_input == "thank you":
        print("Bot: You're welcome 😊")

    else:
        print("Bot: Sorry, I don't understand that.")
