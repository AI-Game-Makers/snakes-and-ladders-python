from setuptools import setup, find_packages

setup(
    name="snakes-and-ladders",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snakes-and-ladders = src.game:main",
        ],
    },
    install_requires=[
        "colorama",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.8',
)
