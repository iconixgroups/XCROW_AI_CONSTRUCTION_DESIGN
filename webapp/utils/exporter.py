```python
import os
from flask import send_file

def export_data(projectData, designData, analysisData):
    try:
        # Export project data
        with open('exports/projectData.txt', 'w') as file:
            file.write(str(projectData))

        # Export design data
        with open('exports/designData.txt', 'w') as file:
            file.write(str(designData))

        # Export analysis data
        with open('exports/analysisData.txt', 'w') as file:
            file.write(str(analysisData))

        return True
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")
        return False

def download_export(file_name):
    try:
        return send_file(os.path.join('exports', file_name), as_attachment=True)
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")
        return None
```