
import re

string = 'hello 22 hi 98. Howdy 16'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)