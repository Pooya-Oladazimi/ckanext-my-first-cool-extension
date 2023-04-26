# encoding: utf-8

from random import random
from flask import render_template, request
import random
from datetime import datetime as _time
import ckan.plugins.toolkit as toolkit
import ckan.model as model
import ckan.logic as logic
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


    def only_admin_can_access_me():
        context = {'model': model,
                   'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}
        try:
            logic.check_access('sysadmin', context, {})
        except logic.NotAuthorized:
            toolkit.abort(403, 'Need to be system administrator to administer')
        
        dataset_id = request.form.get('dataset_id')
        return "Hello Admin with Dataset {}!".format(dataset_id)