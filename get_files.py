from urllib.request import Request, urlopen
from time import sleep
import json
import os
import config

lang = 'Java'
access_token = config.access_token;
print(access_token)
sha = '/master?recursive=1&access_token={}'.format(access_token);
per_page = 100
requests = 0

def create_save_file(repo_name, content_path, path, requests):
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
    file_path = './repos/{}/{}'.format(repo_name, path)
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
        os.chmod(os.path.dirname(file_path), 0o777)
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(response)
        file.close()
    return requests


def download_page(page, requests):
    format_string = 'https://api.github.com/search/repositories?q=language:{}&sort=stars&order=desc&page={}&per_page={}&access_token={}'
    url = format_string.format(lang, page, per_page, access_token)
    repositories = urlopen(url).read().decode('utf-8')
    requests += 1

    repositories = json.loads(repositories)
    for repo in repositories['items']:
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
                requests = create_save_file(repo['name'], content_path, file['path'], requests)

for i in range(10, 15):
    print('\n\nDownloading page {}'.format(i))
    download_page(i, requests)
