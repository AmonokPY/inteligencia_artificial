from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

modelo = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizador = GPT2Tokenizer.from_pretrained("gpt2")

entrada = "Había una vez un robot que aprendió a"

entrada_tokens = tokenizador.encode(entrada, return_tensors="pt")

salida_tokens = modelo.generate(
    entrada_tokens,
    max_length=100,
    num_return_sequences=1,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    do_sample=True
)

texto_generado = tokenizador.decode(salida_tokens[0], skip_special_tokens=True)
print("\nTexto generado:\n")
print(texto_generado)
