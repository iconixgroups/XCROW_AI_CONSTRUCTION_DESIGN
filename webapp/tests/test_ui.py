import unittest
from selenium import webdriver

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_project_setup_form(self):
        self.driver.get('http://localhost:5000/project_setup')
        project_setup_form = self.driver.find_element_by_id('projectSetupForm')
        self.assertIsNotNone(project_setup_form)

    def test_design_view_container(self):
        self.driver.get('http://localhost:5000/design_view')
        design_view_container = self.driver.find_element_by_id('designViewContainer')
        self.assertIsNotNone(design_view_container)

    def test_analysis_view_container(self):
        self.driver.get('http://localhost:5000/analysis_view')
        analysis_view_container = self.driver.find_element_by_id('analysisViewContainer')
        self.assertIsNotNone(analysis_view_container)

    def test_export_view_container(self):
        self.driver.get('http://localhost:5000/export_view')
        export_view_container = self.driver.find_element_by_id('exportViewContainer')
        self.assertIsNotNone(export_view_container)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()