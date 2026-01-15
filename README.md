# Git Copy Context

## Dependencies

- **uv** (Linux/macOS)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

**Install project dependencies:**
```bash
uv sync
```

**Add alias to `~/.zshrc` (example):**
```zsh
alias gcc="uv --quiet --directory /home/haku7a/projects/git-copy-context run src/main.py"
```