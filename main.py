"""
This project was maden by @kalg12.
It is a simple example of how to use the Ollama LLM with LangChain.
It uses the OllamaLLM class to connect to a local LLM model.
"""

# main.py
from langchain_ollama import OllamaLLM

# 1. Instancia del modelo
print("Conectando con el cerebro local...")
llm = OllamaLLM(model="llama3.1")

# 2. Le hacemos una pregunta simple
pregunta = "Explícame en una frase corta qué es SQL."

print(f"Pregunta: {pregunta}")
print("Pensando...")

# 3. Ejecutamos
respuesta = llm.invoke(pregunta)

print(f"Respuesta: {respuesta}")