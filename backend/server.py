from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import products_dao
import uom_dao
import orders_dao
import json

# Initialize SQL connection
connection = get_sql_connection()

# Initialize Flask app
app = Flask(__name__)

# Endpoint to get all products
@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        products = products_dao.get_all_products(connection)
        response = jsonify(products)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all units of measurement (UOM)
@app.route('/getUOM', methods=['GET'])
def get_uom():
    try:
        response = uom_dao.get_uom(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to insert a new product
@app.route('/insertProduct', methods=['POST'])
def insert_product():
    try:
        request_payload = json.loads(request.form['data'])
        product_id = products_dao.insert_new_product(connection, request_payload)
        response = jsonify({'product_id': product_id})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to insert a new order
@app.route('/insertOrder', methods=['POST'])
def insert_order():
    try:
        request_payload = json.loads(request.form['data'])
        order_id = orders_dao.insert_order(connection, request_payload)  # Corrected to use orders_dao
        response = jsonify({'order_id': order_id})  # Corrected key to 'order_id'
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a product
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        return_id = products_dao.delete_product(connection, request.form['product_id'])
        response = jsonify({'product_id': return_id})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the Flask application
if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery")
    app.run(port=5000)
