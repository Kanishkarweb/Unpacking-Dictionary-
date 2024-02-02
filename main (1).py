def print_person(name, age, city):  
  print(f"{name} is {age} years old and lives in {city}")  
my_dict = {'name': 'Kanishkar', 'age': 22, 'city': 'Erode'}  
print_person(**my_dict)  