from setuptools import setup

from local_requirement import local_requirement


setup(
    name='lib-b',
    install_requires=[
        local_requirement('lib-c'),
    ],
)
