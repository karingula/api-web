from apistar import Response, annotate, render_template, http
from apistar.renderers import HTMLRenderer, JSONRenderer
from apistar.interfaces import Templates

@annotate(renderers=[HTMLRenderer()])
def hello(username: str, templates: Templates) -> Response:
    sports_data = [
                {'category': "Sporting Goods", 'price': "$49.99", 'stocked': 'true', 'name': "Football"},
                {'category': "Sporting Goods", 'price': "$9.99", 'stocked': 'true', 'name': "Baseball"},
                {'category': "Sporting Goods", 'price': "$29.99", 'stocked': 'false', 'name': "Basketball"},
                {'category': "Electronics", 'price': "$99.99", 'stocked': 'true', 'name': "iPod Touch"},
                {'category': "Electronics", 'price': "$399.99", 'stocked': 'false', 'name': "iPhone 5"},
                {'category': "Electronics", 'price': "$199.99", 'stocked': 'true', 'name': "Nexus 7"}
    ];
    #output={'name': 'maseratti', 'country': 'malta'}
    index = templates.get_template('index.html')
    # -- valid below two statements --
    #return render_template('index.html', output=output)
    return index.render(output=sports_data)

    #-- invalid below statement --
    #return http.Response(content, content_type='text/html')
