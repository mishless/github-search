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
    results = []
    return template("results.tpl", results)


debug(True)
run(host="localhost", port=8080, reloader=True)
