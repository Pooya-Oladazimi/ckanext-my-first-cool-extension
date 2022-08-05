import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class MySecondPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates/second_plugin')
        toolkit.add_public_directory(config_, 'public/second_plugin')
    
