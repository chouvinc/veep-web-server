import os
import unittest

from app import app, db

TEST_DB = 'test.db'
'''
To run tests on local machine, run "python -m unittest discover" at the root directory
'''
class BasicTests(unittest.TestCase):
    def setup(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        # Disable sending emails during unit testing
        #mail.init_app(app)
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_projects_page(self):
        self.app = app.test_client()
        response = self.app.get('/projects', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_our_team_page(self):
        self.app = app.test_client()
        response = self.app.get('/our_team', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        self.app = app.test_client()
        response = self.app.get('/contact_us', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_events_page(self):
        self.app = app.test_client()
        response = self.app.get('/events', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_sanity(self):
        self.assertEqual(1, 1)

    

