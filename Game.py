from Characters import Character, Character1, Character2, Character3
# ... (same code as before)

class DuelSimulator:
    def simulate_battle(self, team1, team2):
        print("GAME START !")
        while any(charac.isAlive() for charac in team1 + team2):
            for attacker, defender in zip(team1, team2):
                attack_strength = attacker.calculate_attack  # Call attack() as a method
                if (defender.hit(attack_strength())) :
                    defender.hit(attack_strength())
                    print(f"{attacker.name} did -{attack_strength()} from {defender.name}.")
                    defender.print_info()
                    if not defender.isAlive():
                        print(f"{defender.name} is DEAD")
                        break  # Break the loop if the defender is not alive

            for attacker, defender in zip(team2, team1):
                attack_strength = attacker.calculate_attack  # Call attack() as a method
                if (defender.hit(attack_strength())) :
                    defender.hit(attack_strength())
                    print(f"{attacker.name} did -{attack_strength()} from {defender.name}.")
                    defender.print_info()
                    if not defender.isAlive():
                        print(f"{defender.name} is DEAD")
                        break  # Break the loop if the defender is not alive
        



char1 = Character1("char1", 20, 100)
char2 = Character2("char2", 15, 80)
char3 = Character3("char3", 18, 90)

char11 = Character1("char11", 22, 110)
char22 = Character2("char22", 17, 85)
char33 = Character3("char33", 16, 95)

# Simulate a 2v2 battle
team1 = [char1, char2, char3]
team2 = [char11, char22, char33]

DuelSimulator().simulate_battle(team1, team2)
