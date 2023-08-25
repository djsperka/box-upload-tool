'''
Created on Aug 21, 2023

@author: dan
'''
# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return render_template("home.html")

if __name__ == '__main__':  # Script executed directly?
    app.run()  # Launch built-in web server and run this Flask webapp