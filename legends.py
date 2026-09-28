import random


SAVE_FILE = "eldoria_save.txt"

WEAPONS = [
    {"name": "Wooden Sword", "rank": "Common", "damage": 3, "price": 10},
    {"name": "Rusty Axe", "rank": "Common", "damage": 4, "price": 12},
    {"name": "Training Bow", "rank": "Common", "damage": 3, "price": 10},
    {"name": "Iron Sword", "rank": "Rare", "damage": 7, "price": 35},
    {"name": "Steel Axe", "rank": "Rare", "damage": 8, "price": 40},
    {"name": "Long Bow", "rank": "Rare", "damage": 7, "price": 35},
    {"name": "Crystal Blade", "rank": "Super Rare", "damage": 12, "price": 75},
    {"name": "Shadow Dagger", "rank": "Super Rare", "damage": 11, "price": 70},
    {"name": "Lightning Bow", "rank": "Super Rare", "damage": 12, "price": 75},
    {"name": "Flame Sword", "rank": "Epic", "damage": 17, "price": 130},
    {"name": "Ice Spear", "rank": "Epic", "damage": 16, "price": 125},
    {"name": "Thunder Hammer", "rank": "Epic", "damage": 18, "price": 140},
    {"name": "Phoenix Blade", "rank": "Mythical", "damage": 23, "price": 210},
    {"name": "Demon Slayer", "rank": "Mythical", "damage": 25, "price": 230},
    {"name": "Celestial Staff", "rank": "Mythical", "damage": 22, "price": 205},
    {"name": "Dragon King's Sword", "rank": "Legendary", "damage": 32, "price": 350},
    {"name": "Blade of Eternity", "rank": "Legendary", "damage": 35, "price": 380},
    {"name": "Bow of the Gods", "rank": "Legendary", "damage": 33, "price": 360},
    {"name": "Royal Spear", "rank": "Rare", "damage": 8, "price": 42},
    {"name": "Moonlight Staff", "rank": "Epic", "damage": 17, "price": 135},
]

ARMORS = [
    {"name": "Cloth Clothes", "rank": "Common", "defense": 1, "hp": 5, "mana": 0, "price": 10},
    {"name": "Leather Armor", "rank": "Common", "defense": 2, "hp": 10, "mana": 0, "price": 18},
    {"name": "Iron Armor", "rank": "Rare", "defense": 4, "hp": 20, "mana": 0, "price": 45},
    {"name": "Ranger Clothes", "rank": "Rare", "defense": 3, "hp": 10, "mana": 10, "price": 48},
    {"name": "Knight Armor", "rank": "Super Rare", "defense": 7, "hp": 30, "mana": 0, "price": 85},
    {"name": "Mystic Robe", "rank": "Super Rare", "defense": 4, "hp": 15, "mana": 25, "price": 90},
    {"name": "Flame Guard", "rank": "Epic", "defense": 10, "hp": 40, "mana": 5, "price": 145},
    {"name": "Frost Armor", "rank": "Epic", "defense": 9, "hp": 35, "mana": 15, "price": 145},
    {"name": "Dragon Scale", "rank": "Mythical", "defense": 14, "hp": 60, "mana": 10, "price": 230},
    {"name": "Shadow Suit", "rank": "Mythical", "defense": 11, "hp": 40, "mana": 30, "price": 225},
    {"name": "Celestial Plate", "rank": "Legendary", "defense": 20, "hp": 90, "mana": 30, "price": 370},
    {"name": "Demon King's Robe", "rank": "Legendary", "defense": 17, "hp": 70, "mana": 50, "price": 365},
]

# There are 15 potions across healing, mana, mixed and buff types.
POTIONS = [
    {"name": "Small Health Potion", "kind": "hp", "amount": 50, "price": 10},
    {"name": "Medium Health Potion", "kind": "hp", "amount": 100, "price": 20},
    {"name": "Large Health Potion", "kind": "hp", "amount": 250, "price": 40},
    {"name": "Giant Health Potion", "kind": "hp", "amount": 500, "price": 70},
    {"name": "Ultimate Health Potion", "kind": "hp", "amount": 9999, "price": 100},
    {"name": "Small Mana Potion", "kind": "mana", "amount": 30, "price": 10},
    {"name": "Medium Mana Potion", "kind": "mana", "amount": 75, "price": 20},
    {"name": "Large Mana Potion", "kind": "mana", "amount": 150, "price": 40},
    {"name": "Giant Mana Potion", "kind": "mana", "amount": 300, "price": 70},
    {"name": "Ultimate Mana Potion", "kind": "mana", "amount": 9999, "price": 100},
    {"name": "Mixed Potion", "kind": "mixed", "amount": 100, "price": 45},
    {"name": "Strong Mixed Potion", "kind": "mixed", "amount": 250, "price": 80},
    {"name": "Attack Buff", "kind": "attack", "amount": 5, "price": 30},
    {"name": "Defense Buff", "kind": "defense", "amount": 5, "price": 30},
    {"name": "Critical Buff", "kind": "critical", "amount": 20, "price": 30},
]

ENEMY_NAMES = [
    "Goblin", "Wolf", "Slime", "Zombie", "Skeleton", "Orc", "Bandit",
    "Troll", "Dark Archer", "Giant Spider", "Vampire", "Werewolf",
    "Necromancer", "Ice Golem", "Fire Demon", "Sand Scorpion",
    "Desert Raider", "Mummy", "Stone Guard", "Cave Beast", "Castle Knight",
    "Lava Bug", "Frost Wolf", "Sky Harpy", "Demon Hound", "Lost Spirit",
    "Dark Mage", "Cursed Knight", "Ash Dragon", "Demon Soldier",
]

BOSSES = [
    "Goblin King", "Forest Guardian", "Ancient Golem", "Vampire Lord",
    "Dragon Rider", "Demon General", "Ice Titan", "Shadow Emperor",
    "Celestial Dragon", "Ancient Demon King",
]

REGIONS = [
    "Village", "Forest", "Cave", "Desert", "Ruins", "Castle",
    "Volcano", "Frozen Mountain", "Sky Temple", "Demon Realm",
]

SKILLS = {
    "Warrior": [("Slash", 5, 2), ("Shield Bash", 8, 2), ("Rage", 12, 3), ("Earthquake", 20, 4)],
    "Mage": [("Fireball", 8, 2), ("Ice Blast", 12, 3), ("Thunder Strike", 18, 4), ("Meteor", 28, 5)],
    "Archer": [("Multi Shot", 7, 2), ("Poison Arrow", 10, 3), ("Explosive Arrow", 17, 4), ("Sniper Shot", 25, 5)],
    "Assassin": [("Backstab", 6, 3), ("Smoke Bomb", 9, 2), ("Shadow Strike", 16, 4), ("Instant Kill", 25, 6)],
}


def make_player(name, player_class):
    # The classes start with different simple stats.
    stats = {
        "Warrior": (140, 25, 12, 8, 10),
        "Mage": (100, 80, 15, 3, 15),
        "Archer": (115, 50, 11, 5, 20),
        "Assassin": (95, 55, 14, 3, 25),
    }
    hp, mana, attack, defense, crit = stats[player_class]
    return {
        "name": name, "class": player_class, "level": 1, "exp": 0,
        "hp": hp, "max_hp": hp, "mana": mana, "max_mana": mana,
        "attack": attack, "defense": defense, "gold": 40,
        "crit": crit, "weapon": None, "armor": None,
        "potions": ["Small Health Potion", "Small Mana Potion"],
        "inventory": [], "bosses": [], "enemies": 0, "region": 0,
    }


def save_game(player):
    # Store one value per line so the save file is plain text and easy to read.
    weapon = player["weapon"]["name"] if player["weapon"] else ""
    armor = player["armor"]["name"] if player["armor"] else ""
    lines = [
        player["name"], player["class"], str(player["level"]), str(player["exp"]),
        str(player["hp"]), str(player["max_hp"]), str(player["mana"]),
        str(player["max_mana"]), str(player["attack"]), str(player["defense"]),
        str(player["gold"]), str(player["crit"]), weapon, armor,
        "|".join(player["potions"]), "|".join(item["name"] for item in player["inventory"]),
        "|".join(player["bosses"]), str(player["enemies"]), str(player["region"]),
    ]
    with open(SAVE_FILE, "w") as file:
        file.write("\n".join(lines))
    print("Game saved.")


def load_game():
    try:
        with open(SAVE_FILE, "r") as file:
            lines = file.read().splitlines()
        player = {
            "name": lines[0], "class": lines[1], "level": int(lines[2]), "exp": int(lines[3]),
            "hp": int(lines[4]), "max_hp": int(lines[5]), "mana": int(lines[6]),
            "max_mana": int(lines[7]), "attack": int(lines[8]), "defense": int(lines[9]),
            "gold": int(lines[10]), "crit": int(lines[11]), "weapon": None, "armor": None,
            "potions": lines[14].split("|") if lines[14] else [], "inventory": [],
            "bosses": lines[16].split("|") if lines[16] else [],
            "enemies": int(lines[17]), "region": int(lines[18]),
        }
        if lines[12]:
            player["weapon"] = next(item.copy() for item in WEAPONS if item["name"] == lines[12])
        if lines[13]:
            player["armor"] = next(item.copy() for item in ARMORS if item["name"] == lines[13])
        item_list = WEAPONS + ARMORS
        for name in lines[15].split("|"):
            for item in item_list:
                if item["name"] == name:
                    player["inventory"].append(item.copy())
                    break
        return player
    except (FileNotFoundError, ValueError, IndexError, StopIteration):
        print("There is no save file yet.")
        return None


def show_stats(player):
    weapon = player["weapon"]["name"] if player["weapon"] else "None"
    armor = player["armor"]["name"] if player["armor"] else "None"
    print("\n--- PLAYER STATS ---")
    print("Name:", player["name"], " Class:", player["class"])
    print("Level:", player["level"], " EXP:", player["exp"])
    print("HP:", player["hp"], "/", player["max_hp"], " Mana:", player["mana"], "/", player["max_mana"])
    print("Attack:", player["attack"], " Defense:", player["defense"], " Critical chance:", player["crit"])
    print("Gold:", player["gold"], " Weapon:", weapon, " Armor:", armor)
    print("Enemies defeated:", player["enemies"], " Bosses defeated:", len(player["bosses"]))


def level_up(player):
    needed = player["level"] * 20
    while player["exp"] >= needed and player["level"] < 100:
        player["exp"] -= needed
        player["level"] += 1
        player["max_hp"] += 12
        player["max_mana"] += 5
        player["attack"] += 2
        player["defense"] += 1
        player["hp"] = player["max_hp"]
        player["mana"] = player["max_mana"]
        print("Level up! You are now level", player["level"])
        if player["level"] % 5 == 0:
            print("You unlocked a stronger class skill!")
        needed = player["level"] * 20


def random_enemy(player, boss=False):
    level = player["level"]
    if boss:
        name = BOSSES[level // 10 - 1]
        return {"name": name, "hp": 100 + level * 12, "attack": 8 + level * 2,
                "defense": 3 + level, "boss": True}
    name = random.choice(ENEMY_NAMES[:min(5 + level // 3, len(ENEMY_NAMES))])
    return {"name": name, "hp": 25 + level * 7, "attack": 3 + level,
            "defense": level // 3, "boss": False}


def use_potion(player):
    if not player["potions"]:
        print("You have no potions.")
        return
    print("Potions:")
    for i, name in enumerate(player["potions"], 1):
        print(i, name)
    choice = input("Choose potion number (Enter to cancel): ")
    if not choice:
        return
    try:
        index = int(choice) - 1
        name = player["potions"][index]
    except (ValueError, IndexError):
        print("That choice is not valid.")
        return
    potion = next((item for item in POTIONS if item["name"] == name), None)
    if potion is None:
        player["potions"].remove(name)
        print("That potion could not be found.")
        return
    amount = potion["amount"]
    if potion["kind"] == "hp":
        player["hp"] = min(player["max_hp"], player["hp"] + amount)
        print("You restored health.")
    elif potion["kind"] == "mana":
        player["mana"] = min(player["max_mana"], player["mana"] + amount)
        print("You restored mana.")
    elif potion["kind"] == "mixed":
        player["hp"] = min(player["max_hp"], player["hp"] + amount)
        player["mana"] = min(player["max_mana"], player["mana"] + amount)
        print("You restored health and mana.")
    else:
        player[potion["kind"] + "_buff"] = amount
        print("The potion will help with your next battle.")
    player["potions"].remove(name)


def battle(player, boss=False):
    enemy = random_enemy(player, boss)
    defend = False
    turn = 0
    print("\nA", enemy["name"], "appeared!")
    while enemy["hp"] > 0 and player["hp"] > 0:
        turn += 1
        print("\nYour HP:", player["hp"], " Enemy HP:", enemy["hp"], " Mana:", player["mana"])
        print("1 Attack  2 Skill  3 Potion  4 Defend  5 Stats  6 Run")
        choice = input("Action: ")
        damage = 0
        if choice == "1":
            weapon_damage = player["weapon"]["damage"] if player["weapon"] else 0
            damage = player["attack"] + weapon_damage - enemy["defense"]
            if random.randint(1, 100) <= player["crit"]:
                damage *= 2
                print("Critical hit!")
        elif choice == "2":
            skills = SKILLS[player["class"]]
            unlocked = min(1 + (player["level"] - 1) // 5, len(skills))
            for i in range(unlocked):
                skill = skills[i]
                print(i + 1, skill[0], "Mana:", skill[1])
            try:
                number = int(input("Skill number (0 to cancel): "))
                skill = skills[number - 1]
                if number < 1 or number > unlocked:
                    raise ValueError
                if player["mana"] < skill[1]:
                    print("Not enough mana.")
                    continue
                player["mana"] -= skill[1]
                damage = player["attack"] * skill[2] - enemy["defense"]
                print("You used", skill[0])
            except (ValueError, IndexError):
                print("That skill choice is not valid.")
                continue
        elif choice == "3":
            use_potion(player)
            if player["hp"] > 0:
                continue
        elif choice == "4":
            defend = True
            print("You prepare to block half of the next attack.")
        elif choice == "5":
            show_stats(player)
            continue
        elif choice == "6" and not boss:
            print("You escaped.")
            return "run"
        else:
            print("Choose one of the listed actions.")
            continue

        if damage > 0:
            enemy["hp"] -= damage
            print("You dealt", damage, "damage.")
        if enemy["hp"] <= 0:
            break
        enemy_damage = max(1, enemy["attack"] - player["defense"])
        if boss and turn % 3 == 0:
            enemy_damage *= 2
            print(enemy["name"], "uses a special attack!")
        if defend:
            enemy_damage = max(1, enemy_damage // 2)
            defend = False
        player["hp"] -= enemy_damage
        print(enemy["name"], "dealt", enemy_damage, "damage.")

    if player["hp"] <= 0:
        print("You were defeated. Game over.")
        player["hp"] = 1
        return "dead"

    print("You defeated", enemy["name"], "!")
    if boss:
        player["bosses"].append(enemy["name"])
        player["gold"] += player["level"] * 20
        print("Boss defeated! The next region is open.")
    else:
        player["enemies"] += 1
        player["exp"] += 12 + player["level"] * 2
        player["gold"] += random.randint(5, 15) + player["level"]
        if random.randint(1, 100) <= 25:
            potion = random.choice(POTIONS[:12])
            player["potions"].append(potion["name"])
            print("Loot found:", potion["name"])
        level_up(player)
    return "win"


def show_inventory(player):
    print("\nPotions:", ", ".join(player["potions"]) if player["potions"] else "None")
    print("Items:")
    if not player["inventory"]:
        print("None")
    for i, item in enumerate(player["inventory"], 1):
        print(i, item["name"], "-", item["rank"])
    choice = input("Enter item number to equip, or press Enter: ")
    if choice:
        try:
            item = player["inventory"][int(choice) - 1]
            if "damage" in item:
                player["weapon"] = item
                print("Weapon equipped:", item["name"])
            else:
                player["armor"] = item
                player["defense"] += item["defense"]
                player["max_hp"] += item["hp"]
                player["max_mana"] += item["mana"]
                player["hp"] = min(player["hp"], player["max_hp"])
                print("Armor equipped:", item["name"])
        except (ValueError, IndexError):
            print("That item number is not valid.")


def shop(player):
    while True:
        print("\nVillage Shop - Gold:", player["gold"])
        print("1 Buy weapon  2 Buy armor  3 Buy potion  4 Sell an item  5 Leave")
        choice = input("Choose: ")
        if choice == "1":
            goods = WEAPONS
        elif choice == "2":
            goods = ARMORS
        elif choice == "3":
            goods = POTIONS
        elif choice == "4":
            if not player["inventory"]:
                print("You have no gear to sell.")
                continue
            for i, item in enumerate(player["inventory"], 1):
                print(i, item["name"], "sell price:", max(1, item["price"] // 2))
            try:
                item = player["inventory"].pop(int(input("Item number: ")) - 1)
                player["gold"] += max(1, item["price"] // 2)
                print("Item sold.")
            except (ValueError, IndexError):
                print("That choice is not valid.")
            continue
        elif choice == "5":
            return
        else:
            print("Choose 1 to 5.")
            continue
        for i, item in enumerate(goods, 1):
            print(i, item["name"], "-", item["price"], "gold")
        try:
            item = goods[int(input("Item number (0 to cancel): ")) - 1]
        except (ValueError, IndexError):
            continue
        if player["gold"] < item["price"]:
            print("You do not have enough gold.")
        else:
            player["gold"] -= item["price"]
            if "kind" in item:
                player["potions"].append(item["name"])
            else:
                player["inventory"].append(item.copy())
            print("Bought", item["name"])


def play(player):
    while True:
        if player["level"] >= 100 and BOSSES[-1] in player["bosses"]:
            print("\nYou defeated the Ancient Demon King and saved Eldoria!")
            print("Victory summary:")
            show_stats(player)
            save_game(player)
            return
        # A boss blocks each tenth level until it has been defeated.
        if player["level"] % 10 == 0 and player["level"] // 10 > len(player["bosses"]):
            print("A boss is blocking the way. Prepare before fighting!")
            boss_result = battle(player, True)
            if boss_result == "dead":
                return
            continue
        region = REGIONS[min(player["region"], len(REGIONS) - 1)]
        print("\n===", region, "| Level", player["level"], "| Gold", player["gold"], "===")
        print("1 Explore  2 Shop  3 Inventory  4 Stats  5 Save  6 Travel  7 Exit")
        choice = input("Choose: ")
        if choice == "1":
            result = battle(player)
            if result == "dead":
                return
        elif choice == "2":
            shop(player)
        elif choice == "3":
            show_inventory(player)
        elif choice == "4":
            show_stats(player)
        elif choice == "5":
            save_game(player)
        elif choice == "6":
            next_region = min(player["level"] // 10, len(REGIONS) - 1)
            if next_region > player["region"]:
                player["region"] = next_region
                print("Travelled to", REGIONS[next_region])
            else:
                print("Defeat the next boss to unlock a new region.")
        elif choice == "7":
            save_game(player)
            print("See you next time!")
            return
        else:
            print("Choose a number from 1 to 7.")


def main():
    print("=== LEGENDS OF THE FORGOTTEN REALM ===")
    while True:
        print("1 New Game  2 Continue  3 Instructions  4 Exit")
        choice = input("Choose: ")
        if choice == "1":
            name = input("Enter your hero name: ").strip()
            if not name:
                name = "Hero"
            print("1 Warrior  2 Mage  3 Archer  4 Assassin")
            classes = ["Warrior", "Mage", "Archer", "Assassin"]
            try:
                player_class = classes[int(input("Choose class: ")) - 1]
            except (ValueError, IndexError):
                print("Invalid class. Starting as Warrior.")
                player_class = "Warrior"
            player = make_player(name, player_class)
            play(player)
        elif choice == "2":
            player = load_game()
            if player:
                play(player)
        elif choice == "3":
            print("Explore to fight enemies, earn gold and experience, buy gear, and defeat each boss.")
            print("Save from the game menu. A boss appears when you reach each level ending in 0.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
