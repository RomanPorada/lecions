lst = [1, 2 ,3, 4, 5]

print(lst)

for el in lst:
    print(el)

lst_iter = iter(lst)

print(type(lst_iter))

next(lst_iter)
next(lst_iter)

while True:
    try:
        print(next(lst_iter))
    except StopIteration:
        break

print('still running...')

class StudentGroup():
    def __init__(self):
        self.student_list = []
        

    def __iter__(self):
        self.__idx = 0
        return self
    
    def __getitem__(self, index):
        pass
    
    def __next__(self):
        if self.__idx < len(self.student_list):
            obj = self.student_list[self.__idx]
            self.__idx += 1
            return obj
        else:
            raise StopIteration

    def add_student(self, student):
        self.student_list.append(student)

    def __str__(self):
        return ",\n".join(self.student_list)
    
group_1 = StudentGroup()
group_1.add_student("ІР-11")
group_1.add_student("ІР-12")
group_1.add_student("ІР-13")
group_1.add_student("ІР-14")

print(group_1)

for el in group_1:
    print(f"На коврик {el}")

for el in group_1:
    print(f"На комсію {el}")

def first_gen():
    print("Helo one")
    yield
    print("Helo two")
    yield
    print("Helo thre")
    yield
first_gen()

f_gen = first_gen()
next(f_gen)
next(f_gen)

lst = [el for el in range(5)]

lst_gen = (el for el in range(5))

print(lst_gen)

for el in lst_gen:
    print(el)