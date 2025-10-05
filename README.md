# Image Upload Service

Image Upload Service is a lightweight and secure utility for handling image uploads in Flask-based applications.  
It provides filename sanitization, size validation, and automatic directory management for multi-tenant or institutional systems.

---

## Overview

This package is designed for Flask projects that require image upload functionality.  
It ensures safe file saving practices, directory organization, and configurable storage paths.

---

## Features

- Secure file name handling using `werkzeug.utils.secure_filename`
- Automatic folder creation per institution or entity
- Configurable base upload directory
- File size validation (default: 2 MB)
- Supported image formats: `png`, `jpg`, `jpeg`, `webp`
- Simple integration with any Flask application

---

## Installation

Install using `pip3`:

```bash
pip3 install -e .
```

Or install locally in editable mode:

```bash
pip install -e .
```

## Usage

Example Flask route for uploading an image:

```python
from flask import Flask, request, jsonify
from services.image_upload_service import ImageUploadService

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_image():
    file = request.files.get("file")
    try:
        saved_path = ImageUploadService.save(
            file=file,
            inst_id="123",
            image_type="logo",
            base_folder="static/uploads/institutions"
        )
        return jsonify({"status": "success", "path": saved_path})
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

## API Reference

`ImageUploadService.save(file, inst_id, image_type, base_folder="static/uploads/institutions")`

Saves the uploaded file to the specified location and returns the web-accessible path.

## Configuration

You can customize the base upload directory when calling the save() method.
This allows flexible integration with various storage structures:

```python
ImageUploadService.save(file, inst_id="A01", image_type="banner", base_folder="static/media/uploads")
```

## Requirements

- Python 3.8+
- Flask >= 2.0
- Werkzeug >= 2.0

## License

**MIT License**

Copyright (c) 2025
**Murat Cezan** — [github.com/muratcezan](http://github.com/muratcezan)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.
