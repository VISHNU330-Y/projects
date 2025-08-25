import random
import urllib.request
import json
def generate_math_question():
    operators = ["+", "-", "*", "/"]
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operators)

    
    if op == "/":
        num1 = num1 * num2  

    question = f"What is {num1} {op} {num2}?"
    answer = str(eval(f"{num1}{op}{num2}"))

    return {"question": question, "options": [], "answer": answer}


def fetch_trivia_questions(amount=3):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    questions = []
    for item in data["results"]:
        options = item["incorrect_answers"] + [item["correct_answer"]]
        random.shuffle(options)
        questions.append({
            "question": item["question"],
            "options": options,
            "answer": item["correct_answer"]
        })
    return questions

# Quiz Game
def quiz_game():
    score = 0

    all_questions = [generate_math_question() for _ in range(3)] + fetch_trivia_questions(3)
    random.shuffle(all_questions)

    for i, q in enumerate(all_questions, 1):
        print(f"\nQ{i}: {q['question']}")
        
        if q["options"]:  # Trivia question
            for idx, option in enumerate(q["options"], 1):
                print(f"  {idx}. {option}")
            answer = input("Your answer (choose number): ")
            if q["options"][int(answer)-1] == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct Answer: {q['answer']}")
        else:  # Math question
            answer = input("Your answer: ")
            if answer.strip() == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct Answer: {q['answer']}")

    print(f"\n🎯 Final Score: {score}/{len(all_questions)}")


quiz_game()
