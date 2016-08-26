import os
import time

for year in range(2000,2017):
  for qtr in ['QTR1','QTR2','QTR3','QTR4']:
    os.system('mkdir %s-%s' % (year,qtr))
    with open('%s-%s.idx' % (year,qtr)) as f:
        lines = f.readlines()
        for id,line in enumerate(lines):
           split_ = line.split('|')
           if len(split_) < 4: continue
           if '13F' in split_[2]:
               url  = split_[4]
               file = url.split('/')[-1]
               print url
               print 'ftp  ftp://ftp.sec.gov/%s .' % (url)
               os.system('ftp  ftp://ftp.sec.gov/%s .' % (url))
               print 'mv *.txt %s-%s' % (year,qtr)
               os.system('mv *.txt %s-%s' % (year,qtr))

               time.sleep(1.25)
