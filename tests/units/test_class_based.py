from cbfa import ClassBased


class PseudoApp:
    def __init__(self):
        self.calls = []

    def get(self, url):
        self.calls.append(('get', url))
        return lambda x: x
    def post(self, url):
        self.calls.append(('post', url))
        return lambda x: x
    def put(self, url):
        self.calls.append(('put', url))
        return lambda x: x
    def delete(self, url):
        self.calls.append(('delete', url))
        return lambda x: x
    def trace(self, url):
        self.calls.append(('trace', url))
        return lambda x: x
    def head(self, url):
        self.calls.append(('head', url))
        return lambda x: x
    def options(self, url):
        self.calls.append(('options', url))
        return lambda x: x
    def connect(self, url):
        self.calls.append(('connect', url))
        return lambda x: x
    def patch(self, url):
        self.calls.append(('patch', url))
        return lambda x: x


def test_wrap_only_get():
    app = PseudoApp()
    wrapper = ClassBased(app)

    @wrapper('/kek')
    class SomeItem:
        def get():
            pass

    assert app.calls == [('get', '/kek')]


def test_wrap_all():
    url = '/kek'
    app = PseudoApp()
    wrapper = ClassBased(app)

    @wrapper(url)
    class SomeItem:
        def get():
            pass
        def post():
            pass
        def put():
            pass
        def delete():
            pass
        def trace():
            pass
        def head():
            pass
        def options():
            pass
        def connect():
            pass
        def patch():
            pass

    assert app.calls == [('get', url), ('post', url), ('put', url), ('delete', url), ('trace', url), ('head', url), ('options', url), ('connect', url), ('patch', url)]
