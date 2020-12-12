"""
ID: yscript1
LANG: PYTHON3
TASK: milk2
"""
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
num_of_farmers = int( fin.readline().strip() )
time_frames = []
for i in range(num_of_farmers):
    s, e = map(int, fin.readline().strip().split() )
    time_frames.append( { 'start':s, 'end': e})

# we need sort the time_frame first, to make sure the earlier the first
time_frames = sorted(time_frames, key=lambda k:k['start'])


current_start = time_frames[0]['start']
current_end = time_frames[0]['end']
longest_cont = current_end - current_start
longest_idle = 0

for i in range(num_of_farmers  - 1):
    pos = i + 1
    if time_frames[pos]['start']<=current_end:
        if time_frames[pos]['end']>current_end:
            current_end = time_frames[pos]['end']
            # extend current_start,current_end to longer frame
            if current_end - current_start > longest_cont:
                longest_cont = current_end - current_start
        # else: ignore it because current farmer is within the last time frame
    else:  # not continue, caculate continue time, start idle time
        if time_frames[pos]['start'] - current_end > longest_idle:
            longest_idle = time_frames[pos]['start'] - current_end
        # update current time frame to new farmer
        current_start = time_frames[pos]['start']
        current_end = time_frames[pos]['end']
        if current_end - current_start > longest_cont:
            longest_cont = current_end - current_start

fout.write (str(longest_cont) + ' ' + str(longest_idle) + '\n')
fout.close()