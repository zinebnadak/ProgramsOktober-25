import random

# Setup: Initial values
hero_hp = 10
monster_hp = 20

hero_min_attack = 5
hero_max_attack = 8

monster_min_attack = 3
monster_max_attack = 12


# Function to simulate the battle
def battle():
    global hero_hp, monster_hp

    print(f"Battle begins! Hero HP = {hero_hp}, Monster HP = {monster_hp}.\n")

    # Repeat the battle until either hero or monster has HP < 1
    while hero_hp > 0 and monster_hp > 0:
        # Player's turn to attack
        print(f"Your turn! Hero HP = {hero_hp}, Monster HP = {monster_hp}")
        action = input("Do you want to (a)ttack or (d)efend? ").lower()

        if action == "a":
            # Hero attacks
            damage = random.randint(hero_min_attack, hero_max_attack)
            monster_hp -= damage
            print(f"Hero attacks and deals {damage} damage.")
        elif action == "d":
            # Hero defends (Monster's attack damage is halved)
            print("Hero defends and blocks some damage!")
            damage = random.randint(monster_min_attack, monster_max_attack) // 2
            hero_hp -= damage
            print(f"Monster attacks and deals {damage} damage.")
        else:
            print("Invalid choice, you must choose 'a' to attack or 'd' to defend.")
            continue  # Skip the monster's turn and ask for input again

        print(f"Monster now has {monster_hp} HP.")
        print(f"Hero now has {hero_hp} HP.\n")

        # Monster's turn to attack if it's still alive
        if monster_hp > 0:
            damage = random.randint(monster_min_attack, monster_max_attack)
            hero_hp -= damage
            print(f"Monster attacks and deals {damage} damage.")
            print(f"Hero now has {hero_hp} HP.\n")

        # Check if the battle has ended
        if hero_hp <= 0:
            print("Monster wins!")
            break
        elif monster_hp <= 0:
            print("Hero wins!")
            break


# Run the battle
battle()





