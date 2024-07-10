import flask_app

def test_find_total():
    test_data = {
    "id":"xyz", 
    "name": "air conditionar", 
    "price": 30050, 
    "quantity": 4  }

    actual_result = flask_app.find_total_json(test_data)
    expected_result = {
        'total_price': 120200
    }

    assert actual_result == expected_result