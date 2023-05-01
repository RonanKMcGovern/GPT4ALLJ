from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt4allj import Model

app = Flask(__name__)
CORS(app)

model = Model('./models/ggml-gpt4all-j.bin')

@app.route('/complete', methods=['POST'])
def complete():
    prompt = request.json.get('text', '')
    completion = model.generate(prompt, n_threads=8, n_predict=100)
    return jsonify({'completion': completion})

if __name__ == '__main__':
    app.run()
