import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from agent import AutonomousCoderAgent
import pytest
from unittest.mock import patch, Mock

def test_generate_code():
    # Create a mock response object with the expected content
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.iter_lines.return_value = [
        b'{"text": "def hello_world():\\n    print(\'Hello, world!\')\\n"}'
    ]

    # Patch the requests.post method to return the mock response
    with patch('requests.post', return_value=mock_response):
        agent = AutonomousCoderAgent()
        result = agent.generate_code("def hello_world():")
        assert "Generated code: def hello_world():\n    print('Hello, world!')" in result

# Run the test using pytest
if __name__ == "__main__":
    pytest.main([__file__])