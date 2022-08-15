# encoding: utf-8

from random import random
from flask import render_template
import random

class MyLogic():


    def show_something():
        objects = ["Car", "Ship", "Plane"]
        return render_template("index.html", names=objects)


    def do_something(name):
        return "Welcome to ckan {}!".format(name)
    

    def help_it(num):
        return random.randint(num, num + 100)