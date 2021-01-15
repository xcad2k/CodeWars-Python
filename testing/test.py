import re

string = "te3test"

temp = re.findall(r'\d+', string) 

print(temp[0])