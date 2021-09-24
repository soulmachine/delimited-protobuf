"""Save multiple Protobuf messages to a file"""

from __future__ import absolute_import

from typing import BinaryIO, Optional, Type, TypeVar

from google.protobuf.internal.decoder import _DecodeVarint
from google.protobuf.internal.encoder import _EncodeVarint
from google.protobuf.message import Message

T = TypeVar('YourProtoClass', bound=Message)


def _read_varint(stream: BinaryIO, offset: int = 0) -> int:
    """Read a varint from the stream."""
    if offset > 0:
        stream.seek(offset)
    buf: bytes = stream.read(1)
    if buf == b'':
        return 0
    while (buf[-1] & 0x80) >> 7 == 1:  # while the MSB is 1
        new_byte = stream.read(1)
        if new_byte == b'':
            raise EOFError('unexpected EOF')
        buf += new_byte
    varint, _ = _DecodeVarint(buf, 0)
    return varint


def read(stream: BinaryIO, proto_class_name: Type[T]) -> Optional[T]:
    """
    Read a single size-delimited message from the given stream.

    Similar to:
      * parseDelimitedFrom() in https://github.com/protocolbuffers/protobuf/blob/master/java/core/src/main/java/com/google/protobuf/Parser.java
      * ParseDelimitedFromZeroCopyStream() in https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/util/delimited_message_util.h
    @returns new offset.
    """
    size = _read_varint(stream)
    if size == 0:
        return None
    buf = stream.read(size)
    msg = proto_class_name()
    msg.ParseFromString(buf)
    return msg


def write(stream: BinaryIO, msg: T):
    """
    Write a single size-delimited message to the given stream.

    Similar to:
      * writeDelimitedTo() in https://github.com/protocolbuffers/protobuf/blob/master/java/core/src/main/java/com/google/protobuf/MessageLite.java
      * SerializeDelimitedToZeroCopyStream() in https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/util/delimited_message_util.h
    """
    assert stream is not None
    _EncodeVarint(stream.write, msg.ByteSize())
    stream.write(msg.SerializeToString())
