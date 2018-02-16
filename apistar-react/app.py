from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls

import views

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

routes = [
    Route('/', 'GET', views.hello),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
settings = {
    'TEMPLATES': {
        'ROOT_DIR': 'templates',     # Include the 'templates/' directory.
        'PACKAGE_DIRS': ['apistar']  # Include the built-in apistar templates.
    },
    'INSTALLED_APPS': ['webpack']
}

app = App(routes=routes, settings=settings)

if __name__ == '__main__':
    app.main()
