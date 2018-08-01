#!/usr/bin/python

import time
from flask import Flask
import re


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World! Python Running also con working.\n'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
