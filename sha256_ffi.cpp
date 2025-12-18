// sha256_ffi.cpp
#include "cryptlib.h"
#include "sha.h"

#include <stdint.h>
#include <cstddef>

#if defined _WIN32 || defined __CYGWIN__
  #ifdef BUILDING_DLL
    #define DLL_PUBLIC __declspec(dllexport)
  #else
    #define DLL_PUBLIC __declspec(dllimport)
  #endif
#else
  #define DLL_PUBLIC __attribute__ ((visibility ("default")))
#endif

extern "C" DLL_PUBLIC
int sha256_hash_message(
    uint8_t* digest, size_t dsize,
    const uint8_t* message, size_t msize)
{
    using CryptoPP::Exception;
    using CryptoPP::SHA256;

    if (!digest || !message) return 1;
    if (dsize == 0 || dsize > SHA256::DIGESTSIZE) return 1;

    try {
        SHA256().CalculateTruncatedDigest(digest, dsize, message, msize);
        return 0;
    } catch (const Exception&) {
        return 1;
    }
}

extern "C" DLL_PUBLIC
int sha256_verify_digest(
    const uint8_t* digest, size_t dsize,
    const uint8_t* message, size_t msize)
{
    using CryptoPP::Exception;
    using CryptoPP::SHA256;

    if (!digest || !message) return 1;
    if (dsize == 0 || dsize > SHA256::DIGESTSIZE) return 1;

    try {
        bool verified =
            SHA256().VerifyTruncatedDigest(digest, dsize, message, msize);
        return verified ? 0 : 1;
    } catch (const Exception&) {
        return 1;
    }
}
