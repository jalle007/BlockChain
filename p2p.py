import socket
import threading
import json
from blockchain import Blockchain
from block import Block

class P2PNode:
    def __init__(self, blockchain, host='127.0.0.1', port=5000):
        self.blockchain = blockchain
        self.host = host
        self.port = port
        self.peers = []  # List of peer sockets

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Node listening on {self.host}:{self.port}")
        threading.Thread(target=self.accept_connections, args=(server,)).start()

    def accept_connections(self, server):
        while True:
            conn, addr = server.accept()
            self.peers.append(conn)
            print(f"Connected to peer: {addr}")
            threading.Thread(target=self.handle_peer, args=(conn,)).start()

    def handle_peer(self, conn):
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break
                self.process_message(json.loads(data))
            except Exception as e:
                print(f"Error handling peer: {e}")
                break
        conn.close()

    def process_message(self, message):
        if message['type'] == 'blockchain':
            incoming_chain = message['data']
            self.synchronize_chain(incoming_chain)

    def broadcast_chain(self):
        message = {
            'type': 'blockchain',
            'data': [block.__dict__ for block in self.blockchain.chain]
        }
        for peer in self.peers:
            peer.send(json.dumps(message).encode())

    def synchronize_chain(self, incoming_chain):
        if len(incoming_chain) > len(self.blockchain.chain):
            print("Updating blockchain...")
            self.blockchain.chain = [Block(**block) for block in incoming_chain]

    def connect_to_peer(self, peer_host, peer_port):
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect((peer_host, peer_port))
        self.peers.append(peer)
        print(f"Connected to peer at {peer_host}:{peer_port}")
