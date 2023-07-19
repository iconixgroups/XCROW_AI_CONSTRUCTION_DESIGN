```python
import json
from datetime import datetime

class Analytics:

    def __init__(self):
        self.data = {
            'projectData': [],
            'userData': [],
            'designData': [],
            'analysisData': []
        }

    def log_project_data(self, projectData):
        projectData['timestamp'] = str(datetime.now())
        self.data['projectData'].append(projectData)

    def log_user_data(self, userData):
        userData['timestamp'] = str(datetime.now())
        self.data['userData'].append(userData)

    def log_design_data(self, designData):
        designData['timestamp'] = str(datetime.now())
        self.data['designData'].append(designData)

    def log_analysis_data(self, analysisData):
        analysisData['timestamp'] = str(datetime.now())
        self.data['analysisData'].append(analysisData)

    def export_logs(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f)

analytics = Analytics()
```