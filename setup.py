"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages


def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements

    """

    install_reqs = parse_requirements(filename=source)
    return [req for req in install_reqs]

def parse_requirements(filename):
  with open(filename) as requirements:
      # Skipping -i https://pypi.org/simple
    return requirements.readlines()[1:]

setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)
