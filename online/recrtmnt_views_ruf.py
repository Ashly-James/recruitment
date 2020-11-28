from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# from .models import loginpge
dict2={}
c=0
# Create your views here.
def load(request):
	abt(request)
	return render(request,"index.html")
def abt(request):
	pass
	return render(request,"about.html")
def log(request):
	pass

	return render(request,"loginfuf.html")
def regstn(request):
		return render(request,"regstrn_form.html")
def logout_view(request):
	logout(request)
	return render(request,"index.html")

def registration(request):
	# try:
	fnme=request.POST['fname']
	lnme=request.POST['lname']
	gnder=request.POST['gender']
	print(gnder)
	plce=request.POST['place']
	phno=request.POST['phnumber']
	mail=request.POST['email']
	pswrd=request.POST['pswd']
	course=request.POST.get('cse',default='Bcom')
	qulifcn=request.POST['qulificn']
	passout=request.POST['pasout']
	insttn=request.POST['intrstara']
	mrk=request.POST['mark']
	intstd_area=request.POST['intrstara']
	exp=request.POST['exp']
	print(course)
	# data=loginm(umail=mail,pswd=pswrd)
	# data.save()
	data=Registration(fname=fnme,lname=lnme,gnder=gnder,place=plce,emai=mail,phno=phno,
		expnce=exp,corse=course,qulifcn=qulifcn,pasout=passout,clge=insttn,mark=mrk,
		intrested_area=intstd_area,status=1)
	data.save()
	q=User.objects.create_user(username=mail,password=pswrd)
	q.save()
	# data1=auth_user(username=mail,password=pswrd)
	# data1.save()
	return render(request,"index.html")
	
	# except Exception as e:
	# 	print(e) 

	
def loginrf(request):
	# u=""
	return render(request,"loginfuf.html")
def admn_view(request):
	q=Registration.objects.all()
	if q:
	
		return render(request,"admin_index.html",{"msg":q})
	else:

		return render(request,"admin_index.html",{"msg":"No data"})

	# return render(request,"admin_index.html")
def regstn_admn(request):
	q=Registration.objects.all()
	if q:
	
		return render(request,"table.html",{"msg":q})
	else:

		return render(request,"table.html",{"msg":"No data"})


	# return render(request,"prfle.html")
def logipge(request):
	apruval=0
	dict1={}
	passwrd=request.POST['txtpswd']
	usernme=request.POST['logmail']
	request.session['logmail']=usernme
	username=request.session['logmail']
	user=authenticate(username=usernme,password=passwrd)
	if(user!=None):
		login(request,user)
		print("login success")
		
		q=Registration.objects.filter(emai=request.POST['logmail'])
		for i in q:
			print("iiiiiiiiiiiiii",i.fname)
			dict1["name"]=i.fname
			dict1["lnme"]=i.lname
			dict1["gender"]=i.gnder
			dict1["place"]=i.place
			dict1["email"]=i.emai
			dict1["ph"]=i.phno
			dict1["exp"]=i.expnce
			dict1["crse"]=i.corse
			dict1["qlifcn"]=i.qulifcn
			dict1["pasut"]=i.pasout
			dict1["clg"]=i.clge
			dict1["mrk"]=i.mark
			dict1["ara"]=i.intrested_area

			print(dict1)
			print("qqqqqqqqqqqqqqqq",q)
			print(request.user)

		return render(request,"prfle.html",{"msg":dict1})
	else:
		return render(request,"loginfuf.html",{"msg":"Incorrect Username or password"})
def profile_edit(request):
	# try:
	username=request.session['logmail']

	q=Registration.objects.filter(emai=username)
	print(q)
	# for i in q:
	if q:	
		print(q)
		return render(request,"edit_user.html",{"msg":q})

	# except Exception as e:
def user_edit_r(request	):
	username=request.session['logmail']

	q=Registration.objects.filter(emai=username)
	# for i in q:
	print("aaaaaaaaaaaaaaaa",q)
	Registration.objects.filter(emai=username).update(fname=request.POST['fname'],lname=request.POST['lname'],
		# gender=request.POST['gender']
	place=request.POST['place'],phno=request.POST['phnumber'],emai=request.POST['email'],
	paswrd=request.POST['pswd'],
	# cse=request.POST.get('cse',default='Bcom')
	qulifcn=request.POST['qulificn'],pasout=request.POST['pasout'],clge=request.POST['institun']
	,mark=request.POST['mark'],intrested_area=request.POST['intrst_area'],expnce=request.POST['exp'])
	# print(i.fname,"wwwwwwwwww")
	return render(request,"prfle.html")
def job_form(request):
	pass
	return render(request,"jobs.html")
def job_updation(request):
	designation=request.POST['designatn']
	company=request.POST['cmpny']
	salry=request.POST['slry']
	plce=request.POST['plce']
	qualificn=request.POST['qulficn']
	district=request.POST['distrct']
	date=request.POST['dte']

	data=Jobs(designatn=designation,cmpny=company,salary=salry,qualification=qualificn,place=plce,
		district=district,dte=date)
	data.save()
def admin_aproval(request):
	# q=Registration.objects.filter(id=16)
	# for i in q:
	Registration.objects.filter(emai=16).update(status=0)
	q=User.objects.create_user(username=mail,password=pswrd)
	q.save()
	list1=Registration.objects.get(id=16)
	list1.delete()

