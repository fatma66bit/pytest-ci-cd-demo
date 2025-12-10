from setuptools import setup, find_packages

setup(
    name="mon-projet-test-ci",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    tests_require=[
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
    ],
)