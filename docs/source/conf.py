# Sphinx configuration — Dev-Log (Flask app package: app)
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Repo root (parent of docs/) so ``import app`` works during autodoc
sys.path.insert(0, os.path.abspath("../.."))

project = "Dev-Log"
copyright = "2026"
author = "Dev-Log"

release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns: list[str] = []

language = "en"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# :class:`flask.Flask` 등 외부 문서 연결
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "flask": ("https://flask.palletsprojects.com/en/stable/", None),
}

autodoc_member_order = "bysource"
napoleon_google_docstring = True
napoleon_numpy_docstring = False


def _strip_flasgger_openapi_block(
    app,
    what,
    name,
    obj,
    options,
    lines: list[str],
) -> None:
    """Flasgger YAML lives after a ``---`` line; strip it so docutils does not parse it as reST."""
    for i, line in enumerate(lines):
        if line.strip() == "---":
            del lines[i:]
            break


def setup(app):
    app.connect("autodoc-process-docstring", _strip_flasgger_openapi_block)
