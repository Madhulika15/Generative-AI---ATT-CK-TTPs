from setuptools import setup, find_packages

setup(
    name="attack_extractor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "datasets",
        "gradio",
        "scikit-learn",
        "nltk",
        "pandas",
        "openpyxl",
        "rapidfuzz",
        "sentence-transformers",
        "networkx",
        "matplotlib",
    ],
    entry_points={
        'console_scripts': [
            'attack_extractor=src.web_app:main',
        ],
    },
)
