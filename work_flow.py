import os
import sys
import time

databases = ['CVD2014', 'LIVE-Qualcomm']
exp_ids = [i for i in range(10)]
c = 1
sum = 0
for database in databases:
    total = int(len(exp_ids)*len(databases))
    for exp_id in exp_ids:
        print('\nProgress {}/{}'.format(c, total))
        # database = 'CVD2014'
        start = time.time()
        os.system('python VSFA.py --epoch 10 --database {} --exp_id {} >tmp.txt'.format(database, exp_id))
        with open("tmp.txt", "r") as file:
            lines = file.readlines()
            with open("log.txt", "a") as f:
                f.write(lines[0])
                f.write(lines[1])
                f.write(lines[-2])
                f.write('\n')
        end = time.time()
        times = round((end-start)/60)
        print('It takes {} mins'.format(times))
        sum += times
        if c != len(exp_ids):
            ava = sum/c
            rest = ava*(total-c)
            print('Estimated remaining time: {} mins.'.format(rest))
        c += 1
sys.exit()
