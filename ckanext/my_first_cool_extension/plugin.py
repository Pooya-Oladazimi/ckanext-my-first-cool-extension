import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint
from ckanext.my_first_cool_extension.controller import MyLogic


class MyCoolPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates/cool_temp')
        toolkit.add_public_directory(config_, 'public/cool_static')
        toolkit.add_resource('public/cool_static', 'ckanext-cool-plugin')
    

    def get_blueprint(self):

        blueprint = Blueprint(self.name, self.__module__)        
       
        blueprint.add_url_rule(
            u'/cool_plugin/do_something/<name>',
            u'do_something',
            MyLogic.do_something,
            methods=['GET']
        )

        blueprint.add_url_rule(
            u'/cool_plugin/add',
            u'add',
            MyLogic.add,
            methods=['GET']
        )

        blueprint.add_url_rule(
            u'/cool_plugin/get',
            u'get',
            MyLogic.get,
            methods=['GET']
        )

        blueprint.add_url_rule(
            u'/cool_plugin/update',
            u'update',
            MyLogic.update,
            methods=['GET']
        )

        blueprint.add_url_rule(
            u'/cool_plugin/delete',
            u'delete',
            MyLogic.delete,
            methods=['GET']
        )

        blueprint.add_url_rule(
            u'/cool_plugin/do_something/<name>',
            u'do_something',
            MyLogic.do_something,
            methods=['GET']
        )


        return blueprint
    

    #ITemplateHelpers

    def get_helpers(self):
        return {'help_me': MyLogic.help_it}
