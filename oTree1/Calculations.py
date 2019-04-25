prior = [0.25, 0.50, 0.25]
p1 = prior[0]
p2 = prior[1]
p3 = prior[2]

#signal structure s - conditional probability p(black|urn)
signal1 = [0.8, 0.5, 0.2] # second unchanged
signal2 = [0.6, 0.5, 0.4] # second unchanged
signal3 = [0.8, 0.6, 0.2]
signal4 = [0.4, 0.3, 0.1]
signal5 = [1.0, 0.5, 0.5] #% exclude one option,
signal6 = [0.9, 0.9, 0.4] #% second is double than first
signal7 = [0.4, 0.8, 0.2]
signal8 = [0.3, 0.3, 0.3] #% no change
signal9 = [0.8, 0.7, 0.6] #% second unchanged
signal10= [0.8, 0.5, 0.8] #% symmetric first and third
 
SignalList = [signal1, signal2, signal3, signal4, signal5, signal6, signal7, signal8, signal9, signal10]


counter = 1
for signal in SignalList:
    #% read signal structure - black ball
    s1=signal[0]
    s2=signal[1]
    s3=signal[2]
    #reading off the numbers for each list
        
    unc = s1*p1+s2*p2+s3*p3; 
    #print(unc)
    post1 = s1*p1/unc;
    #print(s1)
    #print(p1)
    #print(unc)
    
    post2 = s2*p2/unc;
    post3 = s3*p3/unc;
    print("Signal number" + str(counter))
    print(post1, post2, post3)
    print("")
    counter= counter+1
    
"""
Signal number1
0.4 0.5 0.1

Signal number2
0.3 0.5 0.2

Signal number3
0.36363636363636365 0.5454545454545454 0.09090909090909091

Signal number4
0.36363636363636365 0.5454545454545454 0.09090909090909091

Signal number5
0.4 0.4 0.2

Signal number6
0.2903225806451613 0.5806451612903226 0.12903225806451613

Signal number7
0.18181818181818182 0.7272727272727273 0.09090909090909091

Signal number8
0.25 0.5 0.25

Signal number9
0.2857142857142857 0.49999999999999994 0.21428571428571425

Signal number10
0.3076923076923077 0.3846153846153846 0.3076923076923077
"""