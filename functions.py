


def hello_world():
    return "Hello World"

def plus_number(x,y):
    return x+y

def find_total_json(req):
    #dict = {"id":"string", "name": "string", "price": int, "quantity": int  }
    return { 'total_price': req["price"] * req["quantity"] }