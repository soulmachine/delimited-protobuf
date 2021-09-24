# delimited-protobuf

A read/write library for length-delimited protobuf messages.

It is a very common use case to save multiple protobuf messages to a file, this tiny library provides `read()` and `write()` functions to fullfill this need.

Each message is preceded by a [Varint](https://developers.google.com/protocol-buffers/docs/encoding#varints) containing their size:

![File format](./images/file-format.svg)

## Install

`conda install -c conda-forge delimited-protobuf`

## References

- [`CodedOutputStream`](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/io/coded_stream.h#L47)
- [`MessageLite#writeDelimitedTo`](https://github.com/protocolbuffers/protobuf/blob/master/java/core/src/main/java/com/google/protobuf/MessageLite.java#L126)
- [`CodedInputStream`](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/io/coded_stream.h#L66)
- [`parseDelimitedFrom()`](https://github.com/protocolbuffers/protobuf/blob/master/java/core/src/main/java/com/google/protobuf/Parser.java)
