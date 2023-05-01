from gpt4allj import Model

model = Model('./models/ggml-gpt4all-j.bin')

print(model.generate('What are the strengths and weaknesses of AWS versus Google Cloud?', n_threads=8))

# The truncated response is due to the limit on number of tokens generated which is 200 by default but can be changed using n_predict: e.g. model.generate('...', n_predict=200)