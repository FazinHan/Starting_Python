import numpy as np

def to12hr(x): #converts minutes to time of day in 12 hour format
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
        if d == '0':
            d = '12'
        if len(d) == 1:
            d = '0'+d
        return d+':'+a+' p.m.'
    else:
        d = str(hours)
        if d == '0':
            d = '12'
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
_id = 1
ntime = int(start_time)
_try = 0
a_class = 0
i = 0
while _try <= 2:
    if _id == 1:
        if sub_time <= _stime - ntime:
            times += [to12hr(ntime)+' to '+to12hr(ntime+sub_time)]
            ntime += sub_time
            _id = 0
            i += 1
        else:
            _try += 1
    elif _id == 0:
        if len_break <= _stime - ntime:
            times += [to12hr(ntime)+' to '+to12hr(ntime+len_break)]
            ntime += len_break
            _id = 1
            i += 1
        else:
            _try += 1
ntime += (_stime-ntime) + 60
while i < 5:
    if _id == 1:
        times += [to12hr(ntime)+' to '+to12hr(ntime+sub_time)]
        ntime += sub_time
        _id = 0
        i += 1
    else:
        times += [to12hr(ntime)+' to '+to12hr(ntime+len_break)]
        ntime += len_break
        _id = 1
        i += 1

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

f = open('today.txt','w+')
for i in range(len(times)):
    f.write(times[i]+' '+job[i])
    if i != len(times)-1:
        f.write('\n')
f.close()