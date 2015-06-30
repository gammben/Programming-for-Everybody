sc = raw_input("Type your score:")
try:
    score = float(sc)
except:
    score = -1000
if score > 1.0 :
    print " Out of range" 
elif score < 0 :
    print "Please, input a number"
elif score >= 0.9 :
    print "A"
elif score >= 0.8 :
    print "B"
elif score >= 0.7 :
    print "C"
elif score >= 0.6 :
    print "D"
elif score < 0.6 :
    print "F"