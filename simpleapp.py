# Deprecated

from gpt4allj import Model, load_library

lib = load_library('./libs/libgptj.dylib', './libs/libggml.dylib')

model = Model('./models/ggml-gpt4all-j.bin', lib=lib)

print(model.generate('AI is going to'))