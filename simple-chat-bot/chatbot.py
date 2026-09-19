def chatbot():
    print("Simple Chatbot")
    print("Type 'quit' or 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower().strip()

        if "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Bot: I'm a simple rule-based chatbot.")

        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day!")

        elif user_input == "quit" or user_input == "exit":
            print("Bot: Goodbye! Chat ended.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()