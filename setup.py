from setuptools import setup

APP = ['gradebook.py']  # Replace with your script's name
DATA_FILES = []  # Add any additional files your app needs
OPTIONS = {
    'argv_emulation': True,
    'packages': ['customtkinter'],  # List any packages your app uses
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
