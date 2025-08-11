ls = []
a = 0

def psh(ls,im):
	if(len(ls)==10):
		print("\nstack overflow")
	else :
		ls.append(im)
		print("\nstack after push operation : ",ls)
		

def pp(ls):
	if(len(ls)==0):
		print("\nstack underflow")
	else :
		ls.pop()
		print("\nstack after pop operation : ",ls)

def dply(ls):
	if(len(ls)==0):
		print("\nstack is empty")
	else:
		print("\nelements in stack : ",ls)

def pk(ls):
	if(len(ls)==0):
		print("\nstack underflow")
	else :
		ln = len(ls)-1
		print("\ntopmost element is : ",ls[ln]) 

while(a==0) :
	print("\nEnter choice : ")
	ch = int(input("\n1:push \n2:pop \n3:display \n4:pick \n5:exit\n"))
	if(ch==1) :
		im = int(input("\nenter item :"))
		psh(ls,im)
	elif(ch==2):
		pp(ls)
	elif(ch==3):
		dply(ls)
	elif(ch==4):
		pk(ls)
	else :
		a = a+1;
