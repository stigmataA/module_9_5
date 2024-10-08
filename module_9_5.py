class StepValueError(ValueError):
    pass


class Iterator():
    def __init__(self, start, stop, step=1, pointer= None):
        self.start = start # целое исло с которого начинается итерация
        self.stop = stop # целое число на которое заказнчивается итерация
        self.step = step # шаг итерации
        self.pointer = pointer # указатель текущей итерации


    def __iter__(self): # метод итератора
        self.pointer = self.start - self.step
        return self # возвращает само себя

    def __next__(self): # метод next
        self.pointer += self.step
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration() # выход из итератора 
            return self.pointer
        elif self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration()
            return self.pointer
        else:
            raise StepValueError


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
