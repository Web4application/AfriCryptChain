const ffi = require("ffi-napi");
const ref = require("ref-napi");

const uint8 = ref.types.uint8;
const uint8Ptr = ref.refType(uint8);

const lib = ffi.Library("./libsha256_ffi", {
  sha256_hash_message: [
    "int",
    [uint8Ptr, "size_t", uint8Ptr, "size_t"]
  ]
});

function sha256(buffer) {
  const digest = Buffer.alloc(32);
  const rc = lib.sha256_hash_message(
    digest, 32,
    buffer, buffer.length
  );
  if (rc !== 0) throw new Error("hash failed");
  return digest;
}
