
import socket
import json
import time
import random

HOST = 'ml-analyzer'
PORT = 5050

def generate_log():
    return {
        "timestamp": time.time(),
        "latency": round(random.uniform(50, 700), 2),
        "service": random.choice(["pedidos", "estoque", "pagamento"])
    }

time.sleep(5)  # aguarda serviço ML subir
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for _ in range(50):
        log = generate_log()
        s.sendall((json.dumps(log) + "\n").encode("utf-8"))
        time.sleep(0.5)
