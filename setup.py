"""
Author:木森
"""
from setuptools import setup, find_packages

with open("readme.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name='unittestreport',
    version='1.0.2+qy',
    author='wangfei',
    author_email='hiraly333@163.com',
    url='git@github.com:Hiraly-wang/UnitTestReport.git',
    description='A unittest report plugin for python3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Jinja2>=3.0", "PyYAML>=5.3","requests>=2.30"],
    packages=find_packages(),
    package_data={
        "unittestreport": ["templates/*.html",'*.md'],
    },
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)

