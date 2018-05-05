import re

path = "/home/achin/Desktop/stats_team/player_stat.ttl"
path_new = "/home/achin/Desktop/stats_team/player_stat_integer.ttl"

ttl_file = open(path, 'r')

ttl_new = open(path_new, 'w')

all_lines = ttl_file.readlines()


for line in all_lines:
    spl_lines = line.split(" ")
    if(len(spl_lines)>2):
        m = re.match('\"\d+.\d*\"', spl_lines[2])
        # print(spl_lines[2])
        if m:
            # print(m)
            f_line = " ".join(spl_lines[:2])
            f_line += " \""+str(int(float(m.group(0).replace("\"", ""))))+"\""+"^^xsd:int"
            f_line += " .\n"
        else:
            f_line = line+'\n'
        print(f_line)
        # input()
        ttl_new.write(f_line)

ttl_new.close()