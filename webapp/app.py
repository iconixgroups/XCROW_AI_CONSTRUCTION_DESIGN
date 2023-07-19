```python
from flask import Flask, render_template
from .api.routes import api_blueprint
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register the API blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project_setup')
def project_setup():
    return render_template('project_setup.html')

@app.route('/design_view')
def design_view():
    return render_template('design_view.html')

@app.route('/analysis_view')
def analysis_view():
    return render_template('analysis_view.html')

@app.route('/export_view')
def export_view():
    return render_template('export_view.html')

if __name__ == '__main__':
    app.run()
```