import re

def highlight_text(
    text: str,
    query: str
):
    query_words = query.split()
    for word in query_words:
        pattern = re.compile(
            re.escape(word),
            re.IGNORECASE
        )
        text = pattern.sub(
            f"<b>{word}</b>",
            text
        )
    return text