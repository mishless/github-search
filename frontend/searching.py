from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from elasticsearch_dsl import Q
from elasticsearch_dsl import Search

user = "z5dpiK4Pa6"
secret = "fWMSA56wUtoEa943jrhd"
host = "dd2476-8696942607.eu-central-1.bonsaisearch.net"
client = connections.create_connection(
    host=host, port=443, use_ssl=True, http_auth=(user, secret)
)
client.ping()

def search_class_properties(query):
    q = Q("match_all")
    tokens = query.split(' ')
    is_and = True
    for token in query.split(' '):
        if ":" not in token:
            if token == 'and':
                is_and = True
            else:
                is_and = False
        else:
            tag, word = token.split(':')
            print(tag, word)
            if tag == "class_name":
                q = q & Q("wildcard", class_name=word) if is_and else q | Q("wildcard", class_name=word)
            elif tag == "access_modifier":
                q = q & Q("wildcard", access_modifier=word) if is_and else q | Q("wildcard", access_modifier=word)
            elif tag == "is_abstract":
                q = q & Q("wildcard", is_abstract=word) if is_and else q | Q("wildcard", is_abstract=word)
            elif tag == "is_static":
                q = q & Q("wildcard", is_static=word) if is_and else q | Q("wildcard", is_static=word)
            elif tag == "is_final":
                q = q & Q("wildcard", is_final=word) if is_and else q | Q("wildcard", is_final=word)
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
    s = Search(using=client, index="class").query(q)
    response = s.execute()
    return [class_result_from_hit(hit) for hit in response]

def search(query):
    q = Q("match_all")
    for token in query.split():
        tag, word = parse_token(token)
        if tag:
            if tag == "method_name":
                q = q & Q("match", method_name=word)
            if tag == "access_modifier":
                q = q & Q("match", access_modifier=word)
            if tag == "returns":
                q = q & Q("match", return_type=word)
            if tag == "is_abstract":
                q = q & Q("match", is_abstract=word)
            if tag == "is_static":
                q = q & Q("match", is_static=word)
            if tag == "is_final":
                q = q & Q("match", is_final=word)
            if tag == "input_type":
                q = q & Q("match", input_type=word)
            if tag == "throws":
                q = q & Q("match", throws=word)
            if tag == "annotation":
                q = q & Q("match", annotation=word)
            if tag == "type_parameters":
                q = q & Q("match", type_parameters=word)
        else:
            q = q & Q("wildcard", method_name="*{}*".format(word))
    s = Search(using=client, index="method").query(q).sort('token_count', 'cyclomatic_complexity')
    response = s.execute()
    return [result_from_hit(hit) for hit in response]

def class_result_from_hit(hit):
    format_string = "{hit.class_name}()"
    if hasattr(hit, 'access_modifier') and hit.access_modifier:
        format_string = "{hit.access_modifier} " + format_string
    text = hit.words.split('\n')
    snippet = []
    i = hit.position.line - 1
    number_of_opening = 0
    number_of_closing = 0
    while True:
        snippet.append(text[i])
        number_of_opening += text[i].count('{')
        number_of_closing += text[i].count('}')
        if number_of_opening == number_of_closing:
            break
        i += 1
    return dict(title=format_string.format(hit=hit), url=hit.html_url, snippet=snippet)

def result_from_hit(hit):
    format_string = "{hit.method_name}()"
    if hasattr(hit, 'return_type') and hit.return_type:
        format_string = "{hit.return_type[0]} " + format_string
    if hasattr(hit, 'access_modifier') and hit.access_modifier:
        format_string = "{hit.access_modifier} " + format_string
    text = hit.words.split('\n')
    snippet = []
    i = hit.position.line - 1
    number_of_opening = 0
    number_of_closing = 0
    while True:
        snippet.append(text[i])
        number_of_opening += text[i].count('{')
        number_of_closing += text[i].count('}')
        if number_of_opening == number_of_closing:
            break
        i += 1
    return dict(title=format_string.format(hit=hit), url=hit.html_url, snippet=snippet)

def parse_token(token):
    if len(token) >= 3 and ':' in token[1:]:
        tag, word = token.split(':', maxsplit=1)
        return tag, word
    else:
        return None, token
