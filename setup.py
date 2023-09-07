# setup.py placed at root directory

from setuptools import setup

setup(
    name="pynopepe",
    version="1.0",
    packages=["nopepe"],
    description="pls no pepe ONNX runtime",
    python_requires=">=3.8, <4",
    install_requires=["onnxruntime>=1.14.1",
                      "numpy>=1.23.5",
                      "pillow>=9.5.0"],
    extras_require={
        "test": ["pytest"],
    }
)
