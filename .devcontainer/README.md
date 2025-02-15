<h1>Python 3 Docker container</h1>

## Summary

This is a `VS Code development container abstraction` that provides a `Python 3 Docker container` as a full-featured development environment.  
Builded from the [Ubuntu](https://github.com/devcontainers/images/tree/main/src/base-ubuntu) base development container image.  
This solution provides a way to get going quickly with configuration of Python 3 local development environment in Docker container abstraction.  
Includes `Python 3`, `Git`, [Common Utilities](https://github.com/devcontainers/features/tree/main/src/common-utils) and the related `extensions` and `dependencies`.  
_The solution can be prepared as a development environemnt shared across all team members in a dedicated project._  
This abstraction allows you to open any folder inside (or mounted into) the prepared `Docker container` and take advantage of VS Code's full feature set.  
A `devcontainer.json` file in the project tells VS Code how to access (or create) a development container with a well-defined tool and runtime stack.  
This container can be used to run Python 3 and all of the related tools.

_Enabled VS Code Extensions:_

| Extensions              | Description                                                                                                                      |  
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------- |  
| `Python Extension Pack` | Python, Jinja, Django, Visual Studio IntelliCode, Python Environment Manager, Python Docstring Generator, Python Indent, Jupyter |  
| `Python PyPI Assistant` | There are convenient hover tooltips and CodeLens for PyPI dependencies, comparable to what VS Code offers for package.json dependencies. |  
| `Pip Manager`           | Python package manager in VS Code |  
| `GitLens`               | Use CodeLens and Git blame annotations to quickly see code authorship. |  
| `PyCharm Theme`         | PyCharm Theme for VSCode |  
| `Todo Tree`             | This addon finds comment tags like TODO, FIXME and more in the workspace rapidly |  
| `Markdown All in One`   | Everything required for Markdown, including auto preview, table of contents, and keyboard shortcuts. |  
| `Markdown Lint`         | Linting and style checking for VS Code using Markdown/CommonMark |  
| `:emojisense:`          | Adds emoji autocomplete and recommendations to VS Code. |  

_VS Code Development Container metadata:_

| Metadata                    | Description                                  |  
| --------------------------- | -------------------------------------------- |  
| `Categories`                | Object-Oriented and Functional Programming |  
| `Definition type`           | Dockerfile |  
| `Supported architecture(s)` | x86-64, arm64/aarch64 of the based image |  
| `Container host OS support` | Linux, macOS, Windows |  
| `Container OS`              | Ubuntu 24.04 (Noble) |  
| `Languages, platforms`      | Python |  
