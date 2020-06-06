import numpy as np

def to12hr(x): #converts minutes to time of day
    if x > 1440:
        x -= 1440
    hours = int(x/60)
    mins = x - hours*60
    if len(str(mins)) == 1:
        a = '0'+str(mins)
    else:
        a = str(mins)
    if hours >= 12:
        hours -= 12
        d = str(hours)
        if len(d) == 1:
            d = '0'+d
        return d+':'+a+' p.m.'
    else:
        d = str(hours)
        if len(d) == 1:
            d = '0'+d
        return d+':'+a+' a.m.'

subs = ['Physics','Chemistry','Math']
input_start_time = 1500          #in hours (edit this)
input_end_time = 1930            #in hours (edit this)
t_time_hrs = 3                   #time of study desired (in hours)
stime = 1630                     #suspected class timing in hours (edit this)
t_time = t_time_hrs * 60
sub_time = 60                    #amount of time per subject (in minutes)
len_break = 15                   #amount of time per break (in minutes)
_stime = int(str(stime)[0:-2])*60 + int(str(stime)[-2:-1])
start_time = int(str(input_start_time)[0:-2])*60 + int(str(input_start_time)[-2:-1])
end_time = int(str(input_end_time)[0:-2])*60 + int(str(input_end_time)[-2:-1])

#creates time slots
times = []
ntime = int(start_time)
while ntime < _stime:
    times += [to12hr(ntime)+' to '+to12hr(ntime+sub_time)] + [to12hr(ntime+sub_time)+' to '+to12hr(ntime+sub_time+len_break)]  
    ntime += sub_time + len_break
ntime += 60
while ntime < end_time:
    times += [to12hr(ntime)+' to '+to12hr(ntime+sub_time)]
    if ntime + sub_time < end_time:
        times += [to12hr(ntime+sub_time)+' to '+to12hr(ntime+sub_time+len_break)]
    ntime += sub_time + len_break

job = []
c = int(len(times)/2)+1
for i in range(c):
    job += [subs[np.random.choice([0,1,2])]]
    if i != c-1:
        job += ['Break']

tt = {times[0]:job[0], times[1]:job[1], times[2]:job[2], times[3]:job[3], times[4]:job[4]}

f = open('today.txt','w+')
for i in range(len(tt)):
    f.write(times[i]+' '+tt[times[i]])
    f.write('\n')
f.close()