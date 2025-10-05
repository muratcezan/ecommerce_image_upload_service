"""Setup module for the image_upload_service package.

This module provides the configuration for packaging the image_upload_service
library, which contains secure and configurable image upload handling for
Flask-based ecommerce projects.
"""

import os
from setuptools import setup, find_packages


def read_long_description():
    """Reads the README.md file if it exists, otherwise returns an empty string."""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


setup(
    name="image_upload_service",
    version="0.1.0",
    packages=find_packages(include=["image_upload_service", "image_upload_service.*"]),
    install_requires=[
        "Werkzeug>=2.0",
        "Flask>=2.0",
    ],
    python_requires=">=3.8",
    author="Murat CEZAN",
    author_email="muratcezan@gmail.com",
    description=(
        "A helper service that provides secure and configurable "
        "image upload handling for Flask-based web applications."
    ),
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/muratcezan/ecommerce_image_upload_service",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Flask",
    ],
    include_package_data=True,
)
