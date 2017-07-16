from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='hanalmot',
    version='0.1.1',
    description='hanalmot korean text tokenizer',

    url='https://github.com/cookieshake/pyokt',

    author='cookieshake',
    author_email='cookieshake@github.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='hanalmot korean text tokenize',
    packages=['hanalmot'],
    install_requires=['jpype1']
)
