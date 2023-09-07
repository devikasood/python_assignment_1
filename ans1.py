subj_1 = int(input("enter the marks for subject 1: "))
subj_2 = int(input("enter the marks for subject 2: "))
subj_3 = int(input("enter the marks for subject 3: "))
                
avg = (subj_1+subj_2+subj_3)/3

if avg>= 40:
    print("pass")
else:
    print("fail")
