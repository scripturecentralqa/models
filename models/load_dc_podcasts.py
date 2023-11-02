"""Load podcasts."""

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

from urllib.parse import urljoin, urlparse

from models.load_utils import clean


# Create shorthand method for custom conversion
def _to_markdown(html: str, **options: Any) -> str:
    """Convert html to markdown."""
    return cast(str, MarkdownConverter(**options).convert(html))


def load_dc_podcasts(url: str, html: str, bs_parser: str = "html.parser") -> Document:
    """Load dc podcasts from a url and html."""

    path_components = urlparse(url).path.split('/')
    title = path_components[-1]
    content = clean(_to_markdown(html, base_url=url)) if html else ""

    metadata = {
        "url": url,
        "title": clean(title) if title else "",
    }
    return Document(page_content=content, metadata=metadata)


class PodcastsLoader(BaseLoader):
    """Loader for D&C Podcasts."""

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
            doc = load_dc_podcasts(data["url"], data["html"], bs_parser=self.bs_parser)
            if not doc.metadata["title"] or not doc.page_content:
                if verbose:
                    print("Missing title or content - skipping", filename)
                continue

            docs.append(doc)
        return docs