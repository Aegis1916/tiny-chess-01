import os,json,urllib.request as U
V=[0,100,305,333,563,950,0]
PT=['MMMMWWWWOOQSNNORMMMQNLKMNOOIMMMM','CEGGEIMMGMOPGNPQGMPQGNOPEIMNCEGG','IKKKKMMMKMNOKNNOKMOOKOOOKNMMIKKK','M'*4+'Q'*4+'M'*24,'GEEC'*4+'IGGEKIIIQQMMQSOM']
K=[0]*2;I=1e6;RC={0:2,7:1,56:8,63:4};KL=[0]*99
ND=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)];KD=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
RD=KD[::2];BD=KD[1::2]
D=[0,0,ND,BD,RD,KD,KD]
def SF(f):
 global B,S,C,E
 B=[0]*64;C=0;E=-1;a=f.split();q=56
 for ch in a[0]:
  if ch=='/':q-=16
  elif ch.isdigit():q+=int(ch)
  else:
   p='pnbrqk'.index(ch.lower())+1;B[q]=p*(1-2*ch.islower())
   if p>5:K[ch.islower()]=q
   q+=1
 S=1-2*(a[1]=='b')
 C=sum(1<<'KQkq'.index(ch)for ch in a[2]if ch!='-')
 if a[3]!='-':E=int(a[3][1])*8+ord(a[3][0])-105
def AT(q,y):
 r,f=q>>3,q&7
 for D,w,sl in((ND,2,0),(KD,6,0),(RD,4,1),(BD,3,1),(((-y,-1),(-y,1)),1,0)):
  for dr,df in D:
   rr,ff=r+dr,f+df
   while-1<rr<8>-1<ff<8:
    p=B[rr*8+ff]
    if p:
     if p==w*y or sl and p==5*y:return 1
     break
    if not sl:break
    rr+=dr;ff+=df
 return 0
def GEN():
 ms=[]
 def A(i,t):
  ms.extend([(i,t,x)for x in(5,4,3,2)]if t>>3==pr else[(i,t,0)])
 for i,p in enumerate(B):
  if p*S<=0:continue
  r,f=i>>3,i&7;a=abs(p)
  if a==1:
   d=8*S;pr=7*(S>0)
   if not B[i+d]:
    A(i,i+d)
    if r==1+5*(S<0)and not B[i+2*d]:ms.append((i,i+2*d,0))
   for df in(-1,1):
    if-1<f+df<8 and(B[(t:=i+d+df)]*S<0 or t==E):A(i,t)
  else:
   for dr,df in D[a]:
    rr,ff=r+dr,f+df
    while-1<rr<8>-1<ff<8:
     t=rr*8+ff;q=B[t]
     if q*S>0:break
     ms.append((i,t,0))
     if q or a in(2,6):break
     rr+=dr;ff+=df
 f=56*(S<0)+4
 for bt,g in((1,1),(2,-1)):
  if S<0:bt*=4
  t=f+2*g
  if C&bt and not any((x and B[f+x*g])or(AT(f+x*g,-S)if x<3else 0)for x in range(3+(g<0))):ms.append((f,t,0))
 return ms
def RM(a,b):B[b]=B[a];B[a]=0
def MK(m):
 global S,C,E
 f,t,pr=m;p=B[f];c=B[t];ep=p*p<2 and t==E and not c and f&7!=t&7
 if ep:c=B[t-8*S];B[t-8*S]=0
 B[t]=pr*S if pr else p;B[f]=0;u=(c,C,E,ep);E=-1
 if p*p<2 and t-f==16*S:E=f+8*S
 if p*p>30:
  K[S<0]=t;C&=~(3*4**(S<0))
  if abs(t-f)==2:RM(f+3-7*(t<f),f+1-2*(t<f))
 for x in(f,t):C&=~RC.get(x,0)
 S=-S;return u
def UN(m,u):
 global S,C,E
 S=-S;f,t,pr=m;c,C,E,ep=u;p=B[t]
 if p*p>30:
  K[S<0]=f
  if abs(t-f)==2:RM(f+1-2*(t<f),f+3-7*(t<f))
 B[f]=S if pr else p;B[t]=0;B[t-8*S if ep else t]=c
def EV():
 s=25*((B.count(3)>1)-(B.count(-3)>1))
 for i,p in enumerate(B):
  if p:
   a=abs(p);j=i^56*(p>0);f=j&7
   s+=(V[a]+(ord(PT[a-1-(a==5)*2-(a==6)][j//2&~3|min(f,7-f)])-77)*5+max(0,4-abs((i>>3)-(K[p>0]>>3))-abs(f-(K[p>0]&7)))*(V[a]//150))*(p//a)
 for f in range(8):
  c=B[f::8];w=1 not in c;b=-1 not in c
  s+=(4 in c)*w*(14+10*b)-(-4 in c)*b*(14+10*w)
 return s*S
def SC(m):f,t,pr=m;q=B[t];return pr*100+(10*V[abs(q)]-V[abs(B[f])]if q else 1000 if B[f]**2<2 and t==E else 90 if m==KL[P]else 0)
def NG(d,a,b,y):
 global NN,BM,P
 if y==0:NN=0;BM=None
 NN+=1
 if NN>1e5 or y>13:return EV()
 q=d<=0
 if q:
  st=EV()
  if st>=b:return st
  a=max(a,st)
 z=-I;P=y
 for m in sorted(GEN(),key=SC,reverse=1):
  f,t,pr=m
  if q and not(B[t]or pr or(B[f]**2<2 and t==E)):continue
  if q and B[t]and not pr and st+V[abs(B[t])]+150<a:continue
  u=MK(m)
  if AT(K[S>0],S):UN(m,u);continue
  v=-NG(d-1+AT(K[S<0],-S),-b,-a,y+1);UN(m,u)
  if v>z:
   z=v
   if y==0:BM=m
  if v>a:a=v
  if a>=b:
   if not(B[t]or pr):KL[y]=m
   break
 if q:return a
 return z if z>-I else(-1e5+y if AT(K[S<0],-S)else 0)
def MS(m):f,t,pr=m;return chr(97+(f&7))+str((f>>3)+1)+chr(97+(t&7))+str((t>>3)+1)+('qrbn'[5-pr]if pr else'')
W=os.environ['MAKEFUN_ENV_URL']
def POST(p,b):
 q=U.Request(W+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 return json.load(U.urlopen(q))
while 1:
 g=POST('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  SF(g['fen']);NG(4,-I,I,0)
  g=POST('/move',{'game':g['game'],'move':MS(BM)if BM else g['legal_moves'][0]})
