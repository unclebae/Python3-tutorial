seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict))

values = ('kido', '39', 'Male')
dict = dict.fromkeys(seq, values)
print("New Dictionary with values is not work... : %s" % str(dict))
