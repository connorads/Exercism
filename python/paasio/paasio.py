import io
from socket import SocketType
from types import TracebackType
from typing import Any, Iterator, Optional, Protocol, Self, Type


class ReadableBuffer(Protocol):
    """Type adapted from Buffer in _typeshed."""

    # Not actually a Protocol at runtime; see
    # https://github.com/python/typeshed/issues/10224 for why we're defining it this way
    def __buffer__(self, __flags: int) -> memoryview:
        ...


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(
        self,
        # TODO we shouldn't be using any here, io.BufferedRandom has required args
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self) -> Iterator[bytes]:
        return self

    def __next__(self) -> bytes:
        line = super().readline()
        if not line:
            raise StopIteration
        self._read_bytes += len(line)
        self._read_ops += 1
        return line

    def read(self, size: Optional[int] = -1) -> bytes:
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    @property
    def read_bytes(self):
        """Return the number of bytes read from the file."""
        return self._read_bytes

    @property
    def read_ops(self):
        """Return the number of read operations performed on the file."""
        return self._read_ops

    def write(self, b: ReadableBuffer) -> int:
        bytes_written = super().write(b)
        self._write_bytes += bytes_written
        self._write_ops += 1
        return bytes_written

    @property
    def write_bytes(self):
        """Return the number of bytes written to the file."""
        return self._write_bytes

    @property
    def write_ops(self):
        """Return the number of write operations performed on the file."""
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket: SocketType) -> None:
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        # TODO is there a way to avoid the type: ignore here?
        return self._socket.__exit__(exc_type, exc_val, exc_tb)  # type: ignore

    def recv(self, bufsize: int, flag: int = 0) -> bytes:
        """Receive data from the socket."""
        data = self._socket.recv(bufsize, flag)
        self._recv_bytes += len(data)
        self._recv_ops += 1
        return data

    @property
    def recv_bytes(self) -> int:
        """Return the number of bytes received from the socket."""
        return self._recv_bytes

    @property
    def recv_ops(self) -> int:
        """Return the number of recv operations performed on the socket."""
        return self._recv_ops

    def send(self, data: ReadableBuffer, flags: int = 0):
        """Send data to the socket."""
        length = self._socket.send(data, flags)
        self._send_bytes += length
        self._send_ops += 1
        return length

    @property
    def send_bytes(self) -> int:
        """Return the number of bytes sent to the socket."""
        return self._send_bytes

    @property
    def send_ops(self) -> int:
        """Return the number of send operations performed on the socket."""
        return self._send_ops
