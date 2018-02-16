import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    'INSTALLED_APPS': ['webpack_loader'],
    'TEMPLATES': {
        'ROOT_DIR': 'templates',     # Include the 'templates/' directory.
        'PACKAGE_DIRS': ['apistar']  # Include the built-in apistar templates.
    },
}