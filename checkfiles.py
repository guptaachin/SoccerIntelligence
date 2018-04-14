import os


files_present = set(os.listdir(os.getcwd()+'/newdata/stat/'))
files_should_be_present = set()
# print(len(files_present))

f = open('newdata/team.txt', 'r')
content = f.readlines()
count = 0
for line in content:
    team_id = line.rstrip()
    # curr_file = 'players'+str(team_id)+'.json'
    # if(curr_file in files_should_be_present):
    #     print(team_id)
    files_should_be_present.add(team_id)

f_present = set()
for entry in files_present:
    spl = entry.split('_')[4]
    f_present.add(spl)

print(files_should_be_present - f_present)

# print(len(files_should_be_present))
#
# print(files_present-files_should_be_present)