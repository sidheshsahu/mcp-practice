from mcp.server.fastmcp import FastMCP


mcp = FastMCP("My First MCP Server")

# Define a tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


if __name__ == "__main__":
    mcp.run()