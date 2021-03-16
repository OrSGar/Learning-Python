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
# Colt also returned eggs after he lays one. Convention?
class Chicken:
    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1

c1 = Chicken(name="Alice", species="Partride Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")

print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
c2.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)










