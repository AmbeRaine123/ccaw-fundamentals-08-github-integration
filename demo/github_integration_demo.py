"""
GitHub Integration Demo
=======================
This file was created automatically by Claude Code via the GitHub Actions workflow.
It demonstrates the end-to-end integration working: @claude mention → code committed.

Usage:
    python demo/github_integration_demo.py
"""


def greet(name: str = "World") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def summarize_workflow() -> dict:
    """Return a summary of the GitHub integration workflow."""
    return {
        "trigger": "@claude mention in issue or PR comment",
        "workflow": [
            "User mentions @claude in a GitHub comment",
            "GitHub Actions workflow fires",
            "Claude reads the issue/PR context",
            "Claude implements the requested changes",
            "Claude commits and pushes to a new branch",
            "Claude posts a link to create a PR",
            "User reviews and merges the PR",
        ],
        "workflows_installed": [
            ".github/workflows/claude.yml           (interactive assistant)",
            ".github/workflows/claude-code-review.yml (automatic PR reviews)",
        ],
    }


def main() -> None:
    print(greet("GitHub Integration"))
    print()

    summary = summarize_workflow()
    print(f"Trigger: {summary['trigger']}")
    print()
    print("Workflow steps:")
    for i, step in enumerate(summary["workflow"], 1):
        print(f"  {i}. {step}")
    print()
    print("Installed workflows:")
    for workflow in summary["workflows_installed"]:
        print(f"  - {workflow}")


if __name__ == "__main__":
    main()
