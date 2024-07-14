print("marksheet")
name=input("enter name:")
roll_no=input("enter roll number")
c=int(input("enter marks for c subject"))
coa=int(input("enter marks for coa subject"))
ds=int(input("enter marks for ds subject"))
wordpress=int(input("enter marks for wordpress subject"))
python=int(input("enter marks for python subject"))
if(c>28 and coa>28 and ds>28 and wordpress>28 and python>28):
	total_marks=c+coa+ds+wordpress+python
	print("total marks are",total_marks)
	per=total_marks*100/500
	print("persantage is",per)
	if(per>=80):
		print("pass with A grade")
	elif(per<80 and per>=60):
		print("pass with B grade")
	elif(per>60 and per<=50):
		print("pass with C grade")
	elif(per<50 and per>=30):
		print("pass with D grade")
else:
	print("sorry you are fail")