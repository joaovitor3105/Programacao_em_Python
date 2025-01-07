import matplotlib as plt
pizza = ["cheese","pepperoni","sausage","mushroom","onion","pepper","anchovy","olive","pineapple","ham","spinach","artichoke","anchovy","pepper","onion","mushroom","sausage","pepperoni","cheese"]
plt.pie(labels=pizza,explode=True,autopct='%1.1f%%')
plt.show()