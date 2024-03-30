from typing import cast

from langchain.chains import LLMChain

from rich import print
from rich.prompt import Prompt
from rich.table import Table

from shai.llm import llm
from shai.prompt import prompt, output_parser, CmdOutput
from shai.exec import run_shell_script

llm_chain = LLMChain(llm=llm, prompt=prompt)


def show_command_table(question, cmd, reason, title="command") -> None:
    table = Table(title=title)

    table.add_column("Command", style="magenta")
    table.add_column("Question", justify="right", style="cyan", no_wrap=True)
    table.add_column("Reason", justify="right", style="green")

    table.add_row(f"$ {cmd}", question, reason)
    print(table)


def generate_shell_command(question: str, confirm_run: bool = True) -> str | None:
    output = llm_chain.invoke({"question": question})
    generated_cmd = cast(CmdOutput, output_parser.parse(output.get("text")))

    print("Command generated: ", generated_cmd.command)
    if confirm_run:
        answer = Prompt.ask(
            "Proceed to run command?", choices=["y", "n"], default="yes"
        )
        if answer == "n":
            show_command_table(
                question, generated_cmd.command, "cancelled", title="run this command"
            )
            return

    shelloutput = run_shell_script(generated_cmd.command)
    if not shelloutput:
        print(f"Failed to run command: {generated_cmd.command}")
        return

    return shelloutput
