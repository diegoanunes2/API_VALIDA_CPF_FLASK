from flask import Flask

app = Flask(__name__)

# Carrega a blacklist a partir do arquivo
try:
    with open('blacklist.txt', 'r') as f:
        blacklist = set(line.strip() for line in f)
except FileNotFoundError:
    blacklist = set()

@app.route('/')
def index():
    return "RUNNING", 200

@app.route('/<cpf>')
def check_cpf(cpf):
    # Verifica se o CPF está na blacklist
    if cpf in blacklist:
        return "BLOCK", 200
    return "FREE", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
