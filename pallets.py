from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
import os

# Import configuration
from config import Config

app = Flask(__name__, static_folder='assets')
app.config.from_object(Config)
flatpages = FlatPages(app)
freezer = Freezer(app)

def get_template_name(template):
    """Ensure the template has a .html extension"""
    if not template.endswith('.html'):
        template += '.html'
    return template

@app.route('/')
def index():
    content = flatpages.get_or_404('index')
    return render_template('index.html', content=content, meta=content.meta, base_url=app.config['BASE_URL'])

@app.route('/<path:path>/')
def page(path):
    content = flatpages.get_or_404(path)
    template = get_template_name(content.meta.get('template', 'page'))
    return render_template(template, content=content, meta=content.meta, base_url=app.config['BASE_URL'])

@freezer.register_generator
def page_url_generator():
    for page in flatpages:
        yield 'page', {'path': page.path}

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('default'), 200, {'Content-Type': 'text/css'}

if __name__ == '__main__':
    app.run(debug=True)