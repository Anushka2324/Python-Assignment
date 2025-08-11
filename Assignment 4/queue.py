ls = []
a = 0

def enq(ls,im):
	if(len(ls)==10):
		print("\nqueue overflow")
	else :
		ls.append(im)
		print("\nqueue after enqueue operation : ",ls)
		

def dq(ls):
	if(len(ls)==0):
		print("\nqueue underflow")
	else :
		ls.pop(0)
		print("\nqueue after pop operation : ",ls)

def dply(ls):
	if(len(ls)==0):
		print("\nqueue is empty")
	else:
		print("\nelements in queue : ",ls)

def pk(ls):
	if(len(ls)==0):
		print("\nqueue underflow")
	else :
		ln = len(ls)-1
		print("\ntopmost element is : ",ls[ln]) 
		print("\nfirst element is : ",ls[0])

while(a==0) :
	print("\nEnter choice : ")
	ch = int(input("\n1:enqueue \n2:dequeue \n3:display \n4:peek \n5:exit \n"))
	if(ch==1) :
		im = int(input("\nenter item :"))
		enq(ls,im)
	elif(ch==2):
		dq(ls)
	elif(ch==3):
		dply(ls)
	elif(ch==4):
		pk(ls)
	else :
		a = a+1
