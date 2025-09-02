def chatbot():
    print("Chatbot: Hello! I can talk to you. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "whats your name":
            print("Chatbot: My name is Mas.")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I don't understand that.This was no under my scope")


# Start the chatbot

chatbot()
