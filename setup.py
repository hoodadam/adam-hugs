"""Setup script for installing hugs."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'hugs',
    'author': 'Adam Hood',
    'url': 'Project URL https://github.com/hoodadam/adam-hugs',
    'download_url': 'https://github.com/hoodadam/adam-hugs',
    'author_email': 'kd5wxb@gmail.com',
    'version': '0.1.1',
    'install_requires': ['numpy', 'matplotlib'],
    'packages': ['hugs', 'hugs.calc', 'hugs.plots'],
    'scripts': [],
    'name': 'adam-hugs'
}

setup(**config)
