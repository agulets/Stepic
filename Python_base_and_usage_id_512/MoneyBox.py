'''
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
Класс должен иметь следующий вид
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.
'''


class MoneyBox:
    # конструктор с аргументом – вместимость копилки
    def __init__(self, capacity, coins_counter=0):
        self.capacity = capacity
        self.coins_counter = coins_counter

    # True, если можно добавить v монет, False иначе
    def can_add(self, v):
        return (self.capacity - self.coins_counter) >= v

    # положить v монет в копилку
    def add(self, v):
        if self.can_add(v):
            self.coins_counter = self.coins_counter + v
        else:
            print("Не влезет!")


if __name__ == '__main__':
    svin = MoneyBox(100)
    print(svin.coins_counter)
    svin.add(25)
    print(svin.coins_counter)
    svin.add(150)
    print(svin.coins_counter)
    print(svin.can_add(150))
    svin.add(75)
    print(svin.coins_counter)
