"""Setup script for the Image Upload Service package.

This module uses setuptools to package and distribute the
Image Upload Service, which provides secure file upload handling
for Flask applications.
"""

from setuptools import setup, find_packages

# Package metadata constants
PACKAGE_NAME = "image_upload_service"
VERSION = "0.1.0"
AUTHOR = "Murat Cezan"
AUTHOR_EMAIL = "muratcezan@gmail.com"
DESCRIPTION = (
    "A helper service that provides secure and configurable "
    "image upload handling for Flask-based web applications."
)
URL = "https://github.com/muratcezan/ecommerce_image_upload_service"
PYTHON_REQUIRES = ">=3.8"
INSTALL_REQUIRES = [
    "Werkzeug>=2.0",
    "Flask>=2.0",
]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Framework :: Flask",
]


def read_long_description() -> str:
    """Read the long description from README.md if available."""
    try:
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return DESCRIPTION


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    python_requires=PYTHON_REQUIRES,
    classifiers=CLASSIFIERS,
    include_package_data=True,
)
