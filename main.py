def add_card():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    with open("flashcards.json", "a") as file:
        file.write(f"{question}|{answer}\n")
    print("Flashcard added successfully.")


def quiz():
    try:
        with open("flashcards.json", "r") as file:
            flashcards = [line.strip().split("|") for line in file.readlines()]
    except FileNotFoundError:
        print("No flashcards found. Please add some first.")
        return

    score = 0
    for question, answer in flashcards:
        user_answer = input(f"{question} ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"Your score: {score}/{len(flashcards)}")
def main():
    while True:
        print("\nFlashcard Quiz App")
        print("1. Add Flashcard")
        print("2. Take Quiz")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_card()
        elif choice == "2":
            quiz()
        elif choice == "3":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This is a simple flashcard quiz app that allows users to add flashcards and take quizzes
# It stores flashcards in a text file and reads them for quizzes
# The app provides a menu for users to choose actions
# It handles basic file operations and user input
# The flashcards are stored in a simple format: question|answer
# The app can be extended with more features like editing or deleting flashcards
# It is a console-based application and can be run in any Python environment
# The app is designed to be user-friendly and straightforward
# It can be used for studying various subjects by creating relevant flashcards
# The app can be improved with error handling and data validation
# It can also be enhanced with a graphical user interface in the future
# The app is a good starting point for learning about file handling and user interaction in Python