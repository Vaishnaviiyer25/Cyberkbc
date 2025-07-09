# cyberquest.py
# Cybersecurity Learning Game for Class 11-12

score = 0

def ask(question, options, correct):
    global score
    print("\n" + question)
    for key, val in options.items():
        print(f"{key}) {val}")
    answer = input("Your choice (a/b): ").strip().lower()
    if answer == correct:
        print("✅ Correct!\n")
        score += 10
    else:
        print("❌ Incorrect!")
        print(f"The correct answer was: {options[correct]}\n")

def level1():
    ask(
        "Level 1: Strong Passwords\nWhich password is stronger?",
        {'a': 'password123', 'b': '4xM$7RoQ!'},
        'b'
    )

def level2():
    ask(
        "Level 2: Spotting Phishing\nWhich email looks like a phishing attempt?",
        {'a': 'support@amazon.com', 'b': 'amazon.support@freestuff.ru'},
        'b'
    )

def level3():
    ask(
        "Level 3: Avoiding Malware\nWhich should you AVOID clicking?",
        {'a': 'Free Movie Download Link', 'b': 'Update from Official Site'},
        'a'
    )

def level4():
    ask(
        "Level 4: Safe Browsing\nWhich URL is safer to use?",
        {'a': 'http://bank.com', 'b': 'https://bank.com'},
        'b'
    )

def level5():
    ask(
        "Level 5: Cyberbullying\nYour friend is bullied online. What should you do?",
        {'a': 'Ignore it', 'b': 'Report and Support your friend'},
        'b'
    )

def main():
    print("🎮 Welcome to CyberQuest - Learn Cybersecurity while Playing! 🎮")
    print("---------------------------------------------------------------")
    print("Answer by typing 'a' or 'b' and pressing Enter.\n")

    level1()
    level2()
    level3()
    level4()
    level5()

    print("---------------------------------------------------------------")
    print(f"🏆 Your final score: {score} / 50")
    if score == 50:
        print("🎉 Excellent! You're a Cyber Hero! 🎉")
    elif score >= 30:
        print("👍 Good job! You know your cybersecurity basics.")
    else:
        print("🔍 Keep learning! Cyber safety is important for everyone.")
    print("---------------------------------------------------------------")

if __name__ == "__main__":
    main()
