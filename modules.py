from datetime import date
from pathlib import Path


def get_repo_name(element):
    repo_name = (
        element.find("h2", class_="h3 lh-condensed")
        .find("a")
        .text.replace(" ", "")
        .replace("\n", "")
    )
    return repo_name


def get_stars(element):
    stars = (
        element.select("a[href*=stargazers]")[0].text.replace(" ", "").replace("\n", "")
    )
    return stars


def get_forks(element):
    forks = element.select("a[href*=forks]")[0].text.replace(" ", "").replace("\n", "")
    return forks


def get_lang(element):
    lang_element = element.find("span", itemprop="programmingLanguage")
    if lang_element is not None:
        lang = lang_element.text.strip()
    else:
        lang = "Unknown"
    return lang


def get_desc(element):
    desc_element = element.find("p")
    if desc_element is not None:
        desc = desc_element.text.strip()
    else:
        desc = "None"
    return desc


def create_path(dir, today=None):
    if today is None:
        today = date.today()
    directory_path = Path(dir) / f"{today.year}-{today.month:02d}"
    directory_path.mkdir(parents=True, exist_ok=True)
    return directory_path

def create_md(path, today=None):
    if today is None:
        today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    md_path = Path(path) / f"{today_str}.md"
    md_path.touch()
    return md_path


if __name__ == "__main__":
    print("This module is being run directly")
