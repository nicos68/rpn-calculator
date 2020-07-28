from flask import Flask, jsonify
from rpn_calculator_core.rpn_calculator import Calculator


app = Flask(__name__)
calculator = Calculator()


@app.route('/rpn/stack')
def get_stack():
    return jsonify(calculator.serialize())


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
