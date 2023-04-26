import pytest
import ckan.tests.factories as factories
import ckan.lib.helpers as h
import ckan.model as model
import ckan.lib.create_test_data as ctd


@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')
class TestCoolPlugin(object):    
    @pytest.fixture(autouse=True)
    def initial(self):
        ctd.CreateTestData.create()
        self.sysadmin_user = model.User.get("testsysadmin")
        self.post_data = {}
        self.dest_url = h.url_for('my_cool_new_plugin.only_admin_can_access_me')


    def test_with_not_admin_user(self, app):       
        user = factories.User()
        owner_org = factories.Organization(users=[{
            'name': user['id'],
            'capacity': 'member'
        }])
        dataset = factories.Dataset(owner_org=owner_org['id'])       
        self.post_data['dataset_id'] = dataset['id']                
        response = app.post(self.dest_url, data=self.post_data)        
        assert "You need to authenticate before accessing this function" in response.body

    
    def test_with_admin_user(self, app):       
        owner_org = factories.Organization(users=[{
            'name': self.sysadmin_user.id,
            'capacity': 'member'
        }])
        dataset = factories.Dataset(owner_org=owner_org['id'])         
        self.post_data['dataset_id'] = dataset['id']                             
        auth = {u"Authorization": str(self.sysadmin_user.apikey)}
        response = app.post(self.dest_url, data=self.post_data , extra_environ=auth)           
        assert response.status_code == 200        
