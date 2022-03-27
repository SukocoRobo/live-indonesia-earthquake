"""
https://packaging.python.org/en/latest/tutorials/packaging-projects/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latesteartquakeindonesiaBMKG",
    version="0.0.1",
    author="SukocoRobo",
    author_email="princezuko@gmail.com",
    description="This package will get latest earthquake from BMKG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SukocoRobo/live-indonesia-earthquake",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)e",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
