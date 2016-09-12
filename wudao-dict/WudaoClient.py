import socket


class WudaoClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("0.0.0.0", 2376))

    def get_word_info(self, word):
        word = word.lower()
        self.client.sendall(word.encode('utf-8'))
        server_context = ''
        while True:
            rec = self.client.recv(512)
            if not rec:
                break
            server_context += rec.decode('utf-8')
        self.client.close()
        return server_context

    def close(self):
        self.client.sendall('---shutdown keyword---'.encode('utf-8'))