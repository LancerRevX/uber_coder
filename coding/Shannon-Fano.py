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
                current_difference = abs(sum(frequencies[:j]) - sum(frequencies[j:]))
                if current_difference > last_difference:
                    i = j - 1
                    break
                else:
                    last_difference = current_difference

        codes = get_codes(chars[:i], code + '0')
        codes.update(get_codes(chars[i:], code + '1'))
        return codes


def encode(text: str) -> str:
    chars = [(char, text.count(char) / len(text)) for char in set(text)]
    chars = sorted(chars, key=lambda item: item[1], reverse=True)
    codes = get_codes(chars)
    code = str(codes) + '\n'
    for char in text:
        code += codes[char]
    return code


def decode(code: str) -> str:
    alphabet, code = code.split('\n', 1)
    alphabet = eval(alphabet)
    alphabet = {code: char for char, code in alphabet.items()}
    current_code = ''
    text = ''
    for char in code:
        current_code += char
        if current_code in alphabet:
            text += alphabet[current_code]
            current_code = ''
    return text
