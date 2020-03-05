def encode(text: str) -> str:
    nodes = [([char], text.count(char)) for char in set(text)]
    nodes = sorted(nodes, key=lambda item: item[1])
    alphabet = {char: '' for char in set(text)}
    while len(nodes) > 1:
        left = nodes[0]
        right = nodes[1]
        for char in left[0]:
            alphabet[char] = '0' + alphabet[char]
        for char in right[0]:
            alphabet[char] = '1' + alphabet[char]
        print(nodes)
        nodes[0] = (left[0] + right[0], left[1] + right[1])
        nodes.remove(right)
        nodes = sorted(nodes, key=lambda item: item[1])
    code = str(alphabet) + '\n'
    for char in text:
        code += alphabet[char]
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
