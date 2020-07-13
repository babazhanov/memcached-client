import socket

# docs
# https://github.com/memcached/memcached/blob/master/doc/protocol.txt


class Client:

    def __init__(self, host):
        self.host = host

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, 11211))

    def __del__(self):
        if hasattr(self, 'socket') and isinstance(self.socket, socket.socket):
            self.socket.close()

    def set(self, key: str, value: str):
        """Записать значение"""

        self.socket.send(
            'set {} 0 3600 {}\r\n'.format(key, len(value))
            .encode()
        )
        self.socket.send(value.encode())
        self.socket.send(b'\r\n')

        ret = self.socket.recv(4096)

        return ret == b'STORED\r\n'

    def get(self, key: str):
        """Прочитать значение"""

        self.socket.send("get {}\r\n".format(key).encode())

        ret = self.socket.recv(4096)
        ret = ret.decode().split('\r\n')

        return ret[1]

    def delete(self, key: str):
        """Удалить значение"""

        self.socket.send("delete {}\r\n".format(key).encode())

        ret = self.socket.recv(4096)

        return ret == b"DELETED\r\n"

    def close(self):
        self.socket.close()
        self.socket = None
