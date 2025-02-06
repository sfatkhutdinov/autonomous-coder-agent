# tests/test_agent.py
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from agent import AutonomousCoderAgent
import pytest

def test_generate_code():
    agent = AutonomousCoderAgent()
    result = agent.generate_code("def hello_world():")
    assert "Generated code: def hello_world():" in result