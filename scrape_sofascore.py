import requests
import sys

print(f"Python version: {sys.version}")
print(f"Requests version: {requests.__version__}")

# Test if requests is working
try:
    response = requests.get('https://www.example.com')
    print(f"Test request status code: {response.status_code}")
except Exception as e:
    print(f"Error making request: {str(e)}")