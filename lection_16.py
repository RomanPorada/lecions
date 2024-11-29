from abc import ABC, abstractmethod

class AbstractCls(ABC):

    @abstractmethod
    def Some_method(self):
        pass

# for i in lst:
#     if i == 0:
#         continue
#     else:
#         number /=i

# EAFP = easier to ask forgivnes than a permision

try: 
    1 / 0
except ZeroDivisionError:
    print("Exeption has been caught")

print("still running...")

ex = ValueError("Some exeption text")

# raise ex

name = input('Enter name: ')

if len(name) < 6:
    raise ValueError(f"Given name {name} should be at least 5 characters long...")

print("still running...")

lst = (1, 2, 3, 4, 5)

try:
    while True:
        print(lst.pop())
except IndexError:
    print(f'List is empty {lst}')
except AttributeError:
    print(f"Not supported type {type(lst)}")
except Exception:
    print("Unknown exeption...")

print('still running...')

def average_num(sequence):
    sum_data = 0
    count = 0
    try:
        for element in sequence:
            try:
                sum_data += element 
                count += 1
            except TypeError:
                pass

        avarage = sum_data / count
    except ZeroDivisionError:
        avarage = 0
    return avarage

lst_2 = [1, 2, 3, 4, 5]
print(average_num(lst_2))

try:
    raise ValueError("Some exeption text")
except ValueError as ex:
    print(f"handled exception: {ex}")
finally:
    print("this is always executed")

print("still runnind...")

lst = [1, 2, 3, 4, 5]

for el in lst:
    print(el)

iterator = iter(lst)
print(iterator)

i = 0
while i < 4:
    print(next(iterator))