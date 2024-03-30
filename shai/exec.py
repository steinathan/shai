import shlex
import subprocess


def run_shell_script(script_string) -> str | None:
    try:
        command_list = shlex.split(script_string)
        result = subprocess.run(command_list, capture_output=True, text=True)
        return (result.stderr or result.stdout).strip()
    except subprocess.CalledProcessError:
        pass
