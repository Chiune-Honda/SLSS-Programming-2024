# Loops Example

def validate_answers(question: str, usr_answer: str) -> bool:
    """takes a question and returns true if it's correct, false if it's wrong"""
    questions = [
        "What colour is the sky?",
        "What colour is the ocean?",
        "What's 1+1?"
    ]

    answers = [
        "blue",
        "blue",
        "2"
    ]

    # Find the location of the question in the questions list
    location = questions.index(question)

    # if the usr_answer matches the answer from the key, return true
    if answers[location] == usr_answer:
        return True
    else:
        return False


questions = [
    "What colour is the sky?",
    "What colour is the ocean?",
    "What's 1+1?"
]

print("I'll ask you some questions:")

for question in questions:
    print(question)

    user_answer = input()

    if validate_answers(question, user_answer):
        print("You got it right!")
    else:
        print("Sorry, not this time.")