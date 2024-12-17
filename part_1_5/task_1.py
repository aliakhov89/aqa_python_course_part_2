#Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

#Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
# которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
# предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет,
# не превышая ее вместимость.

#Класс должен иметь следующий вид

#class MoneyBox:
#    def __init__(self, capacity):
   # конструктор с аргументом – вместимость копилки

#    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

#    def add(self, v):
        # положить v монет в копилку


#При создании копилки, число монет в ней равно 0.
#Примечание:
#Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.


class MoneyBox:
    def __init__(self, capacity): # Initialize the capacity and the number of coins in the piggy bank
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v): # Check if it's possible to add v coins without exceeding the capacity
        return self.coins + v <= self.capacity

    def add(self, v): # Add coins to the piggy bank
        if self.can_add(v):
            self.coins += v
        else:
            print("Cannot add coins: capacity exceeded!")