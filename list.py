# list 清單介紹

student = []
num = 1
print('輸入班級同學名字')
while True:
	name = input('第 %d 位同學:' % num)
	if name == "end":
		break
	else:
		student.append(name)
		num += 1
print("班級共 %d 位同學" % len(student))
print("名字分別是", student)
print('austin' in student) #檢查東西是否在清單裡，算是是非題
