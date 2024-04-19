from pypdf import PdfReader


class PageCountParse(Exception):
    """Could not parse the doc, failed page count check"""

    pass


def get_fitz_doc_obj(f_name: str) -> PdfReader:
    reader = PdfReader(f_name)
    pageCount = len(reader.pages)
    if pageCount < 1:
        raise PageCountParse(f"Could not parse the doc, failed page count check: {f_name}")
    else:
        return reader
