# Drosophila Curriculum — Supplemental Materials

This repository holds the supplemental materials for the following manuscript (currently being drafted):

> **From Development to Connectomics: A Scaffolded _Drosophila_ Curriculum for Understanding Brain Wiring and Behavior**
>
> Jelly Hubertus Maria Soffers, Matthew Clark, Durafshan Sakeena Syed, Frank Loesche, Budhaditya Chowdhury, & Syed Mubarak Hussain

The published site is available at <https://floesche.github.io/drosophila-curriculum>.

## Editing the site locally

The site is built with [Quarto](https://quarto.org/). All dependencies are managed through [pixi](https://pixi.sh/), so no manual installation of Quarto or other tools is required. If you get stuck, see [Getting help from an LLM](#getting-help-from-an-llm) below.

### 1. Install pixi

pixi manages **all** dependencies (Quarto, Python, and more). You do **not** need to install them separately.

Follow the [official installation instructions](https://pixi.sh/latest/getting_started/) for your operating system, or use the quick commands below.

> **Important:** Pick the command that matches your operating system. Running the wrong one will produce confusing errors.

**Windows**: open **PowerShell** and run:

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

**Linux** or **macOS**: open a terminal and run:

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

After installation, **close and reopen your terminal** so the `pixi` command is available.

### 2. Clone and preview

First, navigate to the folder where you want to store the project. For example:

```bash
cd ~/Documents        # or any folder you prefer
```

Then clone the repository and start the preview:

```bash
git clone https://github.com/floesche/drosophila-curriculum.git
cd drosophila-curriculum
pixi run preview
```

This installs all dependencies automatically on the first run and opens a live-reloading preview at `http://localhost:8000`.

> **Troubleshooting:** Always use `pixi run preview` (not `quarto preview` directly). pixi sets up the correct environment with all required tools. If you see errors about missing tools or paths, make sure you are running commands through pixi.

### 3. Build the site

```bash
pixi run render
```

Output goes to `public/`.

### Available pixi tasks

| Command | Description |
|---------|-------------|
| `pixi run preview` | Live-reloading local preview |
| `pixi run render` | Build the static site to `public/` |
| `pixi run clean` | Remove generated files |

## Getting help from an LLM

If you run into problems and want to ask ChatGPT, Copilot, Claude, or another LLM for help, include the following context in your prompt so it can give you accurate advice:

> I'm working with a Quarto website project that uses **pixi** (https://pixi.sh/) to manage all dependencies. The repository is at https://github.com/floesche/drosophila-curriculum. pixi installs Quarto, Python, and everything else automatically. I do not install these tools separately. I run all commands through pixi (e.g., `pixi run preview`, `pixi run render`). The project configuration is in `_quarto.yml` and dependencies are defined in `pixi.toml`.
>
> [Paste your error message here]

This prevents the LLM from suggesting you install Quarto or Python manually, create virtual environments, or take other steps that bypass pixi and cause further issues.
