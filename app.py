from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        resp = requests.get("http://api:5001/data")
        data = resp.json()
    except Exception:
        data = {"message": "API no disponible"}
    return render_template_string("<h1>WebApp Taller</h1><p>{{ msg }}</p>", msg=data.get("message"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)