from bottle import *
import searching

static_path = "static/"


@get("/static/<filepath:path>")
def get_static(filepath):
    return static_file(filepath, root=static_path)


@get("/")
def get_index():
    return template("search.tpl", query="", base="")


@get("/search")
def get_search():
    query = request.query.query or ""
    results = searching.search(query)
    return template("results.tpl", query=query, results=results)


debug(True)
run(host="localhost", port=8080, reloader=True, quiet=True)
