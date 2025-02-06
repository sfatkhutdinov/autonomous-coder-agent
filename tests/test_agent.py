# tests/test_agent.py

import pytest
from src.agent import AutonomousCoderAgent

def test_generate_code():
    agent = AutonomousCoderAgent()
    result = agent.generate_code("Hello, world!")
    assert "Generated code: Hello, world!" in result