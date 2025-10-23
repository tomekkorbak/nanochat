# %%

def strip_thinking(text: str) -> str:
    """
    1. If there are not <think> tags, return string as is.
    2. If there are well-formed <think>[content]</think> tag pairs, remove these tags and their contents.
    3. If there are unclosed <think> tags, remove them and what follows them.
    """
    open_tag = "<think>"
    close_tag = "</think>"

    result_parts: list[str] = []
    scan_index = 0

    while True:
        start = text.find(open_tag, scan_index)
        if start == -1:
            # No more opening tags; append the rest and finish
            result_parts.append(text[scan_index:])
            break

        # Append content before the tag
        result_parts.append(text[scan_index:start])

        # Find the corresponding closing tag
        end = text.find(close_tag, start + len(open_tag))
        if end == -1:
            # Unclosed tag: drop everything from the opening tag onward
            break

        # Skip the entire <think>...</think> segment
        scan_index = end + len(close_tag)

    return "".join(result_parts)



