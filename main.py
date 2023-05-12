questions_answers={
    "Hi":"Hey",
    "How Are You":"I am Good",
    "How Old Are You":"I am 1 day old",
    "What Is The Height of Mount Everest":"8848m"
}
while True:
    question=input("You: ")
    question=question.title()
    if question=="Quit":
        print("----------------")
        print("Thanks for Using")
        print("----------------")
        break
    else:
        if question in questions_answers.keys():
            print(f"Bot: {questions_answers.get(question)}")
        else:
            print("Bot: Sorry i have no idea about that")