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
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))

    class Inputs(Enum):
        addition = 1
        subtraction = 2
        multiplication = 3
    key_words = ['add', 'subtract', 'multiply']
    operator_list = ['+', '-', 'x']

    if user_input not in set(item.value for item in Inputs):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=user_input,
            max_tokens=8,
            temperature=0
        )
        data = response['choices'][0]['text']
        for operator in operator_list:
            if operator in data:
                operation = Inputs(operator_list.index(operator) + 1).name
        for word in key_words:
            if word in user_input:
                operation = Inputs(key_words.index(word) + 1).name
                break
        answer = int(data.split(' ')[-1].strip('.'))
    else:
        operation = user_input
        if operation == Inputs.addition:
            answer = x + y
        elif operation == Inputs.subtraction:
            answer = x - y
        elif operation == Inputs.multiplication:
            answer = x * y
    return jsonify(slackUsername='Fola27', result=answer, operation_type=operation)


if __name__ == '__main__':
    app.run(debug=True)





