import os
import shutil

def clean_temp_files():
    temp_dirs = [
        os.getenv('TEMP'),
        os.getenv('TMP'),
        os.path.join(os.getenv('SystemRoot'), 'Temp')
    ]

    for temp_dir in temp_dirs:
        if temp_dir and os.path.exists(temp_dir):
            print(f"Cleaning: {temp_dir}")
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                    except Exception as e:
                        print(f"Failed to delete file: {file_path}. Reason: {e}")
                for dir in dirs:
                    try:
                        dir_path = os.path.join(root, dir)
                        shutil.rmtree(dir_path)
                        print(f"Deleted directory: {dir_path}")
                    except Exception as e:
                        print(f"Failed to delete directory: {dir_path}. Reason: {e}")
        else:
            print(f"Temporary directory not found: {temp_dir}")

if __name__ == "__main__":
    clean_temp_files()

    class Block:
        def __init__(self, index, previous_hash, data, timestamp):
            self.index = index
            self.previous_hash = previous_hash
            self.data = data
            self.timestamp = timestamp
            self.hash = self.calculate_hash()

        def calculate_hash(self):
            hash_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
            return hashlib.sha256(hash_string.encode()).hexdigest()


    class Blockchain:
        def __init__(self):
            self.chain = [self.create_genesis_block()]

        def create_genesis_block(self):
            return Block(0, "0", "Genesis Block", time.time())

        def get_latest_block(self):
            return self.chain[-1]

        def add_block(self, data):
            latest_block = self.get_latest_block()
            new_block = Block(len(self.chain), latest_block.hash, data, time.time())
            self.chain.append(new_block)

        def is_chain_valid(self):
            for i in range(1, len(self.chain)):
                current_block = self.chain[i]
                previous_block = self.chain[i - 1]

                if current_block.hash != current_block.calculate_hash():
                    return False
                if current_block.previous_hash != previous_block.hash:
                    return False
            return True


    if __name__ == "__main__":
        blockchain = Blockchain()
        blockchain.add_block("First Block")
        blockchain.add_block("Second Block")

        for block in blockchain.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Data: {block.data}")
            print(f"Timestamp: {block.timestamp}")
            print("-" * 30)

        print("Is blockchain valid?", blockchain.is_chain_valid())

        