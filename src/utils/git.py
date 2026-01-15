import subprocess
import shutil


def get_staged_diff(context_lines: int = 10) -> str:
    if not shutil.which("git"):
        raise RuntimeError("Git not found.")

    result = subprocess.run(
        ["git", "diff", "--cached", f"-U{context_lines}"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()
