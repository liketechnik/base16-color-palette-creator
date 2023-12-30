from setuptools import setup

setup(
  name='base16-color-palette-creator',
  install_requires=['pyyaml', 'Pillow'],
  scripts=[
    'creator.py',
  ],
)
