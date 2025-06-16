
import pandas as pd
from sklearn.ensemble import IsolationForest
import json
import socket

# Função para simular leitura contínua de logs do Logstash via socket (TCP)
def receive_logs(port=5050):
    s = socket.socket()
    s.bind(("0.0.0.0", port))
    s.listen(1)
    print(f"ML Service listening on port {port}")
    conn, addr = s.accept()
    print(f"Connection from {addr}")

    data = []
    try:
        while True:
            line = conn.recv(1024)
            if not line:
                break
            try:
                log = json.loads(line.decode('utf-8'))
                if 'latency' in log:
                    data.append([log['latency']])
            except:
                continue
    finally:
        conn.close()
    return pd.DataFrame(data, columns=["latency"])

# Detecta outliers com Isolation Forest
def detect_anomalies(df):
    if df.empty:
        print("No data received.")
        return
    clf = IsolationForest(contamination=0.1)
    df['anomaly'] = clf.fit_predict(df[['latency']])
    print(df[df['anomaly'] == -1])

if __name__ == "__main__":
    df_logs = receive_logs()
    detect_anomalies(df_logs)
