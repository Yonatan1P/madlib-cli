welcome="Hello! Welcome to the our python madlib game!\
        \nYou will be prompted to choose some adjectives,\
        \nnouns, and verbs to fill in our funny story!"
print(welcome)
promptAdj=input(">Adjective:")
promptFirstName=input(">A first name:")
promptPastTenseVerb=input(">A past tense verb:")
promptPluralVerb=input(">A plural verb:")
promptSmallNumber=input(">A number between 1 & 50:")
promptfirstName=input(">A first name:")
import re
file_path='madlib_cli/template_madlib.txt'
def read_file(file_path):
    if not file_path:
        return None

    template=''
    with open(file_path) as file:
        for line in file:
            template +=line
    print(template)

def parse_file(template):
    words=[]
    words+=template.splice(' ')
    print(words)