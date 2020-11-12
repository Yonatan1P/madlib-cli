def read_file(file_path):
    with open(file_path) as file:
        content=file.read()
        stripped_content=content.strip()
    return stripped_content

def parse_file(string_template):
    capturing = False
    dissected_string=""
    parts=[]
    current_part=""
    for char in string_template:
        if not capturing:
            dissected_string += char
            if char =="{":
                capturing = True
        else:
            if char=="}":
                capturing = False
                parts.append(current_part)
                dissected_string+=char
                current_part=""
            else:
                current_part+= char
    return[dissected_string,parts]

def merge(bare_template, responses):
    merged = bare_template
    for response in responses:
        merged=merged.replace("{}",response,1)
    with open('madlib_cli/filled_template.txt','w') as answer:
        answer.write(merged)
    print(merged)
    return merged