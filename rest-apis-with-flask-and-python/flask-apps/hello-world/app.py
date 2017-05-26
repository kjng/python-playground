from flask import Flask, jsonify

app = Flask(__name__)

stores = [
  {
    'name': 'My First Store',
    'items': [
      {
        'name': 'First item',
        'price': 19.99
      }
    ]
  }
]

# POST - create a store
@app.route('/store', methods=['POST'])
def create_store():
  pass

# GET - return a store's details
@app.route('/store/<string:name>')
def get_store(name):
  pass

# GET - return all stores
@app.route('/store')
def get_stores():
  return jsonify({ 'store': stores })

# POST - add an item to a store
@app.route('/store/<string:name>/item', methods=['POST'])
def add_item_to_store(name):
  pass

# GET - get items from store
@app.route('/store/<string:name>/item')
def get_items_from_store(name):
  pass

if __name__ == '__main__':
  app.run(port=5000)
