
import random

class TeamSort:

    def __init__(self): 
        self.temp_list = [ i for i in range(1,14) ]

        teams = ['Nebraska','Iowa','Minnesota','Northwestern','Illinois',
         'Michigan','Michigan State','Purdue','Indiana','Ohio State',
         'Penn State','Rutgers','Maryland']

        random.shuffle(teams)

        self.teams_stats = { i:[teams[i-1],0,0,0] for i in range(1,14) }
 

team_sort = TeamSort()

def print_weekly_match(week_match):
    print('===================================================')
    print('{} hosts {} and {}.'.format(team_sort.teams_stats[week_match[0]][0],
                                      team_sort.teams_stats[week_match[1]][0],
                                      team_sort.teams_stats[week_match[2]][0]))
    print('===================================================')

week_1_match = [ i for i in range(1, 14) ]
random.shuffle(week_1_match)
team_sort.update_stats(week_1_match)
print('====================================================')
print('========WEEK 1 MATCHUPS=============================')
print_weekly_match(week_1_match)
print(team_sort.teams_stats)




week_2_match = team_sort.calc_week_match()
random.shuffle(week_2_match)
team_sort.update_stats(week_2_match)
print('====================================================')
print('========WEEK 2 MATCHUPS=============================')
print_weekly_match(week_2_match)

print(team_sort.teams_stats)



week_3_match = team_sort.calc_week_match()
random.shuffle(week_3_match)
team_sort.update_stats(week_3_match)
print('====================================================')
print('========WEEK 3 MATCHUPS=============================')
print_weekly_match(week_3_match)

print(team_sort.teams_stats)



week_4_match = team_sort.calc_week_match()
random.shuffle(week_4_match)
team_sort.update_stats(week_4_match)
print('====================================================')
print('========WEEK 4 MATCHUPS=============================')
print_weekly_match(week_4_match)

print(team_sort.teams_stats)



    
