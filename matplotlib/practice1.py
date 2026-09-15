import matplotlib.pyplot as plt

x=[1,8,6,4,2]
y=[1,5,3,11,2]
y2=[4,9,3,4,6]
plt.plot(x,y,'g--',label="line 1")
plt.plot(x,y2,'bo',label="line 2")
plt.legend()
plt.savefig("practice.png")
plt.show()