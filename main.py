import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status code:", response.status_code)
response_dict = response.json()
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

# Info about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# First Repository
print("\nSelected information about first repository:")
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# For Visualization using Pygal
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')