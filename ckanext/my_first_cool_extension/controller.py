# encoding: utf-8

from flask import render_template

class MyLogic():


    def show_something():
        objects = ["Car", "Ship", "Plane"]
        return render_template("index.html", names=objects)


    def do_something(name):
        return "Welcome to ckan {}!".format(name)