# encoding: utf-8

from random import random
from flask import render_template
import random
from datetime import datetime as _time
from ckanext.my_first_cool_extension.models.cool_plugin_table import CoolPluginTable

class MyLogic():


    def show_something():
        objects = ["Car", "Ship", "Plane"]
        return render_template("index.html", names=objects)


    def do_something(name):
        return "Welcome to ckan {}!".format(name)
    

    def help_it(num):
        return random.randint(num, num + 100)
    
    def add():
        db_model = CoolPluginTable(
            random_number=random.randint(1, 10000),
            name="random thing",
            dataset_name="test-dataset",
            created_at= _time.now()
        )

        db_model.save()

        return "Success!"
    

    def get():
        dataset = "test-dataset"
        result = CoolPluginTable().get_by_package(name=dataset)

        return str(result[0].random_number)
    

    def update():
        dataset = "test-dataset"
        result = CoolPluginTable().get_by_package(name=dataset)
        for res in result:
            res.random_number=random.randint(1, 10000)
            res.commit()
        
        return "Success!"
    

    def delete():
        dataset = "test-dataset"
        result = CoolPluginTable().get_by_package(name=dataset)
        for res in result:
            res.random_number=random.randint(1, 10000)
            res.delete()
            res.commit()
        
        return "Success!"