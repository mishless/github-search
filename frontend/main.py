from bottle import *

static_path = "static/"


@get("/static/<filepath:path>")
def get_static(filepath):
    return static_file(filepath, root=static_path)


@get("/")
def get_index():
    return template("search.tpl")


@get("/search")
def get_search():
    query = request.query.query
    results = [
            {"title": "A result", "url": "http://www.github.com", "snippet": "print('Hello world!');"},
        {"title": "Another result", "url": "http://www.google.com"},
    ]

    return template("results.tpl", query=query, results=results)


debug(True)
run(host="localhost", port=8080, reloader=True)
