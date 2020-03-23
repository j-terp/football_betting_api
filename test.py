from test4 import info as stat_input
match_stat = {}

for x in range(int(len(stat_input) / 3)):
    match_stat[stat_input[1]] = [stat_input[0], stat_input[2]]
    stat_input = stat_input[3:]
print("")
print(match_stat)