import sys
f = open(sys.argv[1]).read().split('\n')[0].split('\t')
total_mpids_before = 0
for i in range(len(f)):
    if 'mpid' in f[i]:
        total_mpids_before += 1
    if sys.argv[2] in f[i]:
        print total_mpids_before

