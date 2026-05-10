# College Inquiry Chatbot

def chatbot():

    print("Chatbot: Welcome to College Inquiry System")
    print("Type 'bye' to exit\n")

    while True:

        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello Student!")

        elif "college" in user:
            print("Bot: PCCOER Ravet Pune.")

        elif "course" in user:
            print("Bot: We offer Engineering courses.")

        elif "fees" in user:
            print("Bot: Please visit college office for fees details.")

        elif "admission" in user:
            print("Bot: Admission process is currently open.")

        elif user == "bye":
            print("Bot: Thank You!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
