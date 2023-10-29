"""Load knowhys."""

import json
import os
from typing import Any
from typing import Iterator
from typing import cast

from bs4 import BeautifulSoup  # type: ignore
from langchain.document_loaders.base import BaseLoader
from langchain.schema.document import Document
from markdownify import MarkdownConverter  # type: ignore
from tqdm import tqdm

from models.load_utils import clean


# Create shorthand method for custom conversion
def _to_markdown(html: str, **options: Any) -> str:
    """Convert html to markdown."""
    return cast(str, MarkdownConverter(**options).convert(html))


def load_dc_people(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load dc people from a url and html."""
    soup = BeautifulSoup(html, bs_parser)
    title = soup.find("h1", class_="elementor-heading-title").text
    author = soup.find("h2", class_="elementor-heading-title").text

    body = soup.find("div", class_="elementor-element-7c4c46d2")
    content = clean(_to_markdown(str(body), base_url=url)) if body else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
        "author": clean(author) if author else "",
    }
    return Document(page_content=content, metadata=metadata)


class PeopleLoader(BaseLoader):
    """Loader for General Conference Talks."""

    def lazy_load(self) -> Iterator[Document]:
        """A lazy loader for Documents."""
        raise NotImplementedError(f"{self.__class__.__name__} does not implement lazy_load()")

    def __init__(self, path: str = "", bs_parser: str = "html.parser"):
        """Initialize loader."""
        super().__init__()
        self.path = path
        self.bs_parser = bs_parser

    def load(self, verbose: bool = False) -> list[Document]:
        """Load documents from path."""
        docs = []
        for filename in tqdm(os.listdir(self.path), disable=not verbose):
            path = os.path.join(self.path, filename)
            with open(path, encoding="utf8") as f:
                data = json.load(f)
            doc = load_dc_people(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue
            if not doc.metadata["author"]:
                if verbose:
                    print("Missing author", filename)
            docs.append(doc)
        return docs
