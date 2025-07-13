

print("Hello, I am a chatbot,how can I help you?\n please enter 'help' if you don't know about me\n enter 'bye' to exit")


def Answer():
    user_input = input("enter: ")
    match user_input:
        case "help":
            print("I am a chatbot,made by babar mir,\n I can help you with some questions releated babar,time,date")
        case "hello":
            print("Hello")
        case "how are you?":
            print("I am fine")
        case "what is your name?":
            print("I am chatbot, you can call me babarbot")
        case "bye":
            print("bye")
        case _:
            print("I don't understand")
    print("Thank you for using this chatbot")
    Answer()


Answer()
