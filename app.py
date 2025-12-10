from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! Site Python funcionando 🔥😎"

if __name__ == "__main__":
    app.run()
