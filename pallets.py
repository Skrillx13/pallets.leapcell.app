from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages, pygments_style_defs
import os

# Import configuration
from config import Config

app = Flask(__name__, static_folder='assets')
app.config.from_object(Config)
flatpages = FlatPages(app)

@app.route('/')
def index():
    content = flatpages.get_or_404('index')
    return render_template('index.html', content=content, meta=content.meta)

@app.route('/<path:path>/')
def page(path):
    content = flatpages.get_or_404(path)
    template = content.meta.get('template', 'page.html')
    return render_template(template, content=content, meta=content.meta)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('default'), 200, {'Content-Type': 'text/css'}

if __name__ == '__main__':
    app.run(debug=True)