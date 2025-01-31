import requests
import html

url = 'https://opentdb.com/api.php?amount=10'
result = requests.get(url).json()

if result['response_code'] == 0:
    questions = result['results']
    for i, question in enumerate(questions, start=1):
        question_text = html.unescape(question['question'])
        correct_answer = html.unescape(question['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in question['incorrect_answers']]
        print(f"Question {i}: {question_text}")
        print("Options:")
        
        options = incorrect_answers + [correct_answer]
        for j, option in enumerate(options, start=1):
            print(f"  {j}. {option}")
        
        print(f"Answer: {correct_answer}")
        print("\n")
else:
    print("Failed to fetch questions.")