import sys
import re
import Implementation as imp

if (len(sys.argv) > 2):
    print("Error: Too many parameters. Needed: 1")
    exit(1)

if (re.search("([1-9]+[a-z]?[+-])*[1-9]+[a-z]+=[1-9]+",sys.argv[1])):
    matches = re.findall("[1-9]*[a-z]",sys.argv[1])
    coeff = []
    coeffNames = []
    for match in matches:
        coeff.append(int(re.findall("[0-9]+", match)[0]))
        coeffNames.append(re.findall("[a-z]+", match)[0])
    rhs=int(re.findall("[1-9]+",re.findall("=[1-9]+",sys.argv[1])[0])[0])
    print(imp.Memoization(len(coeff)-1,list(reversed(coeff)),rhs))
    print(imp.BruteForce(len(coeff)-1,list(reversed(coeff)),rhs))
    print(imp.Tabulation(len(coeff)-1,list(reversed(coeff)),rhs))
else:
    print("Bad parameter: The ecuation has not a valid format")