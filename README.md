# ckanext-my-first-cool-extension

The sample plugin and extension for a tutorial about how can we develop a ckan plugin.


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8 and earlier | No    |
| 2.9             | Yes    |


## Installation


To install ckanext-my-first-cool-extension:

1. Activate your CKAN virtual environment, for example:

        . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

        git clone https://github.com//ckanext-my-first-cool-extension.git
        cd ckanext-my-first-cool-extension
        pip install -e .
        pip install -r requirements.txt
        python setup.py develop

3. Add `my_cool_new_plugin` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service supervisor reload
        sudo service apache2 reload


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
