
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  print("Executou a rota padrao")
  return "API de predicao de credito"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

