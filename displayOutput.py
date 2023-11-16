import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print("I have just rolled 2 die")
print("The numbers produced are", dice1, "and", dice2)

if dice1 + dice2 > 6:
    print("You scored greater than half!")

elif dice1 + dice2 < 6:
    print('You scored less than half.')

else:
    print('You scored exactly half!')

if dice1 > 3:
    print('Roll 1 is above half (う-´)づ.')

elif dice1 < 3:
    print('Roll 1 is under half (੭ˊᵕˋ)੭.')

elif dice1 == 3:
    print('Roll 1 is half.')

if dice2 > 3:
    print('Roll 2 is above half (う-´)づ.')

elif dice2 < 3:
    print('Roll 2 is under half (੭ˊᵕˋ)੭.')

elif dice2 == 3:
    print('Roll 2 is half.')

if dice1 + dice2 > 6:
    print("Congradulations! Victory 🥳 Pew Pew Pew 🕹️.")

if dice1 + dice2 == 6:
    print("You are totally balanced 🧘. Zen mode ☯.")

if dice1 + dice2 < 6:
    print("You're an underdog 🐕 nothin' wrong with that ૮⍝• ᴥ •⍝ა.")