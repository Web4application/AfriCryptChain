from flask import Flask, request, jsonify

app = Flask(__name__)
blockchain = []

@app.route('/broadcast_block', methods=['POST'])
def receive_block():
    data = request.get_json()
    blockchain.append(data)
    return jsonify({"status": "Block received"}), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain), 200

app.run(host='0.0.0.0', port=5000)
