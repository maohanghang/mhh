import requests
import random
import re
from bs4 import BeautifulSoup
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com/').content
    soup = BeautifulSoup(content,'html.parser')

    for div in soup.find_all('div',{'class':'content'}):
        print div.text.strip()
def demo_string():
    stra = 'hello wSS'
    print stra.replace('wSS','mhh')
    print stra.capitalize()
    strb = '\n\rhelloworld\n\r'
    print 1,strb.lstrip()
    print 2,strb.rstrip()
    strc = 'hello w'
    print 3,strc.startswith('hel')
    print 4,strc.endswith('x')
    print stra+strc+strb
    print len(strc)
    print 7,'_'.join(['a','b','c'])
    print 8,strc.split(' ')

def demo_opeartion():
    print 1+2,5/5,5/2,5*2,5-2
    print 2,True,not True
    print 3,1<2,5>2
    print 4,5>>3,5<<3
    print 5,5|3,5&3,5^3
    x=1
    y=0.3
    print x,y,type(x),type(y)

def demo_buildinfunction():
    print 1,max(1,2),min(5,6)
    print 2,len('xxx'),len([1,2,3])
    print 3,abs(-2)
    print 4,range(1,10,3)
    print 5,dir(list)
    x=3
    print 6,eval('x+3')
    print chr(97),ord('a')
    print 8,divmod(11,3)

def demo_controlflow():
    score=65
    if score>99:
        print 1,'A'
    elif score>60:
        print 2,'B'
    else:
        print 3,'C'

    while score<100:
        print score
        score+=10

    for i in range(0,10):
        if i<5:
            continue
        print 3,i
        if i==6:
            break

def demo_list():
    lista = [1,2,3]
    print 1, lista
    listb = ['a','b',1,1.1]
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4,len(lista)
    print 5,'a' in listb
    listb.insert(0,'wwww')
    print 6,listb
    listb.pop(1)
    print 7,listb
    listb.reverse()
    print 8,listb
    print 9,listb[0]
    listb.sort()
    print listb
    listb.sort(reverse=True)
    print 12,listb
    print 13,listb*2
    print 14,[0]*14

    tuplea = (1,2,3)
    lista.append(4)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def demo_dict():
    dicta={1:1,2:4,3:9,4:9}
    print 1,dicta
    print 2,dicta.keys(),dicta.values()
    print 3,dicta.has_key(1),dicta.has_key('3')
    for key,value in dicta.items():
        print key,value
    dictb = {'+':add,'-':sub}
    print 4,dictb['+'](1,2)
    print 5,dictb.get('-')(15,3)
    dictb['*']='x'
    print dictb
    dicta.pop(4)
    print dicta
    del dicta[1]
    print 7,dicta

def demo_set():
    seta = set((1,2,3))
    print 1,seta
    setb = set((2,3,4))
    setc = set([2,3,4])
    seta.add(4)
    print 3,seta,setc
    print 3,seta.intersection(setb),seta & setb
    print 4,seta |setb,seta.union(setb)
    print 5,seta-setb
    seta.add('x')
    print 6,seta
    print len(seta)
    print seta.isdisjoint(set((1,2)))

class User:
    type='USER'
    def __init__(self,name,uid):
        self.name = name
        self.uid=uid
    def __repr__(self):
        return 'iam'+self.name+ ' '+str(self.uid)

class Admin(User):
    type = 'ADMIN'
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group = group
    def __repr__(self):
        return 'iam'+self.name+' '+str(self.uid)+' '+self.group
class Guest(User):
    def __repr__(self):
        return 'iam guest '+self.name+' '+str(self.uid)

def create_user(type):
    if type == 'USER':
        return User('u1',1)
    elif type=='ADMIN':
        return Admin('a1',101,'g1')
    else:
        return Guest(type,2)

def demo_exception():
    try:
        print 2/1
        print 2/0
        raise Exception('Raise Error','NewCoder')
    except Exception as e:
        print 'error:',e
    finally:
        print 'clean up'

def demo_random():
    #random.seed(1)
    print 1,random.random()
    print 2,random.randint(0,200)
    print 3,random.choice(range(0,100,10))
    print 4,random.sample(range(0,100),4)
    a=[1,2,3,4,5]
    random.shuffle(a)
    print 5,a

def demo_re():
    str = 'abcssdasffaf1356464465'
    p1= re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1,p1.findall(str)
    print 2,p2.findall(str)
    str = 'm@163.com;b@gmain.com;c@qq.com;e@163.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(str)

    str = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4,p4.findall(str)
    str = 'xx2016-06-11yyyy'
    p5 = re.compile('\d\d\d\d-\d\d-\d\d')
    print 5,p5.findall(str)
    p6 = re.compile('\d{4}-\d{2}-\d{2}')
    print 6, p6.findall(str)
if __name__ == "__main__":
    print'hello world'
    #demo_string()
    #demo_opeartion()
    #demo_buildinfunction()
    #demo_controlflow()
    #demo_list()
    #demo_dict()
    #demo_set()
    #user1 = User('u1',1)
   # print user1
    #admin1 = Admin('a1',101,'g1')
    #print admin1
    #print create_user('USER')
   #print create_user('ADMIN')
    #print create_user('ddd')
    #demo_exception()
    #demo_random()
    demo_re()
