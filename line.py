import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[25,20,15,10,5]
plt.plot(x,y1,label='y=x^2',color='purple',linestyle='--',marker='o')
plt.plot(x,y2,label='y=30-x^2',color='black',linestyle='-',marker='x')
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized line plot with Multiple Series')
plt.legend()
plt.savefig('all_features_plt.png')
plt.show()
           

