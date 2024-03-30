#!/usr/bin/env python3

import typer

from rich.prompt import Prompt
from shai.chain import generate_shell_command
from rich import print

from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()


@app.command()
def explain(cmd: str):
    """
    Explain how the Shai AI generates commands based on user input.

    This command will print an explanation of the command
    """
    print(f'Explaining "{cmd}" coming soon...')


@app.command()
def shell():
    """
    Start a shell that generates commands based on input.

    This shell will prompt for input, and then use the Shai AI to generate a shell
    command based on that input. The command will be printed below the input, and the
    user can then choose to run the command or not.

    To exit the shell, simply press ^D (control-D).
    """
    while True:
        try:
            cmd = Prompt.ask("shai$")
            out = generate_shell_command(cmd)
            print("------")
            print(out)
        except (KeyboardInterrupt, EOFError):
            break
        except Exception as e:
            print("Failed to run command:", e)
            typer.Exit(1)
