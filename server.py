from mcp.server.fastmcp import FastMCP
import webbrowser
# Create an MCP server
mcp = FastMCP("NawneetServer")

@mcp.tool()
def greet_nawneet() -> str:
    """Returns a greeting to Nawneet boos"""
    return "Hello Nawneet boos"

@mcp.tool()
def open_linkedin() -> str:
    """Opens linkedin in a new browser tab."""
    webbrowser.open("https://www.linkedin.com/in/nawneet-kumar/")
    return "Linkedin opened successfully!"

@mcp.tool()
def open_github() -> str:
    """Opens github in a new browser tab."""
    webbrowser.open("https://github.com/nawneet77")
    return "Github opened successfully!"
