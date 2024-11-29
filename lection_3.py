form = '{0} some {1} text'.format(1234, "dsa")

print(form)

var_1 = 1234
var_2 = "dfg"

form_2 = f"{var_1} and {var_2}"

print(form_2)

str_1 = "test text"

print(id(str_1))

str_2 = str_1

print(id(str_1) == id(str_2))

grade = 44

if grade >= 88:
    print('A mark')
elif grade >= 71:
    print("B mark")
elif grade >= 51:
    print("C mark")
else:
    print("expelt")

price = 12 
volume = 0

if price > 10:
    volume = 12
else:
    volume = 100

print(volume)

volume = 12 if price > 10 else 100