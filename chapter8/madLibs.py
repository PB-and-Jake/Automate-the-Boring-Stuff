#! python3
# madLibs.py - reads text files and lets user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appear

import re

madLib = open('madLibs.txt')
content = madLib.read()
madLib.close()

keywords = re.compile('ADJECTIVE|VERB|NOUN|ADVERB')

while True:
    match = keywords.search(content)
    if match != None:
        print(f'Enter an {match.group().lower()}:')
        userInput = input()
        content = content.replace(str(match.group()), str(userInput), 1)
    else:
        break

output = open('madLibsResult.txt', 'w')
output.write(content)
output.close()
    
