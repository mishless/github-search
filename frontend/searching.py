from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from elasticsearch_dsl import Q
from elasticsearch_dsl import Search

host = "albert.lundstig.com"
client = connections.create_connection(
    host=host, port=9200
)
client.ping()

per_page = 10

def search_class_properties(query, page, sort):
    q = Q("match_all")
    tokens = query.split(' ')
    is_and = True
    queries = []
    query_arr = ['and']
    for token in query.split(' '):
        if ":" not in token:
            query_arr.append(token)
            if token == 'and':
                is_and = True
            else:
                is_and = False
        else:
            tag, word = token.split(':')
            query_arr.append(tag)
            query_arr.append(word)
            queries.append(query_arr)
            query_arr = []
            if tag == "class_name":
                q = q & Q("wildcard", class_name=word) if is_and else q | Q("wildcard", class_name=word)
            elif tag == "access_modifier":
                q = q & Q("wildcard", access_modifier=word) if is_and else q | Q("wildcard", access_modifier=word)
            elif tag == "is_abstract":
                q = q & Q("match", is_abstract=word) if is_and else q | Q("match", is_abstract=word)
            elif tag == "is_static":
                q = q & Q("match", is_static=word) if is_and else q | Q("match", is_static=word)
            elif tag == "is_final":
                q = q & Q("match", is_final=word) if is_and else q | Q("match", is_final=word)
            elif tag == "annotation":
                q = q & Q("wildcard", annotation=word) if is_and else q | Q("wildcard", annotation=word)
            elif tag == "extends_class":
                q = q & Q("wildcard", extends_class=word) if is_and else q | Q("wildcard", extends_class=word)
            elif tag == "implements_interfaces":
                q = q & Q("wildcard", implements_interfaces=word) if is_and else q | Q("wildcard", implements_interfaces=word)
            elif tag == "imports":
                q = q & Q("wildcard", imports=word) if is_and else q | Q("wildcard", imports=word)
            elif tag == "package":
                q = q & Q("wildcard", package=word) if is_and else q | Q("wildcard", package=word)
    if ":" in sort:
        sort_arr = sort.split(":")
        search = Search(using=client, index="class").query(q).sort({sort_arr[0] : {"order" : sort_arr[1]}})
    else:
        search = Search(using=client, index="class").query(q)
    total = search.count()
    max_pages = total // per_page
    search = search[(page - 1) * per_page : page * per_page]
    response = search.execute()
    return [result_from_hit(hit, 'class') for hit in response], queries,  max_pages + 1, total

def search_interface_properties(query, page, sort):
    q = Q("match_all")
    tokens = query.split(' ')
    is_and = True
    queries = []
    query_arr = ['and']
    for token in query.split(' '):
        if ":" not in token:
            query_arr.append(token)
            if token == 'and':
                is_and = True
            else:
                is_and = False
        else:
            tag, word = token.split(':')
            query_arr.append(tag)
            query_arr.append(word)
            queries.append(query_arr)
            query_arr = []
            if tag == "interface_name":
                q = q & Q("wildcard", interface_name=word) if is_and else q | Q("wildcard", interface_name=word)
            elif tag == "access_modifier":
                q = q & Q("wildcard", access_modifier=word) if is_and else q | Q("wildcard", access_modifier=word)
            elif tag == "annotation":
                q = q & Q("wildcard", annotation=word) if is_and else q | Q("wildcard", annotation=word)
            elif tag == "implements_interfaces":
                q = q & Q("wildcard", implements_interfaces=word) if is_and else q | Q("wildcard", implements_interfaces=word)
            elif tag == "imports":
                q = q & Q("wildcard", imports=word) if is_and else q | Q("wildcard", imports=word)
            elif tag == "package":
                q = q & Q("wildcard", package=word) if is_and else q | Q("wildcard", package=word)
    if ":" in sort:
        sort_arr = sort.split(":")
        search = Search(using=client, index="interface").query(q).sort({sort_arr[0] : {"order" : sort_arr[1]}})
    else:
        search = Search(using=client, index="interface").query(q)
    total = search.count()
    max_pages = total // per_page
    search = search[(page - 1) * per_page : page * per_page]
    response = search.execute()
    return [result_from_hit(hit, 'interface') for hit in response], queries,  max_pages + 1, total

def search_enum_properties(query, page, sort):
    q = Q("match_all")
    tokens = query.split(' ')
    is_and = True
    queries = []
    query_arr = ['and']
    for token in query.split(' '):
        if ":" not in token:
            query_arr.append(token)
            if token == 'and':
                is_and = True
            else:
                is_and = False
        else:
            tag, word = token.split(':')
            query_arr.append(tag)
            query_arr.append(word)
            queries.append(query_arr)
            query_arr = []
            if tag == "enum_name":
                q = q & Q("wildcard", enum_name=word) if is_and else q | Q("wildcard", enum_name=word)
            elif tag == "access_modifier":
                q = q & Q("wildcard", access_modifier=word) if is_and else q | Q("wildcard", access_modifier=word)
            elif tag == "constants":
                q = q & Q("wildcard", constants=word) if is_and else q | Q("wildcard", constants=word)
            elif tag == "annotation":
                q = q & Q("wildcard", annotation=word) if is_and else q | Q("wildcard", annotation=word)
            elif tag == "implements_interfaces":
                q = q & Q("wildcard", implements_interfaces=word) if is_and else q | Q("wildcard", implements_interfaces=word)
            elif tag == "imports":
                q = q & Q("wildcard", imports=word) if is_and else q | Q("wildcard", imports=word)
            elif tag == "package":
                q = q & Q("wildcard", package=word) if is_and else q | Q("wildcard", package=word)
    if ":" in sort:
        sort_arr = sort.split(":")
        search = Search(using=client, index="enum").query(q).sort({sort_arr[0] : {"order" : sort_arr[1]}})
    else:
        search = Search(using=client, index="enum").query(q)
    total = search.count()
    max_pages = total // per_page
    search = search[(page - 1) * per_page : page * per_page]
    response = search.execute()
    return [result_from_hit(hit, 'enum') for hit in response], queries,  max_pages + 1, total

def search_method_properties(query, page, sort):
    q = Q("match_all")
    tokens = query.split(' ')
    is_and = True
    queries = []
    query_arr = ['and']
    for token in query.split(' '):
        if ":" not in token:
            query_arr.append(token)
            if token == 'and':
                is_and = True
            else:
                is_and = False
        else:
            tag, word = token.split(':')
            query_arr.append(tag)
            query_arr.append(word)
            queries.append(query_arr)
            query_arr = []
            if tag == "method_name":
                q = q & Q("wildcard", method_name=word) if is_and else q | Q("wildcard", method_name=word)
            elif tag == "access_modifier":
                q = q & Q("wildcard", access_modifier=word) if is_and else q | Q("wildcard", access_modifier=word)
            elif tag == "is_abstract":
                q = q & Q("match", is_abstract=word) if is_and else q | Q("match", is_abstract=word)
            elif tag == "is_static":
                q = q & Q("match", is_static=word) if is_and else q | Q("match", is_static=word)
            elif tag == "is_final":
                q = q & Q("match", is_final=word) if is_and else q | Q("match", is_final=word)
            elif tag == "return_type":
                q = q & Q("wildcard", return_type=word) if is_and else q | Q("wildcard", return_type=word)
            elif tag == "annotation":
                q = q & Q("wildcard", annotation=word) if is_and else q | Q("wildcard", annotation=word)
            elif tag == "input_type":
                q = q & Q("wildcard", input_type=word) if is_and else q | Q("wildcard", input_type=word)
            elif tag == "throws":
                q = q & Q("wildcard", throws=word) if is_and else q | Q("wildcard", throws=word)
    if ":" in sort:
        sort_arr = sort.split(":")
        search = Search(using=client, index="method").query(q).sort({sort_arr[0] : {"order" : sort_arr[1]}})
    else:
        search = Search(using=client, index="method").query(q)
    total = search.count()
    max_pages = total // per_page
    search = search[(page - 1) * per_page : page * per_page]
    response = search.execute()
    return [result_from_hit(hit, 'method') for hit in response], queries,  max_pages + 1, total

def search_variable_properties(query, page, sort):
    q = Q("match_all")
    tokens = query.split(' ')
    is_and = True
    queries = []
    query_arr = ['and']
    for token in query.split(' '):
        if ":" not in token:
            query_arr.append(token)
            if token == 'and':
                is_and = True
            else:
                is_and = False
        else:
            tag, word = token.split(':')
            query_arr.append(tag)
            query_arr.append(word)
            queries.append(query_arr)
            query_arr = []
            if tag == "variable_name":
                q = q & Q("wildcard", variable_name=word) if is_and else q | Q("wildcard", variable_name=word)
            elif tag == "access_modifier":
                q = q & Q("wildcard", access_modifier=word) if is_and else q | Q("wildcard", access_modifier=word)
            elif tag == "variable_type":
                q = q & Q("wildcard", variable_type=word) if is_and else q | Q("wildcard", variable_type=word)
            elif tag == "is_static":
                q = q & Q("match", is_static=word) if is_and else q | Q("match", is_static=word)
            elif tag == "is_final":
                q = q & Q("match", is_final=word) if is_and else q | Q("match", is_final=word)
            elif tag == "annotation":
                q = q & Q("wildcard", annotation=word) if is_and else q | Q("wildcard", annotation=word)
    if ":" in sort:
        sort_arr = sort.split(":")
        search = Search(using=client, index="variable").query(q).sort({sort_arr[0] : {"order" : sort_arr[1]}})
    else:
        search = Search(using=client, index="variable").query(q)
    total = search.count()
    max_pages = total // per_page
    search = search[(page - 1) * per_page : page * per_page]
    response = search.execute()
    return [result_from_hit(hit, 'variable') for hit in response], queries,  max_pages + 1, total

def search(query, page, sort):
    q = Q("match_all")
    word = query
    if word[0] == '"' and word[-1] == '"':
        q = q & Q("match_phrase", words="{}".format(word))
    else:
        words = word.split(' ')
        for w in words:
            q = q & Q("wildcard", words="{}".format(w))
    if ":" in sort:
        sort_arr = sort.split(":")
        search = Search(using=client, index="file").query(q).sort({sort_arr[0] : {"order" : sort_arr[1]}})
    else:
        search = Search(using=client, index="file").query(q)
    total = search.count()
    max_pages = total // per_page
    search = search[(page - 1) * per_page : page * per_page]
    response = search.execute()
    return [file_result_from_hit(hit) for hit in response], max_pages + 1, total

def file_result_from_hit(hit):
    format_string = "{hit.owner}/{hit.repository_name} - {hit.file_name}"
    text = hit.words.split('\n')
    return dict(title=format_string.format(hit=hit), url=hit.html_url, snippet=text, stars_count=hit.stargazers_count, issues_count=hit.open_issues_count)

def result_from_hit(hit, index):
    format_string = "{hit.owner}/{hit.repository_name} - {hit.file_name}"
    text = hit.words.split('\n')
    snippet = []
    i = hit.position.line - 1
    number_of_opening = 0
    number_of_closing = 0
    if index == 'class' or index == 'enum' or index == 'interface':
        for j in range(0, i):
            snippet.append(text[j])
    else:
        for j in range(len(hit.annotation), 0, -1):
            snippet.append(text[i-j])
    while i < len(text):
        snippet.append(text[i])
        #Stop if this is just a function declaration
        if i == hit.position.line - 1 and text[i][-1] == ";":
            break
        if index == 'variable':
            number_of_opening += text[i].count('(')
            number_of_closing += text[i].count(')')
            if (number_of_opening == number_of_closing and number_of_opening > 0):
                break
        else:
            number_of_opening += text[i].count('{')
            number_of_closing += text[i].count('}')
            if (number_of_opening == number_of_closing and number_of_opening > 0):
                break
        i += 1
    return dict(title=format_string.format(hit=hit), url=hit.html_url, snippet=snippet, stars_count=hit.stargazers_count, issues_count=hit.open_issues_count)

def parse_token(token):
    if len(token) >= 3 and ':' in token[1:]:
        tag, word = token.split(':', maxsplit=1)
        return tag, word
    else:
        return None, token
