import random

# Define the quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["4", "8", "16", "32"],
        "answer": "8"
    },
    {
        "question": "Which country is known for the Eiffel Tower?",
        "options": ["France", "Italy", "Spain", "Germany"],
        "answer": "France"
    },
    {
        "question": "What is the currency used in Japan?",
        "options": ["Dollar", "Euro", "Yen", "Pound"],
        "answer": "Yen"
    }
]

def run_quiz():
    """Runs the quiz and keeps track of the user's score."""
    score = 0
    num_questions = len(quiz_data)

    print("Welcome to the Quiz App!")
    print(f"There are {num_questions} questions in the quiz.")

    for question_data in quiz_data:
        question = question_data["question"]
        options = question_data["options"]
        answer = question_data["answer"]

        print("\n" + question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = input("Enter the number of the correct answer: ")
        if options[int(user_answer) - 1] == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print(f"\nYour final score is {score}/{num_questions}")

if __name__ == "__main__":
    run_quiz()