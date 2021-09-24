from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as f_in:
    long_description = f_in.read()

setup(
    name="delimited_protobuf",
    version="0.0.2",
    author="soulmachine",
    description="Save multiple Protobuf messages to a file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soulmachine/delimited-protobuf",
    py_modules=["delimited_protobuf"],
    install_requires=['protobuf'],
    license='Apache License 2.0',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['protobuf', 'delimited', 'serialization'],
)
