import random
p1=input("enter the player-1: ")
p2=input("enter the player-2: ")

winning_point=100
p1_sc=0
p2_sc=0
while p1_sc<winning_point or p2_sc<winning_point:
    p1_st=input("continue the game (Y) or (N):")
    if p1_st=='Y':
        p1_dice=random.randint(1,6)
        print(f"{p1}: your dice score: {p1_dice}")
        p1_sc+=p1_dice
        print(f"{p1}: your total score: {p1_sc}")
    else:
        p2_sc
