
# from datetime import datetime
# print("Hello, I am a chatbot,how can I help you?\n please enter 'help' if you don't know about me\n enter 'bye' to exit")


# def Answer():
#     user_input = input("enter: ")
#     match user_input:
#         case "help":
#             print("I am a chatbot,made by babar mir,\n I can help you with some questions releated babar,time,date")
#         case "hello":
#             print("Hello")
#         case "how are you?":
#             print("I am fine")
#         case "what is your name?":
#             print("I am chatbot, you can call me babarbot")
#         case "what is time?":
#             print(datetime.now().strftime("%H:%M:%S"))
#         case "what is date?":
#             print(f"the date is {datetime.now().strftime('%d-%m-%Y')}")
#         case "what is your favorite color?":
#             print("I don't have a favorite color, I am just a chatbot.")
#         case "bye":
#             print("good bye")
#         case _:
#             print("I don't understand")
#     print("Thank you for using this chatbot")
#     Answer()


# Answer()
from datetime import datetime

print("🤖 Hello! I am BabarBot, your chatbot.")
print("Type 'help' to know what I can do, or 'bye' to exit.\n")


def chatbot():
    while True:
        user_input = input("You: ").lower()

        match user_input:
            case "help":
                print(
                    "Bot: I can answer questions like time, date, my name, how I feel, etc.")
            case "hello":
                print("Bot: Hello there!")
            case "how are you?":
                print("Bot: I'm just a bunch of code, but I'm doing fine!")
            case "what is your name?":
                print("Bot: I am BabarBot, your virtual assistant.")
            case "what is time?":
                print("Bot:", datetime.now().strftime("%H:%M:%S"))
            case "what is date?":
                print("Bot: The date is", datetime.now().strftime("%d-%m-%Y"))
            case "what is your favorite color?":
                print(
                    "Bot: I don't have one, but I like the color of well-written code!")
            case "bye":
                print("Bot: Goodbye! 👋 Thank you for chatting.")
                break
            case _:
                print("Bot: I didn't understand that. Try asking something else.")


chatbot()
