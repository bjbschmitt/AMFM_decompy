# conf.py - Sphinx configuration file

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'AMFM decompy'
author = 'Bernardo J. B. Schmitt'
copyright = '2025, Bernardo J. B. Schmitt'

# The full version, including alpha/beta/rc tags
release = '1.0.12'
version = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

html_theme = 'classic'  # or 'sphinx_rtd_theme' if installed

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory.
html_static_path = ['../_images']