import os
import base64
import re
import logging
import config
from elasticsearch import Elasticsearch

file_properties = {
    "properties": {
        "id": {
            "type": "long"
        },
        "owner": {
            "type": "keyword"
        },
        "created_at": {
            "type": "date"
        },
        "description": {
            "type": "text"
        },
        "repository_name": {
            "type": "text"
        },
        "html_url": {
            "type": "keyword"
        },
        "open_issues_count": {
            "type": "integer"
        },
        "pushed_at": {
            "type": "date"
        },
        "stargazers_count": {
            "type": "integer"
        },
        "file_name": {
            "type": "keyword"
        },
        "words": {
            "type": "text"
        }
    }
}
interface_properties = {
    "properties": {
        "id": {
            "type": "long"
        },
        "owner": {
            "type": "keyword"
        },
        "created_at": {
            "type": "date"
        },
        "description": {
            "type": "text"
        },
        "repository_name": {
            "type": "text"
        },
        "html_url": {
            "type": "keyword"
        },
        "open_issues_count": {
            "type": "integer"
        },
        "pushed_at": {
            "type": "date"
        },
        "stargazers_count": {
            "type": "integer"
        },
        "file_name": {
            "type": "keyword"
        },
        "words": {
            "type": "text"
        },
        "interface_name": {
            "type": "text"
        },
        "access_modifier": {
            "type": "keyword"
        },
        "implements_interfaces": {
            "type": "keyword"
        },
        "imports": {
            "type": "keyword"
        },
        "package": {
            "type": "keyword"
        },
        "position": {
            "type": "nested",
            "properties": {
                "line": {
                    "type": "integer"
                },
                "row": {
                    "type": "integer"
                }
            }
        },
        "type_parameters": {
            "type": "nested",
            "properties": {
                "extends": {
                    "type": "keyword"
                },
                "name": {
                    "type": "keyword"
                }
            }
        },
        "annotation": {
            "type": "text"
        }
    }
}
enum_properties = {
    "properties": {
        "id": {
            "type": "long"
        },
        "owner": {
            "type": "keyword"
        },
        "created_at": {
            "type": "date"
        },
        "description": {
            "type": "text"
        },
        "repository_name": {
            "type": "text"
        },
        "html_url": {
            "type": "keyword"
        },
        "open_issues_count": {
            "type": "integer"
        },
        "pushed_at": {
            "type": "date"
        },
        "stargazers_count": {
            "type": "integer"
        },
        "file_name": {
            "type": "keyword"
        },
        "words": {
            "type": "text"
        },
        "enum_name": {
            "type": "text"
        },
        "access_modifier": {
            "type": "keyword"
        },
        "constants": {
            "type": "keyword"
        },
        "implements_interfaces": {
            "type": "keyword"
        },
        "imports": {
            "type": "keyword"
        },
        "package": {
            "type": "keyword"
        },
        "annotation": {
            "type": "text"
        },
        "position": {
            "type": "nested",
            "properties": {
                "line": {
                    "type": "integer"
                },
                "row": {
                    "type": "integer"
                }
            }
        }
    }
}
class_properties = {
    "properties": {
        "id": {
            "type": "long"
        },
        "owner": {
            "type": "keyword"
        },
        "created_at": {
            "type": "date"
        },
        "description": {
            "type": "text"
        },
        "repository_name": {
            "type": "text"
        },
        "html_url": {
            "type": "keyword"
        },
        "open_issues_count": {
            "type": "integer"
        },
        "pushed_at": {
            "type": "date"
        },
        "stargazers_count": {
            "type": "integer"
        },
        "file_name": {
            "type": "keyword"
        },
        "words": {
            "type": "text"
        },
        "class_name": {
            "type": "text"
        },
        "type_parameters": {
            "type": "nested",
            "properties": {
                "extends": {
                    "type": "keyword"
                },
                "name": {
                    "type": "keyword"
                }
            }
        },
        "access_modifier": {
            "type": "keyword"
        },
        "is_abstract": {
            "type": "boolean"
        },
        "is_static": {
            "type": "boolean"
        },
        "is_final": {
            "type": "boolean"
        },
        "annotation": {
            "type": "text"
        },
        "extends_class": {
            "type": "keyword"
        },
        "implements_interfaces": {
            "type": "keyword"
        },
        "imports": {
            "type": "keyword"
        },
        "package": {
            "type": "keyword"
        },
        "position": {
            "type": "nested",
            "properties": {
                "line": {
                    "type": "integer"
                },
                "row": {
                    "type": "integer"
                }
            }
        }
    }
}
method_properties = {
    "properties": {
        "id": {
            "type": "long"
        },
        "owner": {
            "type": "keyword"
        },
        "created_at": {
            "type": "date"
        },
        "description": {
            "type": "text"
        },
        "repository_name": {
            "type": "text"
        },
        "html_url": {
            "type": "keyword"
        },
        "open_issues_count": {
            "type": "integer"
        },
        "pushed_at": {
            "type": "date"
        },
        "stargazers_count": {
            "type": "integer"
        },
        "file_name": {
            "type": "keyword"
        },
        "words": {
            "type": "text"
        },
        "method_name": {
            "type": "text"
        },
        "access_modifier": {
            "type": "keyword"
        },
        "is_abstract": {
            "type": "boolean"
        },
        "is_static": {
            "type": "boolean"
        },
        "is_final": {
            "type": "boolean"
        },
        "return_type": {
            "type": "keyword"
        },
        "input_type": {
            "type": "keyword"
        },
        "throws": {
            "type": "keyword"
        },
        "annotation": {
            "type": "text"
        },
        "type_parameters": {
            "type": "nested",
            "properties": {
                "extends": {
                    "type": "keyword"
                },
                "name": {
                    "type": "keyword"
                }
            }
        },
        "position": {
            "type": "nested",
            "properties": {
                "line": {
                    "type": "integer"
                },
                "row": {
                    "type": "integer"
                }
            }
        },
        "cyclomatic_complexity": {
            "type": "integer"
        },
        "token_count": {
            "type": "integer"
        },
        "parameter_count": {
            "type": "integer"
        }
    }
}
variable_proprties = {
    "properties": {
        "id": {
            "type": "long"
        },
        "owner": {
            "type": "keyword"
        },
        "created_at": {
            "type": "date"
        },
        "description": {
            "type": "text"
        },
        "repository_name": {
            "type": "text"
        },
        "html_url": {
            "type": "keyword"
        },
        "open_issues_count": {
            "type": "integer"
        },
        "pushed_at": {
            "type": "date"
        },
        "stargazers_count": {
            "type": "integer"
        },
        "file_name": {
            "type": "keyword"
        },
        "words": {
            "type": "text"
        },
        "variable_name": {
            "type": "text"
        },
        "variable_type": {
            "type": "keyword"
        },
        "annotation": {
            "type": "text"
        },
        "access_modifier": {
            "type": "keyword"
        },
        "is_static": {
            "type": "boolean"
        },
        "is_final": {
            "type": "boolean"
        },
        "position": {
            "type": "nested",
            "properties": {
                "line": {
                    "type": "integer"
                },
                "row": {
                    "type": "integer"
                }
            }
        }
    }
}

indices = [(config.enum_index, enum_properties), \
(config.file_index, file_properties), (config.interface_index, interface_properties), \
(config.class_index, class_properties), (config.method_index, method_properties),  \
(config.variable_index, variable_proprties)]

def create_index(es_object, index_name, properties):
    created = False
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": properties
    }
    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            res = es_object.indices.create(index=index_name, ignore=400, body=settings)
            print(res)
            if res['acknowledged']:
                print('Created index', index_name)
            else:
                print('Index couldn\'t be created', index_name, res)
        created = True
    except Exception as ex:
        print('Exception!', index_name, ex)
    finally:
        return created

def delete_index(es_object, index_name):
    if es_object.indices.exists(index_name):
        res = es_object.indices.delete(index=index_name)


logging.basicConfig(level=logging.INFO)
bonsai = config.bonsai_url
print(bonsai)
auth = re.search('http\:\/\/(.*)\@', bonsai).group(1).split(':')
host = bonsai.replace('http://%s:%s@' % (auth[0], auth[1]), '')
print(host)

# es_header = [{
#  'host': host,
#  'port': 443,
#  'use_ssl': True,
#  'http_auth': (auth[0],auth[1])
# }]

es_header = [{
 'host': host,
 'port': 9200,
 'use_ssl': False
}]

es = Elasticsearch(es_header)

for index in indices:
    delete_index(es, index[0])
    create_index(es, index[0], index[1])
