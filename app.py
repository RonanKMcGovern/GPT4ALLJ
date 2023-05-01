from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt4allj import Model

app = Flask(__name__)
CORS(app)

model = Model('./models/ggml-gpt4all-j.bin')

@app.route('/complete', methods=['POST'])
def complete():
    prompt = request.json.get('text', '')
    # completion_length = request.json.get('completionLength', 500)  # Set a default value if promptLength is not provided
    print('Received prompt:', prompt)
    # print('Received completion length:', completion_length)
    completion = model.generate(prompt, n_threads=8, n_predict=500)
    return jsonify({'completion': completion})


if __name__ == '__main__':
    app.run()
