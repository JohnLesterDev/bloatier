from setuptools import setup, find_packages

with open("README.md", "r") as f:
    LONG_DESC = f.read()

setup(
    name='bloatier',
    version='0.1.1',
    description="Basic String Bloater/Debloater Algorithm.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    author="John Lester Dev :>",
    author_email="johnlesterincbusiness@gmail.com",
    url="https://pypi.org/project/nhentaidevs",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    keywords=[
        "algorithm",
        "string manipulation",
        "conversion"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
