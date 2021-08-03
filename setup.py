from setuptools import setup, find_packages

setup(
    name='pdf-extractor',
    version='1.0.0',
    scripts=['bin/pdf_extractor'],
    packages=find_packages(),
    install_requires=[
        'pdfminer.six',
    ]
)