# -*- coding: utf-8 -*-

import os
import sys
import six

if six.PY3:
    from unittest.mock import MagicMock
else:
    from mock import Mock as MagicMock


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return Mock()


# -- Options for HTML output -------------------------------------------------


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
    MOCK_MODULES = [
        'argparse', 'numpy', 'scipy',
    ]
    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'default'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'numpydoc'
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'bsseval'
copyright = u'2018, Fabian-Robert Stöter'
author = u'Fabian-Robert Stöter'

version = u'0.1.0'
release = u'0.1.0'

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False

html_static_path = ['_static']

htmlhelp_basename = 'bssevaldoc'

latex_elements = {
}

latex_documents = [
  (master_doc, 'bsseval.tex', u'bsseval Documentation',
   u'Fabian-Robert Stöter', 'manual'),
]

man_pages = [
    (master_doc, 'bsseval', u'musdb Documentation',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'bsseval', u'bsseval Documentation',
   author, 'bsseval', 'One line description of project.',
   'Miscellaneous'),
]
