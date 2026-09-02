Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#3.if..elif..else - if a single value to be checked with multiple test conditions
mark = 40
if mark >=91 and mark <=100:
    print(mark ,'A+ grade')
elif mark >=81 and mark <=90:
    print (mark,'A grade')
elif mark >=71 and mark <= 80:
    print (mark, 'B grade')
elif mark >=61 and mark <=70:
    print(mark, 'Cgrade')
elif mark >=51 and mark <=60:
    print(mark,'D grade')
elif mark >=41 and mark <=50:
    print (mark,'E grade fail')
else:
    print('enter valid mark')

    
enter valid mark
mark = 50
if mark >=91 and mark <=100:
    print(mark ,'A+ grade')
elif mark >=81 and mark <=90:
    print (mark,'A grade')
elif mark >=71 and mark <= 80:
    print (mark, 'B grade')
elif mark >=61 and mark <=70:
    print(mark, 'Cgrade')
elif mark >=51 and mark <=60:
    print(mark,'D grade')
elif mark >=41 and mark <=50:
    print (mark,'E grade fail')
else:
    print('enter valid mark')

    
50 E grade fail
#4.Nested if  - if one test condition is given inside another test condition
age = 16
weight = 53
if age >= 15:
    print('age wise eligible')
    if weight >= 50:
        print('eligible to donate blood')
    else:
        print('age criteria not matched')

        
age wise eligible
eligible to donate blood


