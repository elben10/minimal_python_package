# minimal_python_package

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)

```bash
pip install -U cookiecutter
```
Generate a Python package project::

```bash
cookiecutter https://github.com/elben10/minimal_python_package.git
```

- [ ] Add index.md symlink without admin rights
- [ ] Add click
- [ ] Add tests
- [ ] Extend setup.py with a `python setup.py docs` command to run docs without having to change into the docs directory
- [ ] Extend setup.py with a `python setup.py format` command to format code
