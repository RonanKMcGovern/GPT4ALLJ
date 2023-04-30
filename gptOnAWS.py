from gpt4allj import Model

model = Model('./models/ggml-gpt4all-j.bin', n_threads=8)

print(model.generate('What are the strengths and weaknesses of AWS versus Google Cloud?'))