import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pdlpy",
    version="0.1.0",
    author="André Bienemann",
    author_email="andre.bienemann@gmail.com",
    description="Probability Distribution Library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrebienemann/pdlpy",
    extras_require={
        "dev": [
            "black",
            "coverage",
            "isort",
        ],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
