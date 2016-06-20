
import random

class TeamSort:

    def __init__(self): 
        self.temp_list = [ i for i in range(1,14) ]

        teams = ('Nebraska','Iowa','Minnesota','Northwestern','Illinois',
         'Michigan','Michigan State','Purdue','Indiana','Ohio State',
         'Penn State','Rutgers','Maryland')

        self.teams_stats = { i:[teams[i-1],0,0,0] for i in range(1,14) }
 
    def eliminate_prior_3_hosts(self, fewest_home):
        removal_list = []
        for team in fewest_home:
            if self.teams_stats[team][1] % 3 != 0:
                removal_list.append(team)
        for team_to_remove in removal_list:
                fewest_home.remove(team_to_remove)
        return fewest_home

    def eliminate_prior_3_away(self, fewest_away):
        removal_list = []
        for team in fewest_away:
            if self.teams_stats[team][3] > 0:
                removal_list.append(team)
        for team_to_remove in removal_list:
            fewest_away.remove(team_to_remove)
        return fewest_away

    def select_fewest_home(self):
        fewest_home = [ ]
        for i in range(0, 20):
            for j in self.temp_list:
                if self.teams_stats[j][1] == i:
                    fewest_home.append(j)
        return fewest_home

    def select_fewest_away(self):
        fewest_away = [ ]
        for i in range(0, 20):
            for j in self.temp_list:
                if self.teams_stats[j][2] == i:
                    fewest_away.append(j)
        return fewest_away

    def select_3_home(self):
        fewest_home = self.select_fewest_home()
        fewest_home_filtered = self.eliminate_prior_3_hosts(fewest_home)
        return fewest_home_filtered[0]
        
    def select_3_away(self):
        fewest_road = self.select_fewest_away()
        fewest_road_filtered = self.eliminate_prior_3_away(fewest_road)
        return fewest_road_filtered[0:2]

    def select_2_homes(self):
        fewest_home = self.select_fewest_home()
        return fewest_home[0:5]

    def calc_week_match(self):
        self.temp_list = [ i for i in range(1,14) ]
        week_match = [ ]
        three_home = self.select_3_home()
        week_match.append(three_home)
        three_away1, three_away2 = self.select_3_away()
        week_match.append(three_away1)
        week_match.append(three_away2)
        self.temp_list = [ i for i in range(1,14) ]
        print('***: ',self.temp_list)
        self.temp_list.remove(three_home)
        self.temp_list.remove(three_away1)
        self.temp_list.remove(three_away2)
        print('***: ',self.temp_list)
        homes = self.select_2_homes()
        for home in homes:
            week_match.append(home)
            self.temp_list.remove(home)
            print('***: ',self.temp_list)
        
        for away in self.temp_list:
            week_match.append(away)
            print('***: ',self.temp_list)
        print(week_match)
        return week_match
        
        
    def update_stats(self, matchups):
        self.teams_stats[matchups[0]][1]+=4
        self.teams_stats[matchups[0]].append(matchups[1])
        self.teams_stats[matchups[0]].append(matchups[2])
        self.teams_stats[matchups[1]][2]+=2
        self.teams_stats[matchups[1]][3]+=2
        self.teams_stats[matchups[1]].append(matchups[0])
        self.teams_stats[matchups[1]].append(matchups[2])
        self.teams_stats[matchups[2]][2]+=2
        self.teams_stats[matchups[2]][3]+=2
        self.teams_stats[matchups[2]].append(matchups[0])
        self.teams_stats[matchups[2]].append(matchups[1])
        self.teams_stats[matchups[3]][1]+=3
        self.teams_stats[matchups[3]].append(matchups[8])
        self.teams_stats[matchups[4]][1]+=3
        self.teams_stats[matchups[4]].append(matchups[9])
        self.teams_stats[matchups[5]][1]+=3
        self.teams_stats[matchups[5]].append(matchups[10])
        self.teams_stats[matchups[6]][1]+=3
        self.teams_stats[matchups[6]].append(matchups[11])
        self.teams_stats[matchups[7]][1]+=3
        self.teams_stats[matchups[7]].append(matchups[12])
        self.teams_stats[matchups[8]][2]+=3
        self.teams_stats[matchups[8]].append(matchups[3])
        self.teams_stats[matchups[9]][2]+=3
        self.teams_stats[matchups[9]].append(matchups[4])
        self.teams_stats[matchups[10]][2]+=3
        self.teams_stats[matchups[10]].append(matchups[5])
        self.teams_stats[matchups[11]][2]+=3
        self.teams_stats[matchups[11]].append(matchups[6])
        self.teams_stats[matchups[12]][2]+=3
        self.teams_stats[matchups[12]].append(matchups[7])

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



    
