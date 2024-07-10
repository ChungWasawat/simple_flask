from flask import Flask, request, jsonify
import functions




app = Flask('simple_web')

@app.route('/home', methods=['POST'])
def predict_endpoint():
    data = request.get_json()

    result =  functions.find_total_json(data)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)