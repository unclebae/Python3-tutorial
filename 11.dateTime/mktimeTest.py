import time

t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)
d=time.mktime(t)
print ("time.mktime(t) : %f" %  d)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(d)))
