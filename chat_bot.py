import re
import random

# Responses for different intents
responses = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you.",
        "Hey! What can I do for you?"
    ],

    "name": [
        "I am a Rule-Based Chatbot.",
        "You can call me ChatBot."
    ],

    "help": [
        "Sure! I can help you with greetings, my name, and general questions.",
        "I am here to help. Ask me something!"
    ],

    "goodbye": [
        "Goodbye! Have a nice day.",
        "Bye! See you soon.",
        "Take care!"
    ]
}

# Keyword mapping
patterns = {
    "greeting": [
        r"\bhello\b",
        r"\bhi\b",
        r"\bhey\b",
        r"\bgood morning\b",
        r"\bgood evening\b"
    ],

    "name": [
        r"\bwho are you\b",
        r"\byour name\b",
        r"\bwhat are you\b"
    ],

    "help": [
        r"\bhelp\b",
        r"\bcan you help\b",
        r"\bwhat can you do\b"
    ],

    "goodbye": [
        r"\bbye\b",
        r"\bgoodbye\b",
        r"\bsee you\b",
        r"\bexit\b",
        r"\bquit\b"
    ]
}


def get_intent(user_input):
    """Recognize user's intent using keyword/pattern matching."""

    user_input = user_input.lower().strip()

    for intent, pattern_list in patterns.items():
        for pattern in pattern_list:
            if re.search(pattern, user_input):
                return intent

    return "fallback"


def chatbot():
    print("       RULE-BASED CHATBOT")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        intent = get_intent(user_input)

        if intent == "fallback":
            print("Bot: Sorry, I don't understand that. "
                  "Can you ask something else?")
        else:
            reply = random.choice(responses[intent])
            print("Bot:", reply)

            if intent == "goodbye":
                break


# Start chatbot
if __name__ == "__main__":
    chatbot()