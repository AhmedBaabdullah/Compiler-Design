
import re

string = 'Twelve:12 Eighty nine:89 Fifty Five:55 Sixty:60'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)