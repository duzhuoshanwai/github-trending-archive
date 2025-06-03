import requests
from requests import Response
from bs4 import BeautifulSoup, Tag
from pathlib import Path
from modules import (
    get_desc,
    get_forks,
    get_lang,
    get_repo_name,
    get_stars,
    create_path,
    create_md,
)

url = "https://github.com/trending/"
page: Response = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

repos: Tag = soup.find_all(class_="Box-row")

# 检查目录并创建
path: Path = create_path(dir="./data")
# 检查md并创建
md_path: Path = create_md(path)

# 定义 Markdown 模板
REPO_TEMPLATE: str = """### **Repository:** [{repo_name}](https://github.com/{repo_name})

**Language:** {lang}  
**Stars:** {stars}  
**Forks:** {forks}  
**Description:** {desc}

"""


# 处理单个仓库并生成 Markdown 内容的函数，使用str.format()
def process_repo(repo: Tag) -> str:
    return REPO_TEMPLATE.format(
        repo_name=get_repo_name(repo),
        lang=get_lang(repo),
        stars=get_stars(repo),
        forks=get_forks(repo),
        desc=get_desc(repo),
    )


# 使用 map 处理所有仓库并写入文件
with open(md_path, "w", encoding="utf-8") as file:
    # 使用 map 生成所有仓库的内容
    repo_contents = map(process_repo, repos)
    file.writelines(repo_contents)
