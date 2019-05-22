---
title: /#40python 统计四级单词词频 
tags: Python,词云,统计,词库,
grammar_cjkRuby: true
---
2019年05月21日 23时36分54秒

1. [成果展示](#成果展示)
2. [第一步寻找四级真题](#第一步寻找四级真题)
3. [第二步分析文字](#第二步分析文字)
4. [文字拆分并排序](#文字拆分并排序)
5. [文字写入文件](#文字写入文件)
6. [总代码](#总代码)

代码主要靠百度边查边写
为了能够更好地展现 代码的生成过程，（主要是懒）
	作业的完成主要靠百度，基本上是用啥查啥
	(有同学问我题，说为啥..我说百度上有，便说我敷衍，百度上真的有，说的很清楚，比我讲的更高效，更系统，遇到这种情况我也是没办法了o(╥﹏╥)o)
	所以我赶紧写个博客，再问我题，我可以直接甩博客链接过去.简单高效
我也没有进行过多的修饰和完善代码。
这样可能更有助于像我这样的新手，看到代码实现的过程，
通过哪些博客的借鉴最终成型的。

# 成果展示

![最终统计单词结果](./images/1558451995989.png)

# 第一步寻找四级真题

网上随便找的

![四级真题](./images/1558452058829.png)

网上版本多样，不能统一，所以我直接暴力，复制文本，粘贴到文本格式TXT保存方便读取

![复制成文本文件](./images/1558452101752.png)

![整理成文本格式方便读取](./images/1558452083932.png)

# 第二步分析文字

文字中很明显可以看出，有中文，有标点，怎么去掉呢？

![文字标点数字进行了分词的干扰](./images/1558452257290.png)

想办法去除这些干扰因素

查阅资料	[使用python提取中文数字和英文](https://blog.csdn.net/supinyu/article/details/80926167)

![将汉字和数字标点进行替换即可](./images/1558452428256.png)

我构建了下列函数，读取文件并返回==去除干扰字符 #2196F3==后的字符串

```	python 
def F(a):
    f=open(a,'r')
    st=f.read()
    s1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",st)
    return s1
    f.close()
```

紧接着 发现每段文字，第一个单词会是大写的，所以也要考虑大小写的问题，加上一句代码进行大小写转换

``` 
s=s.lower()
```

#  文字拆分并排序

1.所有干扰字符替换成空格，并且本身单词与单词之间以空格进行分隔，所以直接使用空格拆分即可
引用==string 库里的split()函数 #E91E63==
2.拆分后为一个列表，遍历列表统计单词出现个数
3.使用字典类型进行统计，key存储单词，velue存储单词个数
4.存储完后用==sort（）函数 进行排序 #E91E63==

资料	[python 统计单词个数](https://blog.csdn.net/weixin_33747129/article/details/86223300)

``` python
s=s.lower()
r=s.split()
words=r
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
```

# 文字写入文件

参考资料	[python的list变量保存为txt文本](https://blog.csdn.net/qq1491599481/article/details/80017493)

``` python
f=open('最终.txt','w')
sw='四级单词词频统计\n'
for i in range(len(items)):
    f.write(items[i][0]+'\t'+str(items[i][1])+'\n')    

f.close()

```
# 总代码

``` python
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

```