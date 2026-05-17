from flask import Flask, request, jsonify
from blockchain import Blockchain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

student_chain = Blockchain()

@app.route("/add", methods=["POST"])
def add_record():
    data = request.json
    student_chain.add_record({
        "name": data["name"],
        "student_id": data["student_id"],
        "grade": data["grade"],
        "marks": data["marks"]
    })
    return jsonify({"message": f"Record added for {data['name']}"}), 200

@app.route("/chain", methods=["GET"])
def get_chain():
    chain_data = []
    for block in student_chain.chain:
        chain_data.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.student_data,
            "hash": block.hash,
            "previous_hash": block.previous_hash
        })
    return jsonify(chain_data), 200

@app.route("/validate", methods=["GET"])
def validate():
    is_valid = student_chain.is_chain_valid()
    return jsonify({"valid": is_valid}), 200

@app.route("/tamper/<int:block_index>", methods=["POST"])
def tamper(block_index):
    data = request.json
    if block_index < len(student_chain.chain):
        student_chain.chain[block_index].student_data = data
        return jsonify({"message": f"Block {block_index} tampered!"}), 200
    return jsonify({"message": "Block not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)