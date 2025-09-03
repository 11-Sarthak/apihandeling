from plotly.graph_objs import Bar
from plotly import offline
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars,labels = [], [],[]

for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href ='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description= repo_dict['description']
    label= f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
}]

my_layout = {
    'title': 'Most starred Python projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}  # ✅ fixed
}

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='python_repos.html')
