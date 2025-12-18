use libc::{size_t, uint8_t};

#[link(name = "sha256_ffi")]
extern "C" {
    fn sha256_hash_message(
        digest: *mut uint8_t,
        dsize: size_t,
        message: *const uint8_t,
        msize: size_t,
    ) -> i32;

    fn sha256_verify_digest(
        digest: *const uint8_t,
        dsize: size_t,
        message: *const uint8_t,
        msize: size_t,
    ) -> i32;
}

pub fn sha256(message: &[u8]) -> Result<[u8; 32], ()> {
    let mut digest = [0u8; 32];
    let rc = unsafe {
        sha256_hash_message(
            digest.as_mut_ptr(),
            digest.len(),
            message.as_ptr(),
            message.len(),
        )
    };
    if rc == 0 { Ok(digest) } else { Err(()) }
}

pub fn verify(message: &[u8], digest: &[u8]) -> bool {
    unsafe {
        sha256_verify_digest(
            digest.as_ptr(),
            digest.len(),
            message.as_ptr(),
            message.len(),
        ) == 0
    }
}
