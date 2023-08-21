import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print('Status code: ', r.status_code)

response_dict = r.json()
print("Total repositories: ", response_d



names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])uuuuuuu
    stars.append(repo_dict['stargazers_count'])



