import hashlib
import time
import json

class GenesisBlock:
    def __init__(self):
        self.index = 0
        self.timestamp = time.time()
        self.data = {
            "chain_name": "AfriCryptChain",
            "creator": "kubu",
            "message": "Powering Crypto Innovation Across the Continent",
            "initial_supply": 100000000,  # total AFCT tokens
            "genesis_address": "AFCT1KUBU00000000000000000000"
        }
        self.previous_hash = "0" * 64
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

genesis = GenesisBlock()
print("🔓 AfriCryptChain Genesis Block Created:")
print(f"Hash: {genesis.hash}")
print(f"Block Data: {genesis.data}")
