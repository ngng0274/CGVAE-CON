f = open("pred.txt", 'r')
f2 = open("real.txt", 'r')

qed_diff = 0
i = 0
while True:
	line = f.readline()
	line2 = f2.readline()
	if not line or not line2:
		break
	qed_diff += abs(float(line)-float(line2))
	i+= 1
print(i)
print(qed_diff/i)