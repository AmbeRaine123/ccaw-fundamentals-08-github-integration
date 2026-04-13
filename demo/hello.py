"""
Hello World demo — added by Claude via the GitHub Integration workflow.

This file was created automatically in response to:
  @claude please implement this

It demonstrates that the Claude Code GitHub Actions integration is working end-to-end.
"""


def hello(name: str = "World") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello())
    print(hello("Claude Code"))
