from random import shuffle

def calc_rounds(list):
	if(len(list) <= 19 and len(list) >= 14):
		rounds = 5
	elif(len(list) <= 13 and len(list) >= 10):
		rounds = 4
	elif(len(list) <= 9 and len(list) >= 7):
		rounds = 3
	elif(len(list) <= 6 and len(list) >= 4):
		rounds = 3
	elif(len(list) <= 3 and len(list) >= 2):
		rounds = 2
	else:
		rounds = 1

	return rounds

def calc_offer(suitcases, selection):
	if(selection < round(sum(suitcases.values()) / len(suitcases))):
		return 0.8*round(sum(suitcases.values()) / len(suitcases))
	else:
		return 1.2*round(sum(suitcases.values()) / len(suitcases))

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
values = [0.1, 1, 5, 10, 50, 100, 250, 500, 750, 1000, 2000, 4000, 8000, 10000, 15000, 20000, 30000, 50000, 75000, 100000]
shuffle(values)
suitcases = dict(zip(keys, values))
values.sort()

selection = input(
	f'''\nWelcome to the DEAL!\nThere are 20 suitcases you can choose from, with the following amounts:
{', '.join(["${:,.2f}".format(integer) for integer in values])}\n
Please pick one of the following suitcases:
{', '.join([str(integer) for integer in keys])}
''')

while(True):
	if int(selection) not in keys:
		selection = input("Wrong input. Please select a number from 1 to 20: ")
	else:
		print(f"Your selected suitcase is {selection}\n")
		break

selection_value = suitcases.pop(int(selection))

rounds = 0
round_name = 0

while len(suitcases) > 0:

	if(rounds == calc_rounds(suitcases)):
		rounds = 0
		round_name += 1
		print(f"Round {round_name} is complete. The banker offers you {round(calc_offer(suitcases, selection_value))} to sell your suitcase and finish the game. Press 'y' to sell your suitcase, or 'n' to continue playing: ")
		choice = input()
		while(True):
			if choice not in ['y', 'n']:
				choice = input("Wrong input. Please press 'y' or 'n': ")
			else:
				if choice == 'y':
					print(f"\n\nSOLD! You sold suitcase {selection}, which contained {selection_value}, for {round(calc_offer(suitcases, selection_value))}!")
					exit()
				else:
					print(f"Continuing to Round {round_name+1}")

				break


		print(selection_value)
		print(round(sum(suitcases.values()) / len(suitcases)))
		print(calc_offer(suitcases, selection_value))

	opened_sc = input(f"Open one of the following suitcases:\n{', '.join([str(integer) for integer in suitcases.keys()])}\n")

	while(True):
		if int(opened_sc) not in suitcases.keys():
			opened_sc = input("Wrong input. Please select a valid suitcase: ")
		else:
			tmp = "${:,.2f}".format(suitcases.pop(int(opened_sc)))
			print(f"You opened suitcase {opened_sc}, which contains {tmp}!")
			rem_amounts = list(suitcases.values())
			rem_amounts.append(selection_value)
			rem_amounts.sort()
			print(f'''Remaining amounts:\n{', '.join(["${:,.2f}".format(integer) for integer in rem_amounts])}\n''')
			rounds += 1
			break



# print(list(suitcases.values))
print(sum(suitcases.values()))
print(round(sum(suitcases.values()) / len(suitcases)))


# print(list(suitcases.keys()))
# print(suitcases)
# print(selection)
# print(len(suitcases))
