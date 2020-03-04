def encode(text: str) -> str:
    chars = {}
    for char in text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    chars = sorted(chars.items(), key=lambda item: item[1])
    return 


def decode(code: str) -> str:
    pass
