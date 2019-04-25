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
    post1 = (float) s1*p1/unc;
    post2 = (float) s2*p2/unc;
    post3 = (float) s3*p3/unc;
    print("Signal number" + counter)
    print(post1, post2, post)
    counter= counter+1