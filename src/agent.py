import requests

class AutonomousCoderAgent:
    def __init__(self, base_url='http://localhost:10000/api', model_name='qwen2.5:latest'):
        self.base_url = base_url
        self.model_name = model_name

    def generate_code(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": 100
        }
        
        try:
            response = requests.post(f"{self.base_url}/generate", json=payload)
            print(f"Response status code: {response.status_code}")
            
            if response.status_code == 200:
                # Read the response line by line and parse each JSON object
                generated_text = []
                for line in response.iter_lines():
                    if line:  # Filter out keep-alive new lines
                        decoded_line = line.decode('utf-8')
                        json_obj = self.parse_json_line(decoded_line)
                        if 'text' in json_obj:
                            generated_text.append(json_obj['text'])
                
                return f"Generated code: {''.join(generated_text)}"
            else:
                raise Exception(f"Error generating code: {response.content.decode('utf-8')}")
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error making API request: {e}")

    def parse_json_line(self, line):
        import json
        try:
            return json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON decode error in line: {line} - Error: {e}")

if __name__ == "__main__":
    agent = AutonomousCoderAgent()
    print(agent.generate_code("def hello_world():"))