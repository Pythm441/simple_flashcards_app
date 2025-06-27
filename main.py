import os
import random

FLASHCARD_FILE = "flashcards.txt"


def add_card():
    question = input("Enter the question: ").strip()
    answer = input("Enter the answer: ").strip()

    if not question or not answer:
        print("Both question and answer are required.")
        return
    elif '|' in question or '|' in answer:
        print("The '|' character is not allowed in questions or answers.")
        return

    with open(FLASHCARD_FILE, "a") as file:
        file.write(f"{question}|{answer}\n")

    print("Flashcard added successfully.")


def load_flashcards():
    if not os.path.exists(FLASHCARD_FILE):
        return []

    with open(FLASHCARD_FILE, "r") as file:
        lines = file.readlines()

    flashcards = []
    for line in lines:
        if '|' in line:
            parts = line.strip().split("|")
            if len(parts) == 2:
                flashcards.append((parts[0], parts[1]))         
    return flashcards


def quiz():
    flashcards = load_flashcards()

    if not flashcards:
        print("No flashcards found. Please add some first.")
        return

    random.shuffle(flashcards)  # Shuffle questions

    score = 0
    for question, answer in flashcards:
        user_answer = input(f"{question}: ").strip()
        if user_answer.lower() == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {answer}")

    print(f"\n📊 Your final score: {score}/{len(flashcards)}")

    if score/len(flashcards) < 0.5:
        print("Review your cards and study well. you'll do better next time")
    else:
        print("Excllent work! No need to review now. Focus on other subjects")    


def main():
    while True:
        print("\n📚 Flashcard Quiz App")
        print("1. Add Flashcard")
        print("2. Take Quiz")
        print("3. Exit")
        choice = input("Choose an option (1–3): ").strip()

        if choice == "1":
            add_card()
        elif choice == "2":
            quiz()
        elif choice == "3":
            print("👋 Exiting the app. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
