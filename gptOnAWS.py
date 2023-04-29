from gpt4allj import Model

model = Model('./models/ggml-gpt4all-j.bin')

print(model.generate('AI is going to'))