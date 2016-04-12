import os
import shutil
import datetime

Months = ["NUll", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def getDate():
	today = datetime.datetime.now()
	month = today.month
	day = today.day

	return (month, day)

def move(src,dst):
	listOfFiles = os.listdir(src)
	for f in listOfFiles:
		#print (f)
		File = src + "/" + f
		FileDst = dst + "/" + f
		
		if File [-4:] != '.ini':
			shutil.move(File, FileDst)

(month, day) = getDate()


f = open('Paths.txt', 'r')
lst = f.readlines()

src = lst[1] 
dst = lst[0]
dst = dst[:-1]		# removes \n
src = src[:-1]		# removes \n
dst = dst + Months[month] + " " + str(day) + "/"


if not os.path.exists(dst):
	os.makedirs (dst)

move(src, dst)
