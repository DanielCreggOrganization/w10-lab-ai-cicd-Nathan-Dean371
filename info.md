# Python Flask CI/CD Lab Application

## Overview

This repository contains a Python Flask web application designed for a CI/CD lab. The application demonstrates continuous integration practices and automated testing workflows using GitHub Actions.

## Application Details

This is a simple Flask web application with the following features:
- Home page route
- About and Contact pages
- Modular Flask app structure

## Requirements

To run this application, you need Python 3.12 or higher. The required Python packages are listed in `requirements.txt`:
- Flask (web framework)
- flake8 (linting)
- pytest (testing framework)

## Installation Instructions

1. **Clone the repository** (if not already cloned):
   ```bash
   git clone <repository-url>
   cd w10-lab-ai-cicd-Nathan-Dean371
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application locally:

```bash
python3 -m flask --app startup run
```

The application will start on `http://127.0.0.1:5000/`. You can access it in your browser at that address.

To stop the application, press `Ctrl+C` in the terminal.

## Running Tests

This project uses pytest for testing. To run all tests:

```bash
python -m pytest
```

To run tests with verbose output:

```bash
python -m pytest -v
```

To run a specific test file:

```bash
python -m pytest tests/test_app.py
```

## Linting

To check the code quality with flake8:

```bash
flake8 .
```

## CI/CD Pipeline

This repository includes GitHub Actions workflows for continuous integration:
- Automated testing on push to main branch
- Code linting with flake8
- Python version: 3.12

Check the `.github/workflows/` directory for workflow configurations.
