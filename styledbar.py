import plotly.express as px
data={"Fruit":["Apples","Orange","Bananas","Apples","Oranges","Bananas"],"Amount":[4,1,2,2,4,5],"City":["SF","SF","SF","Montreal","Montreal","Montreal"]}
fig=px.bar(data,x="Fruit",y="Amount",color="City",barmode="group",title="Fruit consumption by city")
fig.update_layout(template="plotly_dark")
fig.show()

