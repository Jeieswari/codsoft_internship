import re

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello there! How can I help you?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing fine! How about you?")
        elif 'your name' in user_input:
            print("Chatbot: I'm ChatBot-101, your virtual assistant.")
        elif 'help' in user_input:
            print("Chatbot: I can answer simple questions like greetings, name, and mood. Try asking!")
        elif 'bye' in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        elif re.search(r'weather|temperature', user_input):
            print("Chatbot: I can't check real-time weather, but it’s always sunny in the console!")
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else!")


chatbot()
