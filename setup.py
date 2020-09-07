import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TeamSingaSushi", # Replace with your own username
    version="3.1.1",
    description="GDAL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeamSingaSushi/gdal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.2',
)
