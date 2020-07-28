from flask import Flask, jsonify, request
from flask_cors import cross_origin, CORS
from rpn_calculator_core.rpn_calculator import Calculator


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'content-type'
cors = CORS(app)
calculator = Calculator()


@app.route('/rpn/stack', methods=['GET'])
@cross_origin()
def get_stack():
    return return_stack()


def return_stack():
    return jsonify(calculator.serialize())


@app.route('/rpn/stack', methods=['POST'])
@cross_origin()
def push():
    calculator.push(request.data.decode("utf-8"))
    return return_stack()


@app.route('/rpn/stack/execute')
@cross_origin()
def execute_stack():
    calculator.execute()
    return return_stack()


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
