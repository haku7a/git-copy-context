import subprocess
import shutil
import os


def get_staged_diff(context_lines: int = 10) -> str:
    if not shutil.which("git"):
        raise RuntimeError("Git not found.")

    current_dir = os.getenv("PWD") or os.getcwd()

    result = subprocess.run(
        ["git", "diff", "--cached", f"-U{context_lines}"],
        capture_output=True,
        text=True,
        check=True,
        cwd=current_dir,
    )
    return result.stdout.strip()
