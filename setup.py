from setuptools import setup, Extension, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="trash_pandas", # Replace with your own username
    version="0.2.3",
    author="Mifour",
    author_email="mifour@yopmail.com",
    description="Analytic tool for Pandas DataFrame exploration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mifour/trash_pandas/archive/0.2.3.tar.gz",
    packages=find_packages(),
    py_modules=['trash_pandas'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    python_requires='>=3',
)

