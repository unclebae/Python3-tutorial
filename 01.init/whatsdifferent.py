#Python3
#1. 파이선2에서 파이선3 모듈을 이용하고자 한다면 다음과 같이 사용해야한다. 
#from __future__ import division

#2. print 함수 사용방법 변경
#python3에서는 print 함수를 이용하기 위해서 ()를 꼭 써주어야한다. 
#print "Hello World" # Python2에서는 가능
print ("Hello World") # Python3에서는 반드시 ()를 이용해야함. 

#파이선에서기본적으로 뉴라인 캐릭터를 인서트 하고 있다. 
# 파이선 2에서는 마지막에 ','를 입력하여 이를방지할 수 있었다. 
# 파이선 3에서는 "end=' '" 를 추가하면된다. 
x = 5
#print x,  # python2
print (x, end=" ") 

#3. keyboard로부터 입력값 읽기
# 파이선2에서는 input()과 raw_input()2가지의 함수를 가지고 있다. 
# input()함수는 ''이나 ""으로 묶은 내용은 스트링으로 받아들이고, 나머지 케이스에서는 숫자로 받는다. 
# 파이선3에서는 raw_input()함수는 디프리케이트되었다. 
# 즉, 모든 데이터는 스트링으로 처리된다.

#Python2
#>>> x=input('something:')
#something:10
#10
#>>> x=input('something:')
#something:'10'
#'10'
#>>> x=raw_input("something:")
#something:10
#'10'
#>>> x=raw_input("something:")
#something:'10'
#"'10'"

#Python3
x=input("something:")
#something:10
print(x)
#'10'
#something:'10'
#"'10'"
#x=raw_input("something:") # will result NameError
 
# 3. Integer division
# 파이선2에서는 2개의 정수를 나누면 가장 가까운 정수값으로 변환하여 출력한다.. 
# 즉, 3/2는 결과는 1이다. 
# 소수점을 출력하기 위해서는 float로 변환한 값으로 나누어야한다. 
# 즉, 3.0/2, 3/2.0, 3.0/2.0 등으로 표현해야한다. 

# 파이선 3에서는 3/2는 1.5가 기본이다. 더 직관적으로 변경이 되었다. 

# 4. 유니코드 표기
# 파이선2에서는 유니코드로 문자를 저장하기위해서는 u마크를 해주어야한다. 
# 파이선3에서는 기본이 유니코드이다. (utf-8)을 기본으로 한다. 

# 5.xrange() 함수 제거
# 파이선 2에서는 range()함수는 리스트를 반환하여다. 그리고 xrange()는 객체를 반환했다. 
# 이는 메모리 절약을 위해서 사용된 기법이다. 
# 파이선 3에서는 range()함수는 사라지고, xrange() 함수는 range()로 이름이 변경되었다. 
# 추가적으로 range()객체는 python 3.2이후 버젼에서는 slicing 기능을 제공한다. 

# 6.raise exception
# 파이선 2에서는 2개의 표기법으로 모두 사용이 가능했다. 'old'와 'new'문법 모두 사용이 가능했다. 
# 파이선 3에서는 예외발생시 아규먼트를 괄호안에 넣지 않으면 오류가 발생한다. 
# raise IOError, "file error" # this is accepted in Python 2
# raise IOError("file error") # this is also accepted in Python 2
# raise IOError, "file error" # syntax error is raised in Python 3
# raise IOError("file error") # this is the recommended syntax in python 3 

# 7.Arguments in Exception
# 파이선 3에서 아규먼트들은 as키워드로 예외를 설정할 수 있다. 
# except Myerror, err: # In Python2
# except Myerror as err: # In Python3

# 8. next() function and .next() method
# 파이선 2에서 next()는 객체를 생성하는 메소드로 사용이 가능했다. 
# 파이선 2에서 next() 함수는 생성된 객체의 iterator를 위해 사용이 가능했다. 
# 파이선 3에서는 next() 생성 메소드는 중단되었으며, AttributeError를 발생시킨다. 

# gen = (letter for letter in 'Hello World') # creates generator object
# next(my_generator) # 파이선2, 3에서 모두 사용가능
# my_generator.next() # 파이선2에서는 가능하나. 3에서는 AttributeError을 발생

# 9. 2to3 Utility
# 파이선 3 인터프리터와 함께 2to3.py 스크립트는 tools/scripts 폴더에 설치된다. 
# 이는 파이선 2.x 소스코드를 읽고 valid한 Python3 로 변환한다. 

#Here is a sample Python 2 code (area.py):
#
#def area(x,y=3.14): 
#    a=y*x*x
#    print a
#    return a
#
#a=area(10)
#print "area",a
#
#To convert into Python 3 version:
#
#$2to3 -w area.py
#
#Converted code :
#
#def area(x,y=3.14): # formal parameters
#    a=y*x*x
#    print (a)
#    return a
#
#a=area(10)
#print("area",a)
#

# 2to3 변환과정 

#UncleBae:01.init Coupang$ 2to3 -w python2code.py
#RefactoringTool: Skipping implicit fixer: buffer
#RefactoringTool: Skipping implicit fixer: idioms
#RefactoringTool: Skipping implicit fixer: set_literal
#RefactoringTool: Skipping implicit fixer: ws_comma
#RefactoringTool: Refactored python2code.py
#--- python2code.py	(original)
#+++ python2code.py	(refactored)
#@@ -1,7 +1,7 @@
# def area(x, y=3.14):
#     a=y*x*x
#-    print a
#+    print(a)
#     return a
#
# a = area(10)
#-print "area", a
#+print("area", a)
#
