import json  
student = '{"Name": "Nayyar", "Compiler Design": ["Python", "java", "c"]}'  
student_dict = json.loads(student)  
print("The dictionary after parsing: ", student_dict)  
print("\nValues in the Languages: ", student_dict['Compiler Design'])  