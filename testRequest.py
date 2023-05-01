import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
server_ip = os.getenv('SERVER_IP')

url = f'http://{server_ip}:8000/complete'
data = {'text': 'Write a short poem about a dog'}
response = requests.post(url, json=data)

print(response.json())  # Print the JSON response from the server
