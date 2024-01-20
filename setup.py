from setuptools import setup, find_packages

setup(
    name='math',
    version='0.0.1',
    author="Felipe Caetano",
    author_email='felipecaetano0@gmail.com',

    py_modules=['main'],
    packages=['src'],
    entry_points={
        'console_scripts': [
            'math = src.main:main'
        ]
    }
)
