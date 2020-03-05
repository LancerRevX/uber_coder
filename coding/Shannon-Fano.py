def get_codes(chars: list, code='') -> dict:
    if len(chars) == 0:
        return {}
    elif len(chars) == 1:
        if len(code) == 0:
            code = '0'
        return {chars[0][0]: code}
    else:
        i = -1
        if len(chars) > 2:
            frequencies = [frequency for (_, frequency) in chars]
            last_difference = abs(sum(frequencies[:1]) - sum(frequencies[1:]))
            for j in range(1, len(frequencies)):
                if abs(sum(frequencies[:j]) - sum(frequencies[j:])) > last_difference:
                    i = j - 1
        codes = get_codes(chars[:i], code + '0')
        codes.update(get_codes(chars[i:], code + '1'))
        return codes


def encode(text: str) -> str:
    chars = list()
    copy = text
    while len(copy) > 0:
        chars.append((copy[0], text.count(copy[0]) / len(text)))
        copy = copy.replace(copy[0], '')
    chars = sorted(chars, key=lambda item: item[1], reverse=True)
    codes = get_codes(chars)
    code = str(chars) + str(codes) + '\n'
    for char in text:
        code += codes[char]
    return code


def decode(code: str) -> str:
    pass
