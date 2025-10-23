# %%

import re

def strip_thinking(text: str) -> str:
    """
    1. If there are not <think> tags, return string as is.
    2. If there are well-formed <think>[content]</think> tag pairs, remove these tags and their contents.
    3. If there are unclosed <think> tags, remove them and what follows them.
    """
    if "</think>" not in text:
        return ""

    # Find all <think> tags
    think_tags = re.findall(r'<think>.*?</think>', text)

    # If the tag is not closed, remove the tag and what follows it
    breakpoint()
    if think_tags:

        text = think_tags[0]


    # INSERT_YOUR_CODE
    idx = text.find("<think>")
    if idx != -1:
        return ""

    return text

print(strip_thinking("<think>hello world</think>")) # ""

print(strip_thinking("<think>hello world</think> th")) # " th"
print(strip_thinking("<think>hello world</think> then this was th</think>hello world")) # "then this was th</think>hello world"
print(strip_thinking("<think>hello world")) # ""


