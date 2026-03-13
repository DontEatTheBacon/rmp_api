from setuptools import setup, find_packages

setup(
    name="rmp_api",
    version="0.1.0",
    description="Unofficial Python API for scraping RateMyProfessors",
    author="Andrew Valentine",
    url="https://github.com/DontEatTheBacon/rmp_api",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0"
    ],
    python_requires=">=3.9",
)
