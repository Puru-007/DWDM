import math
def dist(a,b,c):
	s = 0
	for i in range(c):
		s+= (a[i]-b[i])**2
	return(math.sqrt(s))

	

def s(a,c):
	ln = len(a)
	e = []
	for i in range(c):
		s = 0
		for j in range(ln):
			s+= a[j][i]
		e.append(s/ln)
	return(e)

n = int(input("Enter the no of elements : "))
c = int(input("Enter the no of attributes : "))
w = []
for i in range(n):
	l = []
	print("Enter the coordinates of object {}".format(i+1))
	for j in range(c):
		l.append(float(input()))
	w.append(l)
k = int(input("Enter the no of clusters : "))
cl = []

for i in range(k):
	cl.append(w[i])
hist = [[] for _ in range(k)]
l1 = [[] for _ in range(k)]
while(1):
	cluster = [[] for _ in range(k)]
	if(hist != l1):
		for i in range(k):
			if(hist[i] != []):
				cl[i] = s(hist[i],c)
	for i in range(n):
		m = 999
		for j in range(k):
			d = dist(w[i],cl[j],c)
			if(d < m):
				m = d
				ind = j
		#print(ind)

		cluster[ind].append(w[i])
	if(hist == cluster):
		break
	else:
		hist = cluster
b = [[] for _ in range(k)]
for i in range(k):
	a = cluster[i]
	b[i] = [w.index(a[j])+1 for j in range(len(a))]
print(b)





