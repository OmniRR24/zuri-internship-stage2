from flask import Flask, jsonify, request
import os
import openai
from enum import Enum

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calc():
    operation = None
    answer = None
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    user_input = request.args.get('operation_type')
    user_input = str(user_input).lower()
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))

    inputs = ['addition', 'subtraction', 'multiplication']
    key_words = ['add', 'subtract', 'multiply']
    operator_list = ['+', '-', 'x']

    if user_input not in inputs:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=user_input,
            max_tokens=8,
            temperature=0
        )
        data = response['choices'][0]['text']
        for operator in operator_list:
            if operator in data:
                operation = inputs[operator_list.index(operator)]
        for word in key_words:
            if word in user_input:
                operation = inputs[key_words.index(word)]
                break
        answer = int(data.split(' ')[-1].strip('.'))
    else:
        operation = user_input
        if operation == inputs[0]:
            answer = x + y
        elif operation == inputs[1]:
            answer = x - y
        elif operation == inputs[2]:
            answer = x * y
    return jsonify(slackUsername='Fola27', result=answer, operation_type=operation)


if __name__ == '__main__':
    app.run(debug=True)





