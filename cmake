cmake_minimum_required(VERSION 3.15)
project(sha256_ffi LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

find_package(cryptopp REQUIRED)

add_library(sha256_ffi SHARED sha256_ffi.cpp)
target_link_libraries(sha256_ffi cryptopp)

target_compile_definitions(sha256_ffi PRIVATE BUILDING_DLL)
