from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("NawneetServer")

@mcp.tool()
def greet_nawneet() -> str:
    """Returns a greeting to Nawneet boos"""
    return "Hello Nawneet boos"

if __name__ == "__main__":
    mcp.run(transport='stdio') 