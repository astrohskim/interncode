from ctypes import sizeof
from turtle import color
import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

o = mr.MesaData("models_z=0.02_c=10.0/m16/LOGS/history.data")
p = mr.MesaData("models_z=0.001_c=10.0/m16/LOGS/history.data")

def SM(z):
    o = mr.MesaData("models_z="+str(z)+"_c=1.0/m16/LOGS/history.data")
    i=0
    for em in o.center_h1:
        if em == 0.000000:
            return i 
        
        else:
            i+=1

def EH(z) : 
    o = mr.MesaData("models_z="+str(z)+"_c=1.0/m16/LOGS/history.data")
    i=-1
    for t in o.center_he4 :
        i+=1

        if t <= 10**(-3) : 
            
            return i

        else :
            if i+1 == len(o.center_he4) :
                return 0
            else :
                continue


def EM(z) :
    o = mr.MesaData("models_z="+str(z)+"_c=1.0/m16/LOGS/history.data")
    return len(o.log_Teff)-1


print(SM(0.02))
print(EH(0.02))
print(EM(0.02))
print(SM(0.001))
print(EH(0.001))
print(EM(0.001))


plt.plot(o.log_Teff,o.log_L,'k')
plt.plot(p.log_Teff,p.log_L,'k')

plt.plot(o.log_Teff[0:582],o.log_L[0:582],'b-',linewidth=6,alpha=0.4,label='Case A')
plt.plot(p.log_Teff[0:239],p.log_L[0:239],'b-',linewidth=6, alpha=0.4)

plt.plot(o.log_Teff[581:1073],o.log_L[581:1073],'y-',linewidth=6,alpha=0.4,label='Case B')
plt.plot(p.log_Teff[238:622],p.log_L[238:622],'y-',linewidth=6, alpha=0.4)

plt.plot(o.log_Teff[1073:1231],o.log_L[1073:1231],'g-',linewidth=6,alpha=0.4,label='Case C')
plt.plot(p.log_Teff[622:868],p.log_L[622:868],'g-',linewidth=6, alpha=0.4)

x=np.arange(3.58,4.61)
y=8*(x-4.5)+3.0
y1=8*(x-4.4)+3.8
y2=8*(x-4.3)+4.6
y3=8*(x-4.2)+5.4
y4=8*(x-4.1)+6.2
y5=8*(x-4.0)+7.0
y6=8*(x-3.9)+7.8
y7=8*(x-3.8)+8.6
y8=8*(x-3.7)+9.4
y9=8*(x-3.6)+10.2

plt.plot(x,y,'--',color='slategray',alpha=0.3)
plt.plot(x,y1,'--',color='slategray',alpha=0.3)
plt.plot(x,y2,'--',color='slategray',alpha=0.3)
plt.plot(x,y3,'--',color='slategray',alpha=0.3)
plt.plot(x,y4,'--',color='slategray',alpha=0.3)
plt.plot(x,y5,'--',color='slategray',alpha=0.3)
plt.plot(x,y6,'--',color='slategray',alpha=0.3)
plt.plot(x,y7,'--',color='slategray',alpha=0.3)
plt.plot(x,y8,'--',color='slategray',alpha=0.3)
plt.plot(x,y9,'--',color='slategray',alpha=0.3)

ax=plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))

plt.text(3.69,4.4,'constant radius', rotation=277, color='slategray',alpha=0.3)
plt.plot(o.log_Teff[0],o.log_L[0],'ko')
plt.plot(p.log_Teff[0],p.log_L[0],'ko')

plt.plot(o.log_Teff[581],o.log_L[581],'k^')
plt.plot(p.log_Teff[238],p.log_L[238],'k^')

plt.plot(o.log_Teff[1073],o.log_L[1073],'ks')
plt.plot(p.log_Teff[622],p.log_L[622],'ks')

plt.annotate('zero age',xy=(o.log_Teff[0],o.log_L[0]),xytext=(4.58,4.32),arrowprops=dict(facecolor='slategray',width=2,headwidth=7,edgecolor='none'))
plt.annotate('zero age',xy=(p.log_Teff[0],p.log_L[0]),xytext=(4.58,4.32),arrowprops=dict(facecolor='slategray',width=2,headwidth=7,edgecolor='none'))
plt.annotate('H exhuastion',xy=(o.log_Teff[581],o.log_L[581]),xytext=(4.45,4.8),arrowprops=dict(facecolor='slategray',width=2,headwidth=7,edgecolor='none'))
plt.annotate('H exhuastion',xy=(p.log_Teff[238],p.log_L[238]),xytext=(4.45,4.8),arrowprops=dict(facecolor='slategray',width=2,headwidth=7,edgecolor='none'))
plt.annotate('He exhuastion',xy=(o.log_Teff[1073],o.log_L[1073]),xytext=(3.9,4.85),arrowprops=dict(facecolor='slategray',width=2,headwidth=7,edgecolor='none'))
plt.annotate('He exhuastion',xy=(p.log_Teff[622],p.log_L[622]),xytext=(3.9,4.85),arrowprops=dict(facecolor='slategray',width=2,headwidth=7,edgecolor='none'))

plt.text(4.1,4.73,'Z=0.02',color='black',fontweight='bold')
plt.text(4.2,4.88,'Z=0.001',color='black',fontweight='bold')

plt.xlabel('log Teff(K)')
plt.ylabel('log L(Lsun)')
plt.xlim(3.58,4.61)
plt.ylim(4.29,5.01)
plt.gca().invert_xaxis()
plt.legend(loc='best', ncol=1)
plt.show()