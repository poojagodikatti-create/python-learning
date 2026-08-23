print("🧠 PYTHON QUIZ GAME 🧠")
print("=" * 35)

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["A. display()", "B. print()", "C. show()", "D. output()"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. List"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for exponentiation?",
        "options": ["A. ^", "B. //", "C. **", "D. %%"],
        "answer": "C"
    }
]

score = 0

for number, quiz in enumerate(questions, start=1):

    print(f"\nQuestion {number}: {quiz['question']}")

    for option in quiz["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == quiz["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct answer:", quiz["answer"])

percentage = (score / len(questions)) * 100

print("\n" + "=" * 35)
print("🏆 QUIZ COMPLETED!")
print("Score:", score, "/", len(questions))
print("Percentage:", percentage, "%")

if percentage == 100:
    print("🔥 PERFECT SCORE!")
elif percentage >= 60:
    print("🎉 Great job!")
else:
    print("📚 Keep learning and try again!")