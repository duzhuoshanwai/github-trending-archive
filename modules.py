from datetime import date
from pathlib import Path
from bs4 import Tag
import re


def get_repo_name(element: Tag) -> str:
    repo_name = element.find("h2", class_="h3 lh-condensed").find("a").text
    return re.sub(r"\s+", "", repo_name)


def get_stars(element: Tag) -> str:
    stars = element.select("a[href*=stargazers]")[0].text
    return re.sub(r"\s+", "", stars)


def get_forks(element: Tag) -> str:
    forks = element.select("a[href*=forks]")[0].text
    return re.sub(r"\s+", "", forks)


def get_lang(element: Tag) -> str:
    lang_element = element.find("span", itemprop="programmingLanguage")
    if lang_element is not None:
        lang = lang_element.text
    else:
        lang = "Unknown"
    return re.sub(r"\s+", "", lang)


def get_desc(element: Tag) -> str:
    desc_element = element.find("p")
    if desc_element is not None:
        desc = desc_element.text.strip()
    else:
        desc = "None"
    return desc


def create_path(dir, today=None) -> Path:
    if today is None:
        today = date.today()
    directory_path = Path(dir) / f"{today.year}-{today.month:02d}"
    directory_path.mkdir(parents=True, exist_ok=True)
    return directory_path


def create_md(path, today=None) -> Path:
    if today is None:
        today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    md_path = Path(path) / f"{today_str}.md"
    md_path.touch(exist_ok=True)
    return md_path


if __name__ == "__main__":
    print("This module is being run directly")
