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
t_time_hrs = 3                   #time of study desired (in hours)
stime = 1730                     #suspected class timing in hours (edit this) if no class is suspected, set to 2400
t_time = t_time_hrs * 60
sub_time = int(t_time/3)                    #amount of time per subject (in minutes)
len_break = int(sub_time/4)                   #amount of time per break (in minutes)
_stime = int(str(stime)[0:-2])*60 + int(str(stime)[-2:4])
start_time = int(str(input_start_time)[0:-2])*60 + int(str(input_start_time)[-2:4])

#creates time slots
times = []
ntime = int(start_time)
while abs(ntime-_stime) > sub_time:
    times += [to12hr(ntime)+' to '+to12hr(ntime+sub_time)] + [to12hr(ntime+sub_time)+' to '+to12hr(ntime+sub_time+len_break)]
    ntime += sub_time + len_break
mtime = _stime + 60
temp_time = mtime - ntime
end_time = start_time + temp_time + sub_time*3 + len_break*2
ntime = mtime
while ntime < end_time:
    times += [to12hr(ntime)+' to '+to12hr(ntime+sub_time)] + [to12hr(ntime+sub_time)+' to '+to12hr(ntime+sub_time+len_break)]
    ntime += sub_time + len_break

job = []
i = 0
while i < 5:
    o = np.random.choice([0,1,2])
    if subs[o] not in job:
        job += [subs[o]]
        i += 1
        if i != 5:
            job += ['Break']
            i += 1

tt = {times[0]:job[0], times[1]:job[1], times[2]:job[2], times[3]:job[3], times[4]:job[4]}

f = open('today.txt','w+')
for i in range(len(tt)):
    f.write(times[i]+' '+tt[times[i]])
    f.write('\n')
f.close()