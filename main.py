"""
This project was maden by @kalg12.
It is a simple example of how to use the Ollama LLM with LangChain.
It uses the OllamaLLM class to connect to a local LLM model with streaming support.
"""

import sys
from langchain_ollama import OllamaLLM

# 1. Instancia del modelo
print("Conectando con el cerebro local...")
llm = OllamaLLM(model="llama3.1")

# 2. El usuario ingresa su pregunta
pregunta = input("\n💭 Escribe tu pregunta: ")

print(f"\n🤔 Pensando...\n")
print("🤖 Respuesta: ", end="", flush=True)

# 3. Streaming real: el modelo va generando y mostrando tokens conforme los produce
for chunk in llm.stream(pregunta):
    print(chunk, end="", flush=True)

print("\n")  # salto de línea final