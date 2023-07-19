```python
import unittest
from webapp.api import app, db
from webapp.api.models import User, Project, Design, Analysis

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_project_creation(self):
        response = self.app.post('/api/project', data=dict(
            projectData='Test Project Data'
        ))
        self.assertEqual(response.status_code, 200)

    def test_design_generation(self):
        response = self.app.post('/api/design', data=dict(
            designData='Test Design Data'
        ))
        self.assertEqual(response.status_code, 200)

    def test_analysis_completion(self):
        response = self.app.post('/api/analysis', data=dict(
            analysisData='Test Analysis Data'
        ))
        self.assertEqual(response.status_code, 200)

    def test_data_export(self):
        response = self.app.get('/api/export')
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        response = self.app.post('/api/user', data=dict(
            userData='Test User Data'
        ))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

if __name__ == "__main__":
    unittest.main()
```