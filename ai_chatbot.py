import string


def sanitize(text):
    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


print("Welcome to DecodeLabs AI Chatbot!")
print("Type 'help' to see what I can answer.")
print("Type 'exit' to stop the chatbot.\n")

responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "good morning": "Good morining! Hope you have a great day.",
    "how are you": "I'm just a program, but I'm working perfectly!",
    "what is ai": "AI means Artificial Intelligence. It allows machines to simulate human thinking.",
    "what is python": "Python is a beginner-friendly programming language used in AI, data analysis, and web development.",
    "who are you": "I am a simple rule-based AI chatbot created for DecodeLab Project 1.",
    "what can you do": "I can answer predefined questions using rules and a dictionary.",
    "thank you": "You're welcome!",
    "help": "You can try: hello, how are you, what is ai, what is python, who are you, what can you do, thank you, bye"
}

exit_commands = ["bye", "exit", "quit"]

while True:
    user_input = input("You: ")
    clean_input = sanitize(user_input)

    if clean_input in exit_commands:
        print("Goodbye! Have a nice day.")
        break

    reply = responses.get(
        clean_input, "Sorry, I don't understand that, Try typing 'help'.")
    print("Bot:", reply)
