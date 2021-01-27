# Unified State Exam preparation program

I use Poetry for the project management, and I don't care if you don't. If you want to
test your solutions by yourself then this instruction is written for you.

Anyway to integrate pycharm with poetry see
the ["How to integrate PyCharm with this project"](#how-to-integrate-pycharm-with-this-project)
section.

At first, you need to install poetry. You can find more information about poetry
here: https://python-poetry.org/docs

# Poetry installation

# Windows

In powershell run :

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
poetry install
```

## Linux | MacosX

In any terminal run:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
poetry install
```
# Questions and answers

## How to test my solutions?

Easier than you think.

```bash
pytest # Run it after 'poetry shell' command
```

## How to automatically format my code?

```bash
black . # Run it after 'poetry shell' command
```

## For those who want to go deeper in linting

If you really want production-level linting (You don't need it, really), you need to
install dependencies with the "flake" extra.

```bash
poetry install -E flake
flake8 . --count # This command will count style errors in your code
```

# How to integrate PyCharm with this project

This option will remove all import errors from any module.

1. Open File > Setting ...
2. Find the "Plugins" section.
3. In marketplace search for the "poetry" plugin.
4. Install it and restart PyCharm.
5. In settings find the "Project interpreter" section.
6. Click on thee dots in top-right corner.
7. In menu select "Add...".
8. In right menu find "Poetry Environment" and click "Ok".
9. You're excellent. Now you have no syntax errors, and you're good to go.

