import re

phone = "2004-955-559 # This is Phone Number"

# 커멘트에 해당하는 내역을 제거한다. 
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# digits 가 아닌것을 제거한다. 
num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)
