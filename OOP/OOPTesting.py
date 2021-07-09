import OOP

# Exercise 77

c = OOP.Comment("OGSik", "Nice content!", 156)

# Exercise 78

acct1 = OOP.BankAccount("Orlando")

print(acct1.owner)
print(acct1.get_balance())
acct1.deposit(10)
acct1.withdraw(3)
print(acct1.get_balance())

# Exercise 79

c1 = OOP.Chicken(name="Alice", species="Partride Silkie")
c2 = OOP.Chicken(name="Amelia", species="Speckled Sussex")

print(OOP.Chicken.total_eggs)
c1.lay_egg()
print(OOP.Chicken.total_eggs)
c2.lay_egg()
c2.lay_egg()
print(OOP.Chicken.total_eggs)

# Exercise 81:

npc_savage = OOP.NPC("Bob", 100, 12)

print(npc_savage.name)
print(npc_savage.hp)
print(npc_savage.level)
print(npc_savage.speak())

# Exercise 82

orlando_DNA = OOP.Child()

print(orlando_DNA.eye_color)
print(orlando_DNA.hair_color)
print(orlando_DNA.hair_type)

# Exercise 83

my_train = OOP.Train(8)

print(my_train)
print(len(my_train))

# Exercise 84

days = OOP.week2()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))

# Exercise 85

gen = OOP.yes_or_no()

for _ in range(0, 20):
    print(next(gen))

# Exercise 86

gen = OOP.make_song(5, "flies")

for _ in range(0, 6):
    print(next(gen))

# Exercise 87, 88

sevens = OOP.get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])

gen = OOP.get_multiples(2, 3)

for _ in range(0, 3):
    print(next(gen))

default_multiples = OOP.get_multiples()
new_list = list(default_multiples)
print(new_list)

# Exercise 89

OOP.my_function(1, 2, 3, a="yeah")

# Exercise 90

print(OOP.add(1, 2))
print(OOP.greet("Orlando"))

# Exercise 91

print(OOP.add_all(1, 2))
print(OOP.add_all(1, 2, 3))
# OOP.add_all(1, 2, 3, 4)

# Exercise 92

print(OOP.add(1, 2))
print(OOP.add("2", "1"))

# Exercise 93

print(OOP.show_secrets(1))
print(OOP.show_secrets(role="admin"))

# Exercise 94

print(OOP.say_hi())