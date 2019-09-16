import random
class Hero:
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = self.start_health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        total = 0
        if self.health > 0:
            for i in range(0,len(self.armors)):
                total += self.armors[i].defend()
        return total

    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_armor(self, armor):
        self.armors.append(armor)


    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        total = 0
        for abilities in self.abilities:
            total += abilities.attack()
        return total



class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        lowest_attack = self.attack_strength // 2
        random_attack = random.randint(lowest_attack, self.attack_strength)
        return random_attack

    def update_attack(self, attack):
        Ability.attack_strength = attack

class Weapon(Ability):

    def attack(self):
        random_weapon_attack = random.randint(0, self.attack_strength)
        return random_weapon_attack

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)


    def has_hero(self):
        hero_list = list()
        for h in range(0,len(self.heroes)):
            if self.heroes[h] > 0:
                hero_list.append(True)
            else: hero_list.append(False)
        if all(hero_list) == True:
            return True
        else: return False

    def remove_hero(self, name):
        for i in range(0, len(self.heroes)):
            if self.heroes[i] == name:
                self.heroes.pop(i)
        return 0

    def find_hero(self, name):
        for i in range(0, len(self.heroes)):
            if self.heroes[i].name == name:
                return self.heroes[i]
        return 0

    def view_all_heroes(self):
        for i in range(0,len(self.heroes)):
            print(self.heroes[i].name)

    def attack(self, other_team):
        total_attack = 0
        kills = 0
        for i in range(0,len(self.heroes)):
            total_attack += self.heroes[i].attack()
        other_team.defend(total_attack)
        for e in range(0,len(other_team.heroes)):
            if other_team.heroes[e].health <= 0:
                kills += 1
                self.heroes[i].add_kills(kills)



        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
    def defend(self, damage_amt):
        total = 0
        total_kills = 0
        for i in range(0,len(self.heroes)):
            total += self.heroes[i].defend()
        damage_taken = damage_amt - total
        self.deal_damage(damage_taken)

        for i in range(0,len(self.heroes)):
            if self.heroes[i].health <= 0:
                total_kills += 1
        return total_kills

        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        Return number of heroes killed in attack.
        """

    def deal_damage(self, damage):
        damage_per_hero = damage // len(self.heroes)
        total_dead = 0

        for i in range(0,len(self.heroes)):
            self.heroes[i].take_damage(damage_per_hero)
            if self.heroes[i].health <= 0:
                total_dead += 1
        return total_dead
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

    def revive_heroes(self, health=100):
        for i in range(0,len(self.heroes)):
            self.heroes[i].health = self.heroes[i].start_health
        """
        This method should reset all heroes health to their
        original starting value.
        """

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """

    def update_kills(self):
        self.heroes
        """
        This method should update each hero when there is a team kill.
        """

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense
    def defend(self):
        return random.randint(0, self.defense)


class Arena:
    def __init__(self):
        """
        Declare variables
        """
        self.team_one = Team
        self.team_two = Team

    def build_team_one(self):
        user_input = input()
        isfinished = True
        team_name = input("Enter a name for team 1: \n")
        team = Team(team_name)
        while isfinished:
            hero_name = input("Enter a name for your hero: \n")
            hero_health = int(input("Enter a starting health value for out Hero: \n"))
            hero = Hero(hero_name,hero_health)
            team.add_hero(hero)
            add_hero = input("Add another hero? y/n: \n")
            if add_hero.lower() == "y":
                hero_name
                hero_health
            else:
                return False
        self.team_one = team

        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):

        user_input = input()
        isfinished = True
        team_name = input("Enter a name for team 2: \n")
        team = Team(team_name)
        while isfinished:
            hero_name = input("Enter a name for your hero: \n")
            hero_health = int(input("Enter a starting health value for yout Hero: \n"))
            hero = Hero(hero_name,hero_health)
            team.add_hero(hero)
            add_hero = input("Add another hero? y/n: \n")
            if add_hero.lower() == "y":
                hero_name
                hero_health
            else:
                return False
        self.team_two = team

        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        while self.team_one.has_hero == True and self.team_two.has_hero == True:
            print("team_battle")
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        for h in self.team_one.heroes:
            print("{} has gotten {} kills, and {} deaths".format(h2.name, h2.kills, h2.deaths))
        for h2 in self.team_two.heroes:
            print("{} has gotten {} kills, and {} deaths".format(h2.name, h2.kills, h2.deaths))
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
