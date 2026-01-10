# mentor/agent.py
from host.agent import root_agent as host_root_agent
from google.adk import Agent

# Expose it as mentor’s root agent
root_agent = host_root_agent
