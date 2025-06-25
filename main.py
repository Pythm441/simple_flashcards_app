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
