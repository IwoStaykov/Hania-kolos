
req_list = input().split() #wprowadzenie N, M i T
req_list = [int(req_list[i]) for i in range(3)]
#req_dict = {'N': req_list[0], 'M': req_list[1], 'T': req_list[2]}

teams = {}
for i in range(req_list[0]):
    name = input() #
    teams[name] = [0,0] # pierwszy element listy to liczba wygranych , drugi element to liczba rozegranych meczy
# teams['colorado'].append(2)

for i in range(req_list[1]):
    match_note = input().split(':') #wpisanie wyników
    if match_note[2] > match_note[3]:
        teams[match_note[0]][0] += 1 #dodaj 1 do wygranych dla pierwszego gracza
    else:
        teams[match_note[1]][0] += 1 #dodaj 1 do wygranych dla drugiego gracza
    teams[match_note[0][1]] += 1 #dodaj 1 do rozegranych meczy
    teams[match_note[1][1]] += 1

for i in range(req_list[0]):


print(teams['colorado'])
print(teams['new york'])