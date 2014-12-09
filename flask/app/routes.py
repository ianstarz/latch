from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  return 'hello world'

@app.route('/widgets')
def widgets():
  return jsonify({'widgets': [{'id': 1}, {'id': 2}, {'id': 3}]})

if __name__ == '__main__':
  app.run(debug=True)
