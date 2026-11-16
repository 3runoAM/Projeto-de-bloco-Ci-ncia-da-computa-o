import subprocess
import threading
import time

from flask import Flask, request

app = Flask(__name__)

def iniciar_servidor():
    app.run(host="0.0.0.0", port=8080)

@app.route("/", methods=["POST"])
def dados_servidor():
    body = request.get_data(as_text=True)
    print(body)
    return body

if __name__ == "__main__":
    print("| Servidor subindo...")
    threading.Thread(target=iniciar_servidor, daemon=True).start()

    time.sleep(1)

    print("| Fazendo requisição...")

    subprocess.run(["curl", "-X", "POST", "http://localhost:8080/", "-d", "hello world"])
