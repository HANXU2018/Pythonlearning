import string
import re
def F(a):
    f=open(a,'r')
    st=f.read()
    s1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",st)
    return s1
    f.close()
f=open('17-12.txt','r')
st=f.read()
s = re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",st)
f.close()
f=open('17-12-1.txt','r')
st=f.read()
s1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",st)
s=s+s1
f.close()
f=open('17-12-2.txt','r')
st=f.read()
s1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",st)
s=s+s1
f.close()

s+=F('16-12-1.txt')
s+=F('16-6-2.txt')
s+=F('15-12-1.txt')
s=s.lower()
r=s.split()
words=r
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
f=open('最终.txt','w')
sw='四级单词词频统计\n'
for i in range(len(items)):
    f.write(items[i][0]+'\t'+str(items[i][1])+'\n')    

f.close()

