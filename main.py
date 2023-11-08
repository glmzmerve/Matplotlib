import inline
import numpy
import matplotlib.pyplot as plt
import numpy as np
'''
age_list=[20,25,30,35,40,45,50,55,60]
weight_list=[70,75,73,85,89,90,75,84,90]
age_list_numpy=numpy.array(age_list)
weight_list_numpy=numpy.array(weight_list)
#print(age_list_numpy)
#print(weight_list_numpy)
#plt.plot(age_list_numpy,weight_list_numpy,"r")
#plt.xlabel("age")
#plt.ylabel("weight")
#plt.title("age-weight graph")
#plt.show()

my_numpy1=np.linspace(0,15,20)
print(my_numpy1)
my_numpy2=my_numpy1**3
print(my_numpy2)

plt.subplot(1,2,1) #1 row,2 column,1.graph
plt.plot(my_numpy1,my_numpy2,"r--")
plt.subplot(1,2,2)
plt.plot(my_numpy2,my_numpy1,"g*")
plt.show()
'''

my_figure=plt.figure()
my_axes=my_figure.add_axes([0.1,0.1,0.5,0.5])
my_numpy1=np.linspace(0,15,20)
print(my_numpy1)
my_numpy2=my_numpy1**3
print(my_numpy2)
#plt.plot(my_numpy1,my_numpy2,"g")
#my_axes.set_title("Graph Title")
'''
my_figure2=plt.figure()
my_axes3=my_figure2.add_axes([0.1,0.1,0.9,0.9])
my_numpy1=np.linspace(0,15,20)
my_numpy2=my_numpy1**3
my_axes3.plot(my_numpy1,my_numpy2,"r*-")
my_axes3.set_title("Large Graph")


my_axes2=my_figure2.add_axes([0.2,0.4,0.3,0.3])
my_numpy1=np.linspace(0,15,20)
my_numpy2=my_numpy1**3
my_axes2.plot(my_numpy1,my_numpy2,"g*")
my_axes2.set_title("Small Graph")

'''

(my_fig,my_axe)=plt.subplots()
my_numpy3=numpy.linspace(0,15,20)
my_numpy4=my_numpy3**2
#my_axe.plot(my_numpy3,my_numpy4,color="#CD621D",alpha=1)
#my_axe.plot(my_numpy4,my_numpy3,color="#B81DCD",alpha=0.5)

(new_fig,new_axe)=plt.subplots()
new_axe.plot(my_numpy3,my_numpy3+2,color="#B81DCD",linewidth=2.4)
new_axe.plot(my_numpy3,my_numpy3+3,color="#1DCDCA",linewidth=1.4)
new_axe.plot(my_numpy3,my_numpy3+4,color="blue",linewidth=1.4,linestyle="-.")
new_axe.plot(my_numpy3,my_numpy3+5,color="green",linewidth=1.4,linestyle=":")
new_axe.plot(my_numpy3,my_numpy3+5,color="red",linewidth=1.4,linestyle="--",marker="o")
new_axe.plot(my_numpy3,my_numpy3+6,color="black",linewidth=1.4,linestyle="--",marker="+",markersize=8)

new_fig.savefig("myfig.png",dpi=200)
plt.show()
'''
plt.scatter(my_numpy3,my_numpy4)
new_numpy=np.random.randint(0,100,40)
print(new_numpy)
plt.hist(new_numpy)
plt.show()
'''