import matplotlib.pyplot as plt
pizza = ["cheese","pepperoni","sausage","mushroom","onion","pepper","anchovy","olive","pineapple","ham","spinach","artichoke","anchovy","pepper","onion","mushroom","sausage","pepperoni","cheese"]
sizes = [1]*len(pizza)
plt.pie(sizes,labels=pizza,autopct='%1.1f%%')
plt.show()