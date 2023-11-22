"""Load Pearl of Great Price."""

from bs4 import BeautifulSoup
from langchain.schema.document import Document

from models.load_utils import clean
from models.load_utils import to_markdown


def remove_hrefs_and_strong_text(html_content):
    """Remove hrefs in p tag."""
    soup = BeautifulSoup(html_content, "html.parser")
    # Find all <p> tags containing <a> tags with href attributes and <em> tags
    for p_tag in soup.find_all("p"):
        a_tags = p_tag.find_all("a", href=True)
        for a_tag in a_tags:
            # Find <strong> tags within <em> tags and remove them
            em_tag = a_tag.find("em")
            if em_tag:
                strong_tag = em_tag.find("strong")
                if strong_tag:
                    strong_tag.extract()
            # Remove the entire <a> tag
            a_tag.extract()
    # Get the cleaned HTML content
    cleaned_content = str(soup)
    return cleaned_content


def load_pogp(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load Pearl of Great Price from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("h1", class_="entry-title")
    body = soup.find("div", class_="entry-content")

    content = clean(to_markdown(str(body), base_url=url)) if body else ""
    content = content.split("\n\n#### Further Reading\n\n")[0]
    content = remove_hrefs_and_strong_text(content)
    metadata = {
        "url": url,
        "title": clean(title) if title else "",
        # "author": clean(author) if author else "",
    }
    return Document(page_content=content, metadata=metadata)
