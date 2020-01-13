import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.next_block = None
        self.hash = self.calc_hash(data)


    def calc_hash(self, raw_data):

        sha = hashlib.sha256()
        if isinstance(raw_data, str):
            hash_str = raw_data.encode('utf-8') # Try to encode data as UTF-8
        else:
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
            timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
            new_block = Block(timestamp, data, 0)
            self.head = new_block
            self.tail = new_block
            self.length += 1
        else:
            # Chain has at least 1 block. 
            # 1. Create new block
            # 2. Reference previous tail next hash to new block hash
            # 3. Make new block tail
            timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
            new_block = Block(timestamp, data, self.tail.hash)
            old_tail = self.tail
            old_tail.next_block = new_block
            self.tail = new_block
            self.length += 1

    def find_block_by_hash(self, hash):

        if self.head is None:
            # Check for empty blockchain
            raise ValueError("Empty blockchain")
        else:
            block = self.head
            while block:
                if block.hash == hash:
                    # Block data match
                    print(f"Hash '{hash}' found in block chain")
                    return block
                block = block.next_block
            raise ValueError("Block hash not found in blockchain")

    def __str__(self):

        block = self.head
        n = 1

        s = "<=== Beginning of blockchain ===>\n"
        while block:
            s += f"Block {n}({block.hash}): {block.data}\n"
            block = block.next_block
            n += 1
        s += "<====== End of blockchain ======>"
        
        return s




	

# b1 = Block(20200111, "Hello", None)
Blockchain = Blockchain()

Blockchain.add_block("Hello")
Blockchain.add_block("Goodbye")
print(Blockchain.length)
print(Blockchain.head.data)
print(Blockchain.head.next_block)
print(Blockchain.tail.data)
print(Blockchain.tail.hash)
print(Blockchain.tail.timestamp)
print(Blockchain)