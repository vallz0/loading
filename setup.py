from setuptools import setup, find_packages

setup(
    name="loading",
    version="1.0.0",
    description="A terminal loading effect library for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vallz",
    author_email="valldircalado@gmail.com",
    url="https://github.com/vallz0/loading",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
