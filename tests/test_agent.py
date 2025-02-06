# tests/test_agent.py

import pytest
from src.agent import AutonomousCoderAgent

def test_generate_code():
    agent = AutonomousCoderAgent()
    result = agent.generate_code("def hello_world():")
    assert "Generated code: def hello_world():" in result  # This is a basic check; the actual output might vary

if __name__ == "__main__":
    pytest.main()