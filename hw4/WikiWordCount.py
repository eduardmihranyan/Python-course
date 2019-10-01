import wikipedia as wiki

text=wiki.summary("London")
sentences=text.split(". ")

d={}
for s in sentences:
    l=s.count(" ")-s.count(" ? ")+1
    if d.get(l):
        d[l]+=1
    else:
        d[l]=1
if d[max(d)]>1:
    print("There are {} sentences of length {} words".format(d[max(d)],max(d)))
else:
    print("There is {} sentence of length {} words".format(d[max(d)],max(d)))
    