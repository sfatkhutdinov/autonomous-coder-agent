# src/agent.py

import requests

class AutonomousCoderAgent:
    def __init__(self, base_url='http://localhost:10000/api', 
                 model_name='deepseek-r1:latest'):
        self.base_url = base_url
        self.model_name = model_name

    def generate_code(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": 50
        }
        response = requests.post(f"{self.base_url}/generate", json=payload)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content.decode('utf-8')}")

        if response.status_code == 200:
            try:
                generated_text = response.json().get('text', '')
                return f"Generated code: {generated_text}"
            except requests.exceptions.JSONDecodeError as e:
                raise Exception(f"Error decoding JSON response: {e}")
        else:
            raise Exception(f"Error generating code: {response.content.decode('utf-8')}")

if __name__ == "__main__":
    agent = AutonomousCoderAgent()
    print(agent.generate_code("def hello_world():"))