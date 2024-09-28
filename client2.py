''' Here the client is an AI bot 
    Responses are generated from the GPT API
    Input is transferred from client-1 --> client-2 
    Here the output is printed
'''

import socket

import google.generativeai as genai
import os

api_key = os.environ.get("API_KEY")  # Returns None if not found

if api_key:
    genai.configure(api_key=api_key)
else:
    raise ValueError("API_KEY environment variable is not set.")

def start_client():
    client = socket.socket()
    client.connect(("localhost", 8080))

    while True:
        message = client.recv(1024).decode()
        if message == "exit":
            break
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(message)
        # print(response.text)
        client.sendall(response.text.encode())
    client.close()

start_client()