from ctypes import cdll, c_uint8, c_size_t, POINTER

lib = cdll.LoadLibrary("./libsha256_ffi.so")

lib.sha256_hash_message.argtypes = [
    POINTER(c_uint8), c_size_t,
    POINTER(c_uint8), c_size_t
]
lib.sha256_hash_message.restype = int

def sha256(data: bytes) -> bytes:
    digest = (c_uint8 * 32)()
    rc = lib.sha256_hash_message(
        digest, 32,
        (c_uint8 * len(data))(*data), len(data)
    )
    if rc != 0:
        raise RuntimeError("hash failed")
    return bytes(digest)
