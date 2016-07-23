intab = "aeiouxm"
outtab = "1234512"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!";
print (str.translate(trantab))
