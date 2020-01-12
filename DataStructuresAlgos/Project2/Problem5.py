import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)


    def calc_hash(self, raw_data):

        sha = hashlib.sha256()
        try:
            hash_str = raw_data.encode('utf-8') # Try to encode data as UTF-8
        except:
            raise ValueError("Data must be a string.")

        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_block(self, data):
        
        if self.head is None:
            # Chain is empty, add new block as head and tail
            timestamp = datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
            self.head = Block(timestamp, data, 0)
            self.tail = Block(timestamp, data, 0)
            self.length += 1
        else:
            # Chain has at least 1 block. 
            # 1. Create new block
            # 2. Reference previous tail next hash to new block hash
            # 3. Make new block tail
            new_block = Block(timestamp, data, self.tail.hash)
            self.tail = new_block
            self.length += 1

    def find_block_by_hash(self, data):

        if self.head is None:
            # Check for empty blockchain
            print("Empty blockchain")
        else:
            block = self.head
            while block.tail:
                if block.data == data:
                    # Block data match
                    print(f"Data '{data}' found in block chain")
                    return block
                block = block.next_hash




	

# b1 = Block(20200111, "Hello", None)
Blockchain = Blockchain()

Blockchain.add_block("Hello")
Blockchain.add_block("Hello")
print(Blockchain.length)
print(Blockchain.tail.data)
print(Blockchain.tail.hash)

print(datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"))