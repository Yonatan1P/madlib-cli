def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
        stripped_content = content.strip()
    return stripped_content


def parse_file(string_template):
    capturing = False
    dissected_string = ""
    parts = []
    current_part = ""
    for char in string_template:
        if not capturing:
            dissected_string += char
            if char == "{":
                capturing = True
        else:
            if char == "}":
                capturing = False
                parts.append(current_part)
                dissected_string += char
                current_part = ""
            else:
                current_part += char
    return [dissected_string, parts]


def merge(bare_template, responses):
    merged = bare_template
    for response in responses:
        merged = merged.replace("{}", response, 1)
    with open('madlib_cli/filled_template.txt', 'w') as answer:
        answer.write(merged)
    print(merged)
    return merged


inputs = [
    input("> Adjective: "),
    input("> Adjective: "),
    input("> A First Name: "),
    input("> Past Tense Verb: "),
    input("> A First Name: "),
    input("> Adjective: "),
    input("> Adjective: "),
    input("> Plural Noun: "),
    input("> Large Animal: "),
    input("> Small Animal: "),
    input("> A Girl's Name: "),
    input("> Adjective: "),
    input("> Plural Noun: "),
    input("> Adjective: "),
    input("> Plural Noun: "),
    input("> Number 1-50: "),
    input("> First Name's: "),
    input("> Number: "),
    input("> Plural Noun: "),
    input("> Number: "),
    input("> Plural Noun: ")
]

template = read_file('madlib_cli/template_madlib.txt')
bare_template = parse_file(template)
merge(bare_template[0], inputs)