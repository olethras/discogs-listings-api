from setuptools import setup, find_packages

setup(
    name='discogs-marketplace',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'cloudscraper',
    ],
)
