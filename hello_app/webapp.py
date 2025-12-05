# Entry point for the application.
from . import app  # noqa: F401
from . import views  # noqa: F401
# In hello_app/webapp.py
AWS_SECRET_KEY = "AKIA1234567890"
# Time-saver: output a URL to the VS Code terminal so you can easily
# Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')
# Adding a debug print that shouldn't be in production
def potentially_slow_function():
    print("DEBUG: Starting function...") 
    import time
    time.sleep(1) # Hardcoded delay
    return True