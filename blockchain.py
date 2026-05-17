from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_record(self, student_data):
        previous_hash = self.get_last_block().hash
        new_block = Block(len(self.chain), student_data, previous_hash)
        self.chain.append(new_block)
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

    def display_chain(self):
        for block in self.chain:
            print(f"\n--- Block {block.index} ---")
            print(f"Timestamp     : {block.timestamp}")
            print(f"Data          : {block.student_data}")
            print(f"Hash          : {block.hash}")
            print(f"Previous Hash : {block.previous_hash}")