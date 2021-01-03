from abc import abstractmethod, ABCMeta


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.all_animals = []

    def add_animal(self, animal):
        animal_type = type(animal).__name__
        if hasattr(self, animal_type):
            print(f"{animal_type}已在动物园")
        else:
            setattr(self, animal_type, True)

        if animal not in self.all_animals:
            print(f"add animal:{animal}")
            self.all_animals.append(animal)
        return self.all_animals


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, animal_type, size, habit):
        self.animal_type = animal_type
        self.size = size
        self.habit = habit

    @property
    def animal_is_violent(self):
        # 设置体型属性的值
        if str(self.size) == "大":
            self.size_num = 3
        elif str(self.size) == "中":
            self.size_num = 2
        elif str(self.size) == "小":
            self.size_num = 1
        else:
            print("Size input error!")

        # 判断是否为凶猛动物
        if self.animal_type == "食肉" and self.size_num >= 2 and self.habit == "凶猛":
            self.is_violent = True
        else:
            self.is_violent = False
        return self.is_violent


class Cat(Animal):
    voice = "Miao"

    def __init__(self, name, animal_type, size, habit):
        super().__init__(animal_type, size, habit)
        self.name = name

    @property
    def is_pet(self):
        self.is_violent = super().animal_is_violent
        if self.is_violent == True:
            is_pet = False
        else:
            is_pet = True
        return is_pet

    def __str__(self):
        return self.name


class Dog(Animal):
    voice = "Wang"

    def __init__(self, name, animal_type, size, habit):
        super().__init__(animal_type, size, habit)
        self.name = name

    @property
    def is_pet(self):
        self.is_violent = super().animal_is_violent
        if self.is_violent == True:
            is_pet = False
        else:
            is_pet = True
        return is_pet

    def __str__(self):
        return self.name


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    print(z.name)
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
