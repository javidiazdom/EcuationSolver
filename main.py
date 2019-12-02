import sys
import re

if (len(sys.argv) > 2):
    print("Error: Too many parameters. Needed: 1")
    exit(1)

if (re.search("([1-9]*[a-z]?[+-])*[1-9]+[a-z]+=[1-9]+",sys.argv[1])):
    matches = re.findall("[1-9]*[a-z]",sys.argv[1])
    variables = {}
    for match in matches:
        print(match)
else:
    print("Bad parameter: The ecuation has not a valid format")

