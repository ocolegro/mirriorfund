import os

for year in range(2000,2017):
  for qtr in ['QTR1','QTR2','QTR3','QTR4']:
    os.system('ftp  ftp://ftp.sec.gov/edgar/full-index/%s/%s/master.idx .' % (year,qtr))
    os.system('mv master.idx %s-%s.idx' % (year,qtr))
