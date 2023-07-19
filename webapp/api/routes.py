```python
from flask import Blueprint, request
from .controllers import setupProject, generateDesign, analyzeDesign, exportData, importData

api = Blueprint('api', __name__)

@api.route('/setupProject', methods=['POST'])
def route_setupProject():
    projectData = request.get_json()
    return setupProject(projectData)

@api.route('/generateDesign', methods=['POST'])
def route_generateDesign():
    projectData = request.get_json()
    return generateDesign(projectData)

@api.route('/analyzeDesign', methods=['POST'])
def route_analyzeDesign():
    designData = request.get_json()
    return analyzeDesign(designData)

@api.route('/exportData', methods=['POST'])
def route_exportData():
    projectData = request.get_json()
    return exportData(projectData)

@api.route('/importData', methods=['POST'])
def route_importData():
    importData = request.get_json()
    return importData(importData)
```