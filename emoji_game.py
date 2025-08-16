import random
emojis = [
    {"emoji": " ⚡️ 👨 🔨", "answer": "thor",
        "hint": "A Marvel superhero who wields a hammer."},
    {"emoji": "🛳️ 🧊", "answer": "titanic", "hint": "A famous ship that sank."},
    {"emoji": "🕸️ 👨", "answer": "spider man",
        "hint": "A superhero who climbs walls."},
    {"emoji": "🐀 🍝", "answer": "ratatouille",
        "hint": "A movie about a rat who cooks."},
    {"emoji": "🤖 🚗", "answer": "transformers",
        "hint": "A movie about robots that transform into vehicles."},
    {"emoji": "👻 🚫", "answer": "ghost busters",
        "hint": "A movie about a team of ghost hunters."},
    {"emoji": "🐠 🔍", "answer": "finding nemo",
        "hint": "A movie about a fish searching for his son."},
    {"emoji": "🦕 🏞️", "answer": "jurassic park",
        "hint": "A movie about dinosaurs in a theme park."},
    {"emoji": "🦁 👑", "answer": "lion king",
        "hint": "A movie about a lion cub's journey to adulthood."},
    {"emoji": "🎈 🏠", "answer": "up",
        "hint": "A movie about a man who fulfills his dream of adventure."},
    {"emoji": "😴 👸", "answer": "sleeping beauty",
        "hint": "A classic fairy tale about a princess."},
    {"emoji": "🔪 🏃", "answer": "blade runner",
        "hint": "A movie about a dystopian future with bioengineered beings."},
    {"emoji": "🟩 😡", "answer": "hulk",
        "hint": "A movie about a man who transforms into a giant green creature."},
    {"emoji": "🌪️ 🏠", "answer": "wizard of oz",
        "hint": "A movie about a girl who is swept away to a magical land."},
    {"emoji": "🐼 🥋", "answer": "kung fu panda",
        "hint": "A movie about a clumsy panda who becomes a kung fu hero."}
]


def intro(total):
    print("=" * 60)
    print("🍿Welcome to the Emoji Movie Game🍿".center(60))
    print("=" * 60)
    print("\nHow to Play:")
    print("You will be shown an emoji representation of a movie title.")
    print("If you guess correctly, you will earn a point.")
    print("If you're stuck, type 'hint' for a clue.")
    print("If you don't know the answer, type 'idk' to skip or 'exit' to leave the game")
    print("If you guess correctly after a hint it is half a point")
    print("You will have {} questions to answer.".format(total))
    print("Good Luck! 😉")
    print("-------------------------------------------------------------\n")


def ask(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Please answer with 'yes' or 'no'.")


def print_results(results):
    print("\n-------------------------------------------------------------")
    print("📈Score Breakdown📉")
    for r in results:
        emoji = r["emoji"]
        result = r["result"]
        answer = r["answer"]
        if result == "correct":
            status = "✅ Correct"
        elif result == "hint":
            status = "📝 Guessed with hint"
        else:
            status = "❌ Skipped"
        print("{} - {} - Answer: {}".format(emoji, status, answer))
    print("-------------------------------------------------------------")


def print_score(score, total):
    print("=" * 60)
    print("🏁Game Over! Your final score is {}/{}".format(score, total))
    perc = round(score / total * 100)
    print("📊Your accuracy was: {}%".format(perc))
    print("=" * 60)


def play(i, score, total):
    hint_used = False
    while True:
        print(i["emoji"])
        user = input(
            "What movie is this? (do not use 'the')\n").strip().lower()
        if user.replace(" ", "") == i["answer"].replace(" ", ""):
            if hint_used:
                score += 0.5
                print(
                    "🎉You guessed it with a hint! Your score is {}/{}\n".format(score, total))
                return score, {"emoji": i["emoji"], "result": "hint", "answer": i["answer"]}
            else:
                score += 1
                print("🎊You're right! Your score is {}/{}\n".format(score, total))
                return score, {"emoji": i["emoji"], "result": "correct", "answer": i["answer"]}
        elif user == "idk":
            print(
                "❌The answer is: {}. Your score is {}/{}\n".format(i["answer"], score, total))
            return score, {"emoji": i["emoji"], "result": "skipped", "answer": i["answer"]}
        elif user == "hint":
            print("Hint: {}".format(i["hint"]))
            hint_used = True
        elif user == "exit":
            raise KeyboardInterrupt
        else:
            print("☹️ Incorrect try again")
            print("If you want a hint type 'hint'")
            print("If you want to skip this question type 'idk'\n")


def game():
    total = len(emojis)
    while True:
        try:
            num_emojis = int(input(
                "How many emojis do you want to guess? maximum number is {}:\n".format(total)))
            select = random.sample(emojis, num_emojis)
            if 1 <= num_emojis <= total:
                return select
            else:
                print("Please enter a number between 1 and {}".format(total))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        score = 0
        intro(len(emojis))
        select = game()
        results = []
        try:
            for i in select:
                score, result = play(i, score, len(select))
                results.append(result)
        except KeyboardInterrupt:
            print("\nExiting the game!")
            break

        print_score(score, len(select))

        if ask("\nDo you want to see your score breakdown? (yes/no)\n"):
            print_results(results)

        if not ask("\nDo you want to play again? (yes/no)\n"):
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
