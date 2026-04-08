# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Project'
author = 'Author'

# -- General configuration ---------------------------------------------------

html_static_path = ['_static']

html_css_files = [
    'style.css',
]

# Source file suffixes - support both reStructuredText and Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'  # your root document

templates_path = ['templates']  # Important: enables your custom templates

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_title = "$1800 Monthly Social Security Increase – Eligibility, Payment Dates & Latest Update"

# You can still add html_meta here if you want, but with the new Read the Docs addons
# custom template is the reliable way to inject meta tags.

# If you want to add other meta tags, do so in your _templates/layout.html


