import itertools
f=open("apriori.txt","r");
support=2
lines = f.readlines()

distinct = {}
for line in lines:
    line=line.strip()
    for item in line.split(','):
        if(item not in distinct.keys()):
            distinct[item]=1;
        else:
            distinct[item]=distinct[item]+1;
            
list1=[]
frequent=[]
print '------C 1-----'
for key in sorted(distinct):
        print "('%s') %d" % (key, distinct[key])
        
print '******L 1*****'
for key in sorted(distinct):
    if(distinct[key]>=support):
        print "('%s') %d" % (key, distinct[key])
        if(key not in list1):
            list1.append(key)
            frequent.append(key)

print "\n\n"
length=len(list1)
L=2

newlist=[]
while(L<=length):
    print '------C',L,'-----'
    for subset in itertools.combinations(list1, L):
        for line in lines:
            line=line.strip().split(',')
            if(subset not in distinct):
                distinct[subset]=0
            if(set(subset).issubset(set(line))):
                distinct[subset]=distinct[subset]+1

        print subset, distinct[subset]
    print '******L',L,'*****'
    for subset in itertools.combinations(list1, L):
        if(distinct[subset]>=support):
            print subset, distinct[subset]
            frequent.append(subset)
            for j in subset:
                if j not in newlist:
                    newlist.append(j)
    list1=newlist
    newlist=[]
    length=len(list1)
    print "\n\n"
    L=L+1
    
print "Frequent Item Sets are\n",frequent
