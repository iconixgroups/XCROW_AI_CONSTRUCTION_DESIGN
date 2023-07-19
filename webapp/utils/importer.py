```python
import json
from webapp.api.models import UserSchema, ProjectSchema, DesignSchema, AnalysisSchema

def import_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        userData = UserSchema().load(data.get('userData', {}))
        projectData = ProjectSchema().load(data.get('projectData', {}))
        designData = DesignSchema().load(data.get('designData', {}))
        analysisData = AnalysisSchema().load(data.get('analysisData', {}))

        return userData, projectData, designData, analysisData

    except Exception as e:
        print(f"Error occurred while importing data: {str(e)}")
        return None
```