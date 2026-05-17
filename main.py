from blockchain import Blockchain

def test_blockchain():
    print("=" * 50)
    print("  Blockchain Student Records - System Test")
    print("=" * 50)

    # Initialize blockchain
    student_chain = Blockchain()

    # Test 1: Adding records
    print("\n[TEST 1] Adding student records...")
    student_chain.add_record({"name": "Ali Hassan", "student_id": "CS-101", "grade": "A", "marks": 92})
    student_chain.add_record({"name": "Sara Ahmed", "student_id": "CS-102", "grade": "B+", "marks": 85})
    student_chain.add_record({"name": "Umar Farooq", "student_id": "CS-103", "grade": "A+", "marks": 97})
    print("All records added successfully.")

    # Test 2: Chain validity
    print("\n[TEST 2] Validating blockchain integrity...")
    student_chain.is_chain_valid()

    # Test 3: Hash linking
    print("\n[TEST 3] Checking hash links between blocks...")
    all_linked = True
    for i in range(1, len(student_chain.chain)):
        current = student_chain.chain[i]
        previous = student_chain.chain[i - 1]
        if current.previous_hash != previous.hash:
            print(f"❌ Block {i} is not linked correctly!")
            all_linked = False
    if all_linked:
        print("✅ All blocks are correctly linked.")

    # Test 4: Tamper detection
    print("\n[TEST 4] Simulating tamper attack on Block 1...")
    student_chain.chain[1].student_data["marks"] = 99
    student_chain.chain[1].student_data["grade"] = "A+"
    print("Tampered with Ali Hassan's record...")
    student_chain.is_chain_valid()

    print("\n" + "=" * 50)
    print("  Test Complete — Run app.py for the web interface")
    print("=" * 50)

if __name__ == "__main__":
    test_blockchain()