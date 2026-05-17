import hashlib
import datetime

class Block:
    def __init__(self, index, student_data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.student_data = student_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = (
            str(self.index) +
            self.timestamp +
            str(self.student_data) +
            self.previous_hash
        )
        return hashlib.sha256(block_content.encode()).hexdigest()