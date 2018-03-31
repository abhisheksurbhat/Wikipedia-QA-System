import json
import matplotlib.pyplot as plt

def avg(p):
	return sum(p)/len(p)

q = open("question.json","r")
dataq = json.load(q)
q.close()
datalq = dataq['data']

c = open("context.json","r")
datac = json.load(c)
c.close()
datalc = datac['data']

plength = []
count = 0
for i in range(len(datalc)):
	plength.append(len(datalc[i][str(i)]))
fp = open('ana.csv','w')
for i in plength:
	fp.write(str(i)+'\n')
fp.close()
plt.plot(range(len(datalc)),plength)
plt.show()
print(len(plength))
print(max(plength))
print(avg(plength))