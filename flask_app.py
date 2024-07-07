from flask import Flask, request, jsonify


def hello_world():
    return "Hello World"

def plus_number(x,y):
    return x+y

def convert_value_json(req):
    #dict = {"id":"string", "name": "string", "price": int, "quantity": int  }
    return req["price"] * req["quantity"]


app = Flask('simple_web')

@app.route('/home', methods=['POST'])
def predict_endpoint():
    data = request.get_json()

    result = {
        'total_price': convert_value_json(data)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)