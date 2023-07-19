```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'dwg', 'dxf', 'stl'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    AI_ENGINE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ai_engine')
    ANALYTICS_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'analytics')
```