from block import Block
import json
import os

class Blockchain:
    def __init__(self):
        self.chain = []
        self.file = "chain_data.json"
        self.load_chain()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)
        self.save_chain()

    def get_last_block(self):
        return self.chain[-1]

    def add_record(self, student_data):
        previous_hash = self.get_last_block().hash
        new_block = Block(len(self.chain), student_data, previous_hash)
        self.chain.append(new_block)
        self.save_chain()
        print(f"✅ Record added for: {student_data['name']}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print(f"❌ Block {i} has been tampered with!")
                return False

            if current.previous_hash != previous.hash:
                print(f"❌ Block {i} is disconnected from the chain!")
                return False

        print("✅ Blockchain is valid. All records are secure.")
        return True

    def save_chain(self):
        data = []
        for block in self.chain:
            data.append({
                "index": block.index,
                "timestamp": block.timestamp,
                "student_data": block.student_data,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            })
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def load_chain(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                data = json.load(f)
            for item in data:
                block = Block(
                    item["index"],
                    item["student_data"],
                    item["previous_hash"]
                )
                block.timestamp = item["timestamp"]
                block.hash = item["hash"]
                self.chain.append(block)
            print("✅ Chain loaded from file.")
        else:
            self.create_genesis_block()
            print("✅ New blockchain created.")