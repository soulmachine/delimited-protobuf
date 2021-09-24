# delimited-protobuf

A read/write library for length-delimited protobuf messages.

It is a very common use case to save multiple protobuf messages to a file, this tiny library provides `read()` and `write()` functions to fullfill this need.

Each message is preceded by a [Varint](https://developers.google.com/protocol-buffers/docs/encoding#varints) containing their size:

![File format](./images/file-format.svg)
