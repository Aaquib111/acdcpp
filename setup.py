from setuptools import setup, find_packages

setup(
    name="eap",
    version="0.1.0",
    # description="A simple description of your project.",
    # author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "jaxtyping",
        "tqdm",
        "transformer_lens"
    ],
)