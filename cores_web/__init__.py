# Code in this file is run when the cores_web package is imported, so this is the place to do initialization,
# configuration, etc.

from flask import Flask


app = Flask(__name__.split('.')[0])

# Apply the configuration values in config.py
app.config.from_object('cores_web.config')

# Load the URL routes
from cores_web import routes
