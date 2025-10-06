import asyncio
import os

from langchain_ollama.chat_models import ChatOllama
from mcp_use import MCPAgent, MCPClient

# Get the server script path (same directory as this file)
current_dir = os.path.dirname(os.path.abspath(__file__))
server_path = os.path.join(current_dir, "src/main.py")


# Describe which MCP servers you want.
CONFIG = {
    "mcpServers": {
        "mtg": {
            "command": "uv",
            "args": ["run", "mcp", "run", "src/main.py"]
        }
    }
}

async def main():
    client = MCPClient.from_dict(CONFIG)
    llm = ChatOllama(model="llama3.1", base_url="http://localhost:11434")

    # Wire the LLM to the client
    agent = MCPAgent(llm=llm, client=client, max_steps=20, verbose=True)
    await agent.initialize()
    # Give prompt to the agent
    query = ""
    result = await agent.run(
        f"{query} Always use a tool if available instead of doing it on your own"
    )
    print("\n🔥 Result:", result)

    # Always clean up running MCP sessions
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
