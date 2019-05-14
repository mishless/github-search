from bottle import *
import searching

static_path = "static/"

@get("/static/<filepath:path>")
def get_static(filepath):
    return static_file(filepath, root=static_path)

@get("/")
def get_index():
    return template("search.tpl", query="", base="", queries=None, sort=None, index='code')

@get("/search")
def get_search():
    query = request.query.query or ""
    page = int(request.query.page)
    sort = request.query.sort
    results, max_pages, total_results = searching.search(query, page, sort)
    return template("results.tpl", query=query, results=results, queries=None, sort=sort, index='code', max_pages=max_pages, page=page, total_results=total_results)

@get("/search-class-properties")
def get_search_class_properties():
    query = request.query.class_query or ""
    page = int(request.query.page)
    sort = request.query.sort
    results, queries, max_pages, total_results = searching.search_class_properties(query, page, sort)
    return template("results.tpl", query="", results=results, queries=queries, sort=sort, index='class', max_pages=max_pages, page=page, total_results=total_results)

@get("/search-interface-properties")
def get_search_class_properties():
    query = request.query.interface_query or ""
    page = int(request.query.page)
    sort = request.query.sort
    results, queries, max_pages, total_results = searching.search_interface_properties(query, page, sort)
    return template("results.tpl", query="", results=results, queries=queries, sort=sort, index='interface', max_pages=max_pages, page=page, total_results=total_results)

@get("/search-enum-properties")
def get_search_class_properties():
    query = request.query.enum_query or ""
    page = int(request.query.page)
    sort = request.query.sort
    results, queries, max_pages, total_results = searching.search_enum_properties(query, page, sort)
    return template("results.tpl", query="", results=results, queries=queries, sort=sort, index='enum', max_pages=max_pages, page=page, total_results=total_results)

@get("/search-method-properties")
def get_search_class_properties():
    query = request.query.method_query or ""
    page = int(request.query.page)
    sort = request.query.sort
    results, queries, max_pages, total_results = searching.search_method_properties(query, page, sort)
    return template("results.tpl", query="", results=results, queries=queries, sort=sort, index='method', max_pages=max_pages, page=page, total_results=total_results)

@get("/search-variable-properties")
def get_search_class_properties():
    query = request.query.variable_query or ""
    page = int(request.query.page)
    sort = request.query.sort
    results, queries, max_pages, total_results = searching.search_variable_properties(query, page, sort)
    return template("results.tpl", query="", results=results, queries=queries, sort=sort, index='variable', max_pages=max_pages, page=page, total_results=total_results)

debug(True)
run(host="localhost", port=8080, reloader=True, quiet=True)
