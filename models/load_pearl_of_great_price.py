"""Load Pearl of Great Price."""

import re

from bs4 import BeautifulSoup
from langchain.schema.document import Document

from models.load_utils import clean
from models.load_utils import to_markdown


def remove_links(markdown_content) -> str:
    """Remove links from the document."""
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.sub(pattern, "", markdown_content)


def remove_lines_starting_with_pipe(text) -> str:
    """Remove unwanted lines of text."""
    # Pattern to match lines starting with "|"
    pattern = r"^\|.*$"

    # Use re.MULTILINE to match the pattern at the beginning of each line
    result = re.sub(pattern, "", text, flags=re.MULTILINE)

    return result


def remove_non_texts(markdown_text) -> str:
    """Remove unwanted lines of text."""
    # Define the regex pattern for non-texts
    non_text_pattern = re.compile(r"\[[^\]]+\]\[[^\]]+\]")

    # Use sub() to replace non-text patterns with an empty string
    cleaned_text = re.sub(non_text_pattern, "", markdown_text)

    return cleaned_text


def remove_non_texts_anywhere(markdown_text) -> str:
    """Remove unwanted lines of text."""
    # Define the regex pattern for lines starting with the non-text pattern '>'
    non_text_pattern = re.compile(r"^\s*>", re.MULTILINE)

    # Use sub() to replace non-text patterns at the beginning of lines with an empty string
    cleaned_text = re.sub(non_text_pattern, "", markdown_text)

    return cleaned_text


def load_pogp(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load Pearl of Great Price from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("h1", class_="entry-title")
    body = soup.find("div", class_="entry-content")

    content = clean(to_markdown(str(body), base_url=url)) if body else ""
    content = content.split("\n\n#### Further Reading\n\n")[0]
    content = remove_links(content)
    content = remove_lines_starting_with_pipe(content)
    content = remove_non_texts(content)
    content = remove_non_texts_anywhere(content)

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
        # "author": clean(author) if author else "",
    }
    return Document(page_content=content, metadata=metadata)
