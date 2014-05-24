import math
asks = ["Input 1 for a^x = b", "Input 2 for a^x > b",
       "Input 3 for a^x < b", "Input 4 for a^x >= b",
       "Input 5 for a^x <= b"]
for ask in asks:
    print ask   

choose = input('make choose')
a = input('input A number')
b = input('input B number')
if choose == 1: # =
    answer = math.log(b) / math.log(a)
    print answer
     
elif choose == 2: # >
    if b <= 0:
        print "x O R"
    elif 0 < a and a < 1:
        math_log = math.log(b) / math.log(a)
        answer = "x < " +  str(math_log)
        print answer
    if a > 1:
        math_log = math.log(b) / math.log(a)
        answer = "x > " +  str(math_log)
        print answer
     
elif choose == 3: # <
    if b <= 0:
        print "No variants"
    elif 0 < a and a < 1:
        math_log = math.log(b) / math.log(a)
        answer = "x > " +  str(math_log)
        print answer
    if a > 1:
        math_log = math.log(b) / math.log(a)
        answer = "x < " +  str(math_log)
        print answer
     
elif choose == 4: # >=
    if b <= 0:
        print "x O R"
    elif 0 < a and a < 1:
        math_log = math.log(b) / math.log(a)
        answer = "x <= " +  str(math_log)
        print answer
        if a > 1:
            math_log = math.log(b) / math.log(a)
            answer = "x >= " +  str(math_log)
            print answer
     
elif choose == 5: # <=
    if b <= 0:
        print "No variants"
    elif 0 < a and a < 1:
        math_log = math.log(b) / math.log(a)
        answer = "x >= " +  str(math_log)
        print answer
    if a > 1:
        math_log = math.log(b) / math.log(a)
        answer = "x <= " +  str(math_log)
        print answer
