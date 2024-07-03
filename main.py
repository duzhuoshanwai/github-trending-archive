import requests
from bs4 import BeautifulSoup
from datetime import datetime
from modules import get_desc, get_forks, get_lang, get_repo_name, get_stars, create_path, create_md

url = "https://github.com/trending/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

repos = soup.find_all(class_="Box-row")

# 检查目录并创建
path = create_path(dir="./data")
# 检查md并创建
md_path = create_md(path)

with open(md_path, 'w', encoding='utf-8') as file:
    for repo in repos:
        repo_name = get_repo_name(repo)
        md_formatted_repo_name = f'### **Repository:** [{repo_name}](https://github.com/{repo_name})'
        stars = get_stars(repo)
        md_formatted_stars = f'**Stars:** {stars}'
        forks = get_forks(repo)
        md_formatted_forks = f'**Forks** {forks}'
        lang = get_lang(repo)
        md_formatted_lang = f'**Language:** {lang}'
        desc = get_desc(repo)
        md_formatted_desc = f'**Description:** {desc}'
        file.write(md_formatted_repo_name+'  \n')
        file.write('\n')
        file.write(md_formatted_lang+'  \n')
        file.write(md_formatted_stars+'  \n')
        file.write(md_formatted_forks+'  \n')
        file.write(md_formatted_desc+'  \n')
        file.write("\n")