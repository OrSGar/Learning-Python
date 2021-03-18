# # Exercise 77
# class Comment:
# # Apparently its ok for class attributes to have same name as params
#     def __init__(self, username, text, likes):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
#
# c = Comment("OGSik", "Lol ur so silly u silly goose", 156)

# Exercise 78
#
# class BankAccount:
#     # FYI Colt returned balance after each depo/withdraw
#
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0.0
#
#     def deposit(self, amt):
#         self.balance += amt
#
#     def withdraw(self, amt):
#         self.balance -= amt
#
#     def get_balance(self):
#         return self.balance
#
#
# acct1 = BankAccount("Orlando")
#
# print(acct1.owner)
# print(acct1.get_balance())
# acct1.deposit(10)
# acct1.withdraw(3)
# print(acct1.get_balance())

# Exercise 79
# # Colt also returned eggs after he lays one. Convention?
# class Chicken:
#     total_eggs = 0
#
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.eggs = 0
#
#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1
#
# c1 = Chicken(name="Alice", species="Partride Silkie")
# c2 = Chicken(name="Amelia", species="Speckled Sussex")
#
# print(Chicken.total_eggs)
# c1.lay_egg()
# print(Chicken.total_eggs)
# c2.lay_egg()
# c2.lay_egg()
# print(Chicken.total_eggs)

# Exercise 81:
#
# class Character:
#
#     def __init__(self, name, hp, lvl):
#         self.name = name
#         self.hp = hp
#         self.level = lvl
#
#
# class NPC(Character):
#
#     def __init__(self, name, hp, lvl):
#         super(NPC, self).__init__(name, hp, lvl)
#
#     def speak(self):
#         return f"{self.name} says: 'You looking for some trouble SOY BOY??'"
#
#
# npc_savage = NPC("Bob", 100, 12)
#
# print(npc_savage.name)
# print(npc_savage.hp)
# print(npc_savage.level)
# print(npc_savage.speak())

# Exercise 82:
# In Colts code, he did an init for Mother and Father, afterwards he passed on child
# class Mother:
#     def set_traits(self):
#         self.eye_color = "brown"
#         self.hair_color = "dark brown"
#         self.hair_type = "curly"
#
# class Father:
#
#     def set_traits(self):
#         self.eye_color = "blue"
#         self.hair_color = "blond"
#         self.hair_type = "straight"
#
#
# class Child(Mother, Father):
#
#     def __init__(self):
#         super(Child, self).set_traits()
#
#
# orlando_DNA = Child()
#
# print(orlando_DNA.eye_color)
# print(orlando_DNA.hair_color)
# print(orlando_DNA.hair_type)

# # Exercise 83
#
# class Train():
#
#     def __init__(self, cars):
#         self.num_cars = cars
#
#     def __repr__(self):
#         return f"{self.num_cars} car train"
#
#     def __len__(self):
#         return self.num_cars
#
#
# my_train = Train(8)
#
# print(my_train)
# print(len(my_train))

# Exercise 84:
#
# def week():
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
#     index = 0
#     while index < len(days):
#         try:
#             yield days[index]
#         except StopIteration:
#             pass
#         else:
#             index += 1
# # Colts implementation
# def week2():
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
#     for day in days:
#         yield day
#
# days = week2()
#
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))

# Exercise 85:
#
# def yes_or_no():
#     yes_flag = False
#     while True:
#         if not yes_flag:
#             yield "yes"
#         else:
#             yield "no"
#
#         yes_flag = not yes_flag
# # Colts implementation only uses on variable and checks against that
# def yes_or_no_colt():
#     answer = "yes"
#     while True:
#         yield answer
#
#         answer = "no" if answer == "yes" else "yes"
#
# gen = yes_or_no()
#
# for _ in range(0, 20):
#     print(next(gen))
#
# def make_song(count, bev):
#
#     while count >= 0:
#         if count == 0:
#             yield "NO MORE FORTNITE"
#         yield f"{count} of {bev} on the wall"
#         count -= 1
#
#
# gen = make_song(5, "ligma")
#
# for _ in range(0, 6):
#     print(next(gen))

# Exercise 87, 88
#
# def get_multiples(num=1, count=10):
#     for i in range(1, count + 1):
#         yield i * num
#
#
# def get_multiples_colt(num=1, count=10):
#     next_num = num
#
#     while count > 0:
#         yield next_num
#         count -= 1
#         next_num += num
#
#
# def get_unlimited_multiples(num = 1):
#     multiple = 1
#
#     while True:
#         yield multiple * num
#         multiple += 1
#
#
# sevens = get_unlimited_multiples(7)
#
# print([next(sevens) for i in range(15)])
#
#
# # gen = get_multiples(2, 3)
# #
# # for _ in range(0, 3):
# #     print(next(gen))
# #
# # default_multiples = get_multiples()
# #
# # new_list = list(default_multiples)
# #
# # print(new_list)

