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

def search(query):
    q = Q("match_all")
    for token in query.split():
        tag, word = parse_token(token)
        if tag:
            if tag == "access":
                q = q & Q("match", access_modifier=word)
            elif tag == "returns":
                q = q & Q("match", return_type=word)
        else:
            q = q & Q("wildcard", method_name=f"*{word}*")
    print(q)

    s = Search(using=client, index="method").query(q).sort('token_count', 'cyclomatic_complexity')
    response = s.execute()
    return [result_from_hit(hit) for hit in response]

def result_from_hit(hit):
    format_string = "{hit.method_name}()"
    if hasattr(hit, 'return_type') and hit.return_type:
        format_string = "{hit.return_type[0]} " + format_string
    if hasattr(hit, 'access_modifier') and hit.access_modifier:
        format_string = "{hit.access_modifier} " + format_string
    return dict(title=format_string.format(hit=hit), url=hit.url, snippet="code goes here()")
      
def parse_token(token):
    if len(token) >= 3 and ':' in token[1:]:
        tag, word = token.split(':', maxsplit=1)
        return tag, word
    else:
        return None, token

