"""Load Redeemer of Israel."""

from typing import Any

from bs4 import BeautifulSoup
from langchain.schema.document import Document

from models.load_utils import clean
from models.load_utils import to_markdown


def remove_strings(page_content):
    """This function removed unwanted strings."""
    # List of strings to remove
    strings_to_remove = ["|", "-"]

    # Iterate through each character in the page content
    cleaned_content = "".join(char for char in page_content if char not in strings_to_remove)

    return cleaned_content


def extract_title(soup: BeautifulSoup) -> Any:
    """Extract the title from the page."""
    # get the title
    title = soup.find("h3", class_="post-title")
    return title


def extract_content(soup: BeautifulSoup) -> Any:
    """Extract the HTML content from the page."""
    # Find all sections
    content = soup.find_all("div", class_="post-body entry-content")
    return content


def load_redeemer(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load redeemer of israel from a url and html."""
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    content = extract_content(soup)
    content = clean(to_markdown(str(content), base_url=url)) if content else ""
    clean_content = remove_strings(content)

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    print(metadata)
    return Document(page_content=clean_content, metadata=metadata)
