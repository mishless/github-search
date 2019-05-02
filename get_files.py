from urllib.request import Request, urlopen
from time import sleep
import json
import os
import config
import lizard
import os, base64, re, logging
import file_parser
from elasticsearch import Elasticsearch

lang = 'Java'
access_token = config.access_token
sha = '/master?recursive=1&access_token={}'.format(access_token);
per_page = 100
requests = 0

# Log transport details (optional):
logging.basicConfig(level=logging.INFO)

# Parse the auth and host from env:
bonsai = config.bonsai_url
auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

# Connect to cluster over SSL using auth for best security:
es_header = [{
 'host': host,
 'port': 443,
 'use_ssl': True,
 'http_auth': (auth[0],auth[1])
}]

# Instantiate the new Elasticsearch connection:
es = Elasticsearch(es_header)

def create_save_file(repo_name, content_path, path, requests, id, url):
    if requests == 5000:
        sleep(60*60)
        requests = 0
    request = Request('{}/{}?access_token={}'.format(content_path, path, access_token))
    request.add_header('Accept', 'application/vnd.github.v3.raw')
    try:
        response = urlopen(request).read().decode('utf-8')
        requests += 1
    except:
        print("Retrying for {}".format(path))
        response = urlopen(request).read().decode('utf-8')
        requests += 1
    print('Request for {}, requests {}'.format(path, requests))
    doc = {
        'id': id,
        'url': url,
        'file_name': os.path.basename(path),
        'words': response
    }
    res = es.index(index=config.file_index, doc_type='doc', body=doc)
    docs = file_parser.parse_data(response, url)
    for doc in docs:
        res = es.index(index=doc[0], doc_type='doc', body=doc[1])
    # file_path = './repos/{}/{}'.format(repo_name, path)
    # if not os.path.exists(os.path.dirname(file_path)):
    #     os.makedirs(os.path.dirname(file_path))
    #     os.chmod(os.path.dirname(file_path), 0o777)
    # with open(file_path, 'a', encoding='utf-8') as file:
    #     file.write(response)
    #     file.close()
    # i = lizard.analyze_file(file_path)
    # for function_index in range(len(i.__dict__['function_list'])):
    #     print(i.function_list[function_index].__dict__)
    return requests

def download_page(page, requests):
    format_string = 'https://api.github.com/search/repositories?q=language:{}&sort=stars&order=desc&page={}&per_page={}&access_token={}'
    url = format_string.format(lang, page, per_page, access_token)
    repositories = urlopen(url).read().decode('utf-8')
    requests += 1

    repositories = json.loads(repositories)
    for repo in repositories['items']:
        doc = {
            'id': repo['id'],
            'owner': repo['owner']['login'],
            'created_at': repo['created_at'],
            'description': repo['description'],
            'name': repo['name'],
            'html_url': repo['html_url'],
            'open_issues_count': repo['open_issues_count'],
            'pushed_at': repo['pushed_at'],
            'stargazers_count': repo['stargazers_count']
        }
        res = es.index(index=config.repository_index, doc_type='doc', body=doc)
        content_path = repo['contents_url'].replace('{+path}', '')
        if requests == 5000:
            sleep(60*60)
            requests = 0
        try:
            requests += 1
            files = urlopen(repo['trees_url'].replace('{/sha}', sha)).read().decode('utf-8')
        except:
            print("Ignoring {}".format(repo['trees_url'].replace('{/sha}', sha)))
        files = json.loads(files)
        for file in files['tree']:
            if file['path'].endswith('.java'):
                requests = create_save_file(repo['name'], content_path, file['path'], requests, repo['id'], file['url'])

for i in range(10, 15):
    print('\n\nDownloading page {}'.format(i))
    download_page(i, requests)
