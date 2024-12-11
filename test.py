from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render の PORT 環境変数を使用
    app.run(host="0.0.0.0", port=port)