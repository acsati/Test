from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Ziraat Team from Alp Caner SATI !!!"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=11130)

