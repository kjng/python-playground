from flask import Flask, jsonify, request

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
  request_data = request.get_json()
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)

# GET - return a store's details
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify(store)
  return jsonify({ 'message': 'Store not found.' })

# GET - return all stores
@app.route('/store')
def get_stores():
  return jsonify({ 'store': stores })

# POST - add an item to a store
@app.route('/store/<string:name>/item', methods=['POST'])
def add_item_to_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
      new_item = {
        'name': request_data['name'],
        'price': request_data['price']
      }
      store['items'].append(new_item)
      return jsonify(new_item)
  return jsonify({ 'message': 'Store not found.' })

# GET - get items from store
@app.route('/store/<string:name>/item')
def get_items_from_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify({ 'items': store['items'] })
  return jsonify({ 'message': 'Store not found.' })

if __name__ == '__main__':
  app.run(port=5000)
