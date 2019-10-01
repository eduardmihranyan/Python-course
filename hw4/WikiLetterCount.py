import wikipedia as wiki
text=wiki.summary("London")
sentences=text.split(". ")

d={}
for i in range(len(sentences)):
    d[i+1]=len(sentences[i])

longest=max(d,key=d.get)
if longest==1:
    print("1st sentence is the longest with the length {}".format(max(d.values())))
elif longest==2:
    print("2nd sentence is the longest with the length {}".format(max(d.values())))                                                                  
else:
    print("{}th sentence is the longest with the length {}".format(longest,max(d.values())))
    
    