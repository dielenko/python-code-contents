<h1>Python 3 Docker container</h1>

## Summary
This is a VS Code Remote - Container abstraction that lets you use a Python 3 Docker container as a full-featured development environment. It is sourced from the official one provided in [microsoft/vscode-dev-containers](https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3).\
*This solution provides a way to get going quickly with configuration of Python 3 local development environment in Docker container abstraction. Includes Python 3, the Docker CLI (for testing locally), Node.js, Git, and related extensions and dependencies. The solution can be prepared as a development environemnt shared across all team members in a dedicated project.* \
This abstraction allows you to open any folder inside (or mounted into) the prepared Docker container and take advantage of VS Code's full feature set. A devcontainer.json file in the project tells VS Code how to access (or create) a development container with a well-defined tool and runtime stack. This container can be used to run Python 3 and all of the related tools described above.

*Enabled VS Code Extensions in the default Remote - Container configuration:*

| Extensions             | Description                                                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
| *Python*               | IntelliSense (Pylance), Linting, Debugging, Jupyter Notebooks, code formatting, refactoring, unit tests, and more |
| *Pylance*              | A performant, feature-rich language server for Python in VS Code                                                  |
| *Better Comments*      | Improve your code commenting by annotating with alert, informational, TODOs, and more                             |
| *Python Test Explorer* | Run Python tests in the Sidebar of VS Code                                                                        |
| *Python Indent*        | Correct Python indentation in VS Code                                                                             |
| *Python Snippets*      | Code snippets for python                                                                                          |
| *Python Type Hint*     | Type hint completion for Python                                                                                   |
| *AREPL for python*     | AREPL automatically evaluates python code in real-time as you type                                                |
| *autoDocstring*        | Generates python docstrings automatically                                                                         |
| *GitLens*              | Helps you to visualize code authorship at a glance via Git blame annotations and CodeLens                         |

*VS Code Remote - Container metadata details:*

| Metadata                    | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| *Categories*                | Object-Oriented and Functional Programming                   |
| *Definition type*           | Dockerfile, Docker Compose                                   |
| *Supported architecture(s)* | x86-64, arm64/aarch64 for `bullseye` variants of based image |
| *Container host OS support* | Linux, macOS, Windows                                        |
| *Container OS*              | Debian                                                       |
| *Languages, platforms*      | Python                                                       |