from config import *
import requests
import sys

github_request = requests.get('https://api.github.com/meta')

if github_request.status_code != 200:
    print('Error while fetching Github ips: Bad HTTP Code')
    sys.exit()

github_response = github_request.json()
content = ''
i = 0
for ip_range in github_response['actions']:
    if content != '':
        content += '\n'

    i += 1
    acl_name = 'github_action_ips_' + str(i)
    content += 'acl ' + acl_name + ' src ' + ip_range
    content += '\n'
    content += 'http_access allow ' + acl_name

f = open(config_file_path, 'a')
f.write(content)
f.close()
