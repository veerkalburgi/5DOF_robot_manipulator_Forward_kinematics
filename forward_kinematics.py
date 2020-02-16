import numpy as np

d1=0.5
d2=0
d3=0
d4=0
d5=0.05

a1=0
a2= 0.4
a3= 0.3
a4= 0.2
a5=0

Theta1 =0 
Theta2 =0
Theta3 =0
Theta4 =0
Theta5 =0

Theta1 =(Theta1/180)*np.pi
Theta2 =(Theta2/180)*np.pi
Theta3 =(Theta3/180)*np.pi
Theta4 =(Theta4/180)*np.pi
Theta5 =(Theta5/180)*np.pi

# DH parameter Table 
PT =[[Theta1,(90.0/180.0)*np.pi,0,d1],
     [Theta2,0,a2,0],
     [Theta3,0,a3,0],
     [Theta4,(135/180)*np.pi,a4,0],
     [Theta5,0,0,d5]]
 
i =0 
H0_1=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
     [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
     [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
     [0,0,0,1]] 

i =1 
H1_2=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
     [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
     [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
     [0,0,0,1]] 


i =2 
H2_3=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
     [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
     [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
     [0,0,0,1]]

i =3
H3_4=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
     [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
     [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
     [0,0,0,1]]


i =4 
H4_5=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
     [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
     [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
     [0,0,0,1]]

#print ("H0_1=",np.matrix(H0_1))
#print ("H1_2=",np.matrix(H1_2))
#print ("H2_3=",np.matrix(H2_3))
#print ("H3_4=",np.matrix(H3_4))
#print ("H4_5=",np.matrix(H4_5))

H0_2 =np.dot(H0_1,H1_2)
H0_3 =np.dot(H0_2,H2_3)
H0_4 =np.dot(H0_3,H3_4)
H0_5 =np.dot(H0_4,H4_5)

print ("H0_5=",np.matrix(H0_5))
print ("postion of end effector=",H0_5[:,3])
print ("orientation of end effector=",H0_5[:3,:3])


