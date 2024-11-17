from flask import Flask, render_template, request, redirect

app = Flask(__name__)

quiz_data = [
    {'question': 'Яку мову програмування ти використовуєш', 'options': ['Python', 'C++', 'Java', 'JavaScript']},
    {'question': 'Який веб фреймворт ти використовуєш', 'options': ['Flask', 'Django', 'FastAPI', 'Spring']}
    # {'question': ''}
]
current_quiz_index = 0
user_answer = []

@app.route('/', methods=['GET', 'POST'])
def quiz():
    global current_quiz_index, user_answer
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer:
            user_answer.append(answer)
            current_quiz_index += 1
            if current_quiz_index >= len(quiz_data):
                with open('data.txt', 'a', encoding='utf-8') as f:
                    for i, ans in enumerate(user_answer):
                        f.write(f"Питання_{i+1}: {quiz_data[i]['question']}\n")
                        f.write(f"Відповідь: {ans}\n\n")
                current_quiz_index = 0
                user_answer = []
                return redirect('end')
    question = quiz_data[current_quiz_index]
    return render_template('quiz.html', question=question, index=current_quiz_index+1, total=len(quiz_data))


@app.route('/end')
def end():
    return render_template('end.html')

if __name__ == '__main__':
    app.run(debug=True)
