from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration,Approved_users,Jobs,Apply_job,intrvew_schedule,Intrview_scheduled_for_user,Rejected_applicatn
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.core.mail import send_mail
from recruitment.settings import EMAIL_HOST_USER
import json
dict2={}
c=0
# Create your views here.
def load(request):
	# abt(request)
	return render(request,"index.html")
def abt(request):
	pass
	return render(request,"about.html")

	return render(request,"loginfuf.html")
def regstn(request):
		return render(request,"regstrn_form.html")
def logout_view(request):
	logout(request)
	return render(request,"index.html")
def registration(request):
	try:
		fnme=request.POST['fname']
		lnme=request.POST['lname']
		gnder=request.POST['gender']

		print(gnder)
		plce=request.POST['place']
		phno=request.POST['phnumber']
		mail=request.POST['email']
		pswrd=request.POST['pswd']
		# course=request.POST.get('cse')

		course=request.POST.get('cse',default='Bcom')
		qulifcn=request.POST['qulificn']
		passout=request.POST['pasout']
		insttn=request.POST['institun']
		mrk=request.POST['mark']
		intstd_area=request.POST['intrstara']
		# meta['gender'] = bool(request.POST.get('gender',''))

		exp=request.POST['exp']
		print(course)
		
		if Approved_users.objects.filter(emai=mail).exists():
			print("mails")
			q3="Sorry Email is Alredy Existed"
			return render(request,"regstrn_form.html",{"msg":q3})
		else:
			# import pdb; pdb.set_trace(
			data1=Approved_users(fname=fnme,lname=lnme,gnder=gnder,place=plce,emai=mail,phno=phno,
			expnce=exp,corse=course,qulifcn=qulifcn,pasout=passout,clge=insttn,mark=mrk,
			intrested_area=intstd_area)
			data1.save()		
			q=User.objects.create_user(username=mail,password=pswrd,first_name=fnme,last_name=lnme)
			q.save()
		# data1=auth_user(username=mail,password=pswrd)
		# data1.save()
			return render(request,"index.html")

	except Exception as e:
		print(e) 
		return render(request,"exception.html")
def user_home(request):
	username=request.session['logmail']

	q1=Approved_users.objects.filter(emai=username)
	return render(request,"prfle.html",{"msg":q1})

# def user_home_page(request):
# 		pass
# 		return render(request,"index.html")
	
def loginrf(request):
	# u=""
	return render(request,"loginfuf.html")
def admn_view(request):
	try:
		count=Approved_users.objects.filter(admin_status="Approved").count()

		job_count=Jobs.objects.count()
		apply_job_count=Apply_job.objects.count()
		aprvl=Approved_users.objects.filter(admin_status="Not Approved").count()
		print(count,apply_job_count)
		print("aaaaaaaa",aprvl)
		q=Approved_users.objects.filter(admin_status="Not Approved")
		if q:
		
			return render(request,"admin_index.html",{"msg":q,"msg1":count,"msg2":job_count,"msg3":apply_job_count,"msg4":aprvl})
		else:

			return render(request,"admin_index.html",{"msg":q,"msg1":count,"msg2":job_count,"msg3":apply_job_count,"msg4":aprvl})

		return render(request,"admin_index.html",{"msg":q,"msg1":count,"msg2":job_count,"msg3":apply_job_count,"msg4":aprvl})
	except Exception as e:
		print(e)
		return render(request,"exception.html")
 
def bck_home_admin(request):
	try:
		count=Approved_users.objects.filter(admin_status="Approved").count()
		job_count=Jobs.objects.count()
		apply_job_count=Apply_job.objects.count()
		aprvl=Approved_users.objects.filter(admin_status="Not Approved").count()
		print("aaaaaaaa",aprvl)
		q=Approved_users.objects.filter(admin_status="Not Approved")
		if q:
		
			return render(request,"admin_index.html",{"msg":q,"msg1":count,"msg2":job_count,"msg3":apply_job_count,"msg4":aprvl})
		else:

			return render(request,"admin_index.html",{"msg":"No data"})
		# return render(request,"admin_index.html",{"msg":q})
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def regstn_admn(request):
	q=Approved_users.objects.filter(admin_status="Approved")
	if q:
	
		return render(request,"Aproved_users.html",{"msg":q})
	else:

		return render(request,"Aproved_users.html",{"msg":"No data"})


	return render(request,"prfle.html")
def logipge(request):
	try:
	# apruval=0
		dict1={}
		passwrd=request.POST['txtpswd']
		usernme=request.POST['logmail']
		request.session['logmail']=usernme
		username=request.session['logmail']
		print(usernme)
		enter=Approved_users.objects.filter(emai=usernme,admin_status="Approved")
		print("qaa",enter)
		user1=authenticate(username=usernme,password=passwrd,is_superuser=1)
		# import pdb;pdb.set_trace()
		print(user1)
		if(user1.is_superuser):
			login(request,user1)
			count=Approved_users.objects.filter(admin_status="Approved").count()
			job_count=Jobs.objects.count()
			apply_job_count=Apply_job.objects.count()
			aprvl=Approved_users.objects.filter(admin_status="Not Approved").count()
			q=Approved_users.objects.filter(admin_status="Not Approved")
			if q:
			
				return render(request,"admin_index.html",{"msg":q,"msg1":count,"msg2":job_count,"msg3":apply_job_count,"msg4":aprvl})
			else:

				return render(request,"admin_index.html",{"msg":"No data"})
				# return redirect("admin123")
		elif enter:
			print("user login")
			user=authenticate(username=usernme,password=passwrd)
			if(user!=None):
				login(request,user)
				print("login success")
				
				q=Approved_users.objects.filter(emai=request.POST['logmail'])
				
				qa=Jobs.objects.all()
				dict1["q"]=qa
				
				return render(request,"prfle.html",{"msg":q})
			
			else:

				return render(request,"loginfuf.html",{"msg":"Incorrect Username or password"})
		elif(Approved_users.objects.filter(emai=usernme,admin_status="Rejected")):
			return render(request,"loginfuf.html",{"msg":"Sorry admin reject your application"})
		elif(Approved_users.objects.filter(emai=usernme,admin_status="Not Approved")):

			return render(request,"loginfuf.html",{"msg":"Wait for the admin approval"})
	except Exception as e:
		print(e)
		# return render(request,"exception.html")
		return render(request,"loginfuf.html",{"msg":"Incorrect Username or password"})


def profile_edit(request):
	try:
		username=request.session['logmail']

		q=Approved_users.objects.filter(emai=username)
		print(q)
		# for i in q:
		if q:	
			print(q)
			return render(request,"edit_user.html",{"msg":q})

	except Exception as e:
		print(e)
		return render(request,"exception.html")

def user_edit_r(request	):
	try:
		username=request.session['logmail']

		q=Approved_users.objects.filter(emai=username)
		# for i in q:
		print("aaaaaaaaaaaaaaaa",q)
		Approved_users.objects.filter(emai=username).update(fname=request.POST['fname'],lname=request.POST['lname'],
			# gender=request.POST['gender']
		place=request.POST['place'],phno=request.POST['phnumber'],emai=request.POST['email'],
		
		# cse=request.POST.get('cse',default='Bcom')
		qulifcn=request.POST['qulificn'],pasout=request.POST['pasout'],clge=request.POST['institun']
		,mark=request.POST['mark'],intrested_area=request.POST['intrst_area'],expnce=request.POST['exp'])
		# print(i.fname,"wwwwwwwwww")
		return render(request,"prfle.html",{"msg":q})
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def job_form(request):
	pass
	return render(request,"jobs.html")
def job_updation(request):
	try:
		designation=request.POST['designatn']
		company=request.POST['cmpny']
		salry=request.POST['slry']
		plce=request.POST['plce']
		qualificn=request.POST['qulficn']
		district=request.POST['distrct']
		date=request.POST['dte']

		dat=Jobs(designatn=designation,cmpny=company,salary=salry,qualification=qualificn,place=plce,
			district=district,dte=date)
		dat.save()
		return render(request,'admin_index.html')
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def admin_aproval(request):
	try:
		print("Req Data=> ",request.POST) 
		count=Approved_users.objects.filter(admin_status="Approved").count()
		job_count=Jobs.objects.count()
		apply_job_count=Apply_job.objects.count()
		aprvl=Approved_users.objects.filter(admin_status="Not Approved").count()
		
		q=Approved_users.objects.filter(admin_status="Not Approved")

		
		idi=request.POST.get('id')
		print("id",idi)
		
		if request.POST.get('id')!=None:

			Approved_users.objects.filter(id=idi).update(admin_status="Approved")

			return render(request,'admin_index.html',{"msg":q})
		elif request.POST.get("id1"):
			Approved_users.objects.filter(id=request.POST.get("id1")).update(admin_status="Rejected")

			return render(request,"admin_index.html",{"msg":q,"msg1":count,"msg2":job_count,"msg3":apply_job_count,"msg4":aprvl})

	except Exception as e:
		print(e)
		return render(request,"exception.html")

def apply_job(request):
	try:
	# import pdb;pdb.set_trace()
		username=request.session['logmail']
		print("lllllllllllll",username)
		q=Approved_users.objects.filter(emai=username)
		# import pdb;pdb.set_trace()
		id1=request.POST['id']
		w=Jobs.objects.filter(id=id1)
		print(w)
		return render(request,'aply_job.html',{"msg":q,"msg1":w})
	except Exception as e:
		print(e)
	
def contact(request):
	pass
	return render(request,'contact.html')

def apply_jobs_user_view(request):
	# import pdb;pdb.set_trace()
	try:
		fulnme=request.POST['full_name']
		email=request.POST['email']
		mesg=request.POST['message']
		cv=request.FILES['file_cv']
		cmpny=request.POST['cmpany']
		designtn=request.POST['designtion']
		if Apply_job.objects.filter(fullnme=fulnme,mail=email,company=cmpny,desination=designtn):
			print("sorry already exist")
			q2="Sorry You have allready applayed for this Job!!!"
			q=Approved_users.objects.filter(emai=email)
			return render(request,"aply_job.html",{"msge":q2,"msg":q})
		else:
			data=Apply_job(fullnme=fulnme,mail=email,msg=mesg,resme_uplod=cv,company=cmpny,desination=designtn)
			data.save()
			q=Approved_users.objects.filter(emai=email)
			return render(request,"prfle.html",{"msg":q})
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def admin_job_user_apply(request):
	q=Apply_job.objects.filter(admin_status="Not Scheduled Yet")
	return render(request,"job_appy_details.html",{"msg":q})

def admin_job_allotmnt(request):
	try:
		q=Apply_job.objects.filter(admin_status="Not Scheduled Yet")
		print("aaaaaaaaaaaaaaaa",request.POST) 
		pid=request.POST.get('id2')

		if request.POST.get('id'):
			q=Apply_job.objects.filter(id=request.POST['id'],admin_status="Not Scheduled Yet")
			print("qqqqqqqqqqq",q)
			return render(request,"admin_job_allocation.html",{"mesg":q})
		elif request.POST.get('id2')!=None:
			Apply_job.objects.filter(id=pid).update(admin_status="Rejected")
			return render(request,"job_appy_details.html",{"msg":q})
		return render(request,"job_appy_details.html",{"msg":q})
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def admin_job_alotmnt_submit(request):
	try:
		fulname=request.POST['fnme']
		mmail=request.POST['email']
		designation=request.POST['designatn']
		compny=request.POST['cmpny']
		addrss=request.POST['ads']
		dat=request.POST['dte']
		if request.POST.get("alocte"):
			Apply_job.objects.filter(mail=mmail,company=compny,desination=designation).update(admin_status="Scheduled")

			data=Intrview_scheduled_for_user(fname=fulname,email=mmail,desination=designation,company=compny
			,adres=addrss,date=dat,status="Scheduled")
			data.save()
		
		return render(request,"admin_job_allocation.html")
	except Exception as e:
		print(e)
		return render(request,"exception.html")
def notification(request):
	try:
		username=request.session['logmail']
		print("lllllllllllll",username)
		q=Intrview_scheduled_for_user.objects.filter(email=username,overall_status="No action")
		return render(request,"intrview_scheduled.html",{"msg":q})
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def confirmation_user(request):
	try:
		username=request.session['logmail']
		f=request.POST['fnme']
		d=request.POST['desn']
		c=request.POST['cpny']

		if request.POST.get('confirm')!=None:
			Intrview_scheduled_for_user.objects.filter(email=username,desination=d,company=c,fname=f).update(usr_status="Confirmed")
		else:
			Intrview_scheduled_for_user.objects.filter(email=username,desination=d,company=c,fname=f).update(usr_status="Declined")

		q=Approved_users.objects.filter(emai=username)
		return render(request,"prfle.html",{"msg":q})
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def user_confirmed_jobs(request):
	q=Intrview_scheduled_for_user.objects.filter(overall_status="No action",usr_status="Confirmed").order_by('-date')
	q2="Confirmed Interviews"
	return render(request,"confirmed_intrviws.html",{"msg":q,"msg2":q2})
def jobs_details_for_user(request):
	q=Jobs.objects.filter(status="Not Expaired")
	print("jobssssssssssssss",q)
	return render(request,"jobs_for_user.html",{"msge":q})
def password_reset(request):
	return render(request,'set_email/password_reset_form.html')
def forgot(request):
	try:
		password=User.objects.make_random_password()
		print(password)
		n=request.POST['pswdreset']
		# import pdb; pdb.set_trace()
		try:
			user=User.objects.get(username=n)
			print(user)
			password_mail_String="You have requested for a password for your account.The new password is "+str(password)+". Please login to 127.0.01:8000"
			print("hsi")
			subject='password reset instruction.This is your new password . Please login with the new password '
			message=password_mail_String
			print("hai")
			recepient=n
			print("ja")
			send_mail( subject, message, EMAIL_HOST_USER,[recepient],fail_silently=False)
			print(user)
			user.set_password(password)
			user.save()
			print(user)
			messages.info(request,'we\' sent the new password to this mail address')
		except: 
			messages.info(request,'Email does not exist')
	except Exception as e:
		print(e)
	return render(request,'set_email/password_reset_form.html')
def complted_intrview(request):
	print(request.POST)
	pid=request.POST.get('id')
	print("id==",pid)
	d=request.POST['desination']
	c=request.POST['company']
	f=request.POST['fname']
	# print(p,d,c,f)
	q=Intrview_scheduled_for_user.objects.filter(overall_status="No action",usr_status="Confirmed").order_by('-date')
	if request.POST.get('id')!=None:
		Intrview_scheduled_for_user.objects.filter(id=pid).update(overall_status="Expaired")
		# elif request.POST.get('id2')!=None:
	elif request.POST.get("id1"):
		Intrview_scheduled_for_user.objects.filter(id=request.POST.get("id1")).update(overall_status="Completed")
	q2="Confirmed Interviews"
	return render(request,"confirmed_intrviws.html",{"msg":q,"msg2":q2})

def home_jobs(request):
	q=Jobs.objects.filter(status="Not Expaired")
	return render(request,"home_jobs.html",{"msg":q})
def aply_job_home(request):
	q=Jobs.objects.filter(status="Not Expaired")
	q1="Sorry You Have To Login First !!!!"
	return render(request,"home_jobs.html",{"msge":q1,"msg":q})
def usr_complte_intrws(request):
	q=Intrview_scheduled_for_user.objects.filter(overall_status="Completed")
	print(q)
	q2="Completed Interviews"
	return render(request,"complted_intrws.html",{"msg":q,"msg2":q2})
def usr_abort_intrws(request):
	q=Intrview_scheduled_for_user.objects.filter(overall_status="Expaired")
	q2="Expaired Interviews"
	return render(request,"complted_intrws.html",{"msg":q,"msg2":q2})
def usr_decline_inrws(request):
	q2="Declined Interviews"
	q=Intrview_scheduled_for_user.objects.filter(usr_status="Declined")
	return render(request,"complted_intrws.html",{"msg":q,"msg2":q2})
def usr_rjct_inrws(request):
	q2="Rejected Interviews"
	q=Apply_job.objects.filter(admin_status="Rejected")
	return render(request,"admin_rjct_intews.html",{"msg":q,"msg2":q2})
def admin_job_view(request):
	try:
		q=Jobs.objects.filter(status="Not Expaired")
		return render(request,"admin_view_jobs.html",{"msg":q})

	except Exception as e:
		print(e)
		return render(request,"exception.html")

def dlte_admn_jobs(request):
	try:
	
		pid=request.POST.get('id')
		print(pid)
		q=Jobs.objects.filter(status="Not Expaired")

		Jobs.objects.filter(id=pid).update(status="Expaired") 

		return render(request,"admin_view_jobs.html",{"msg":q})

	except Exception as e:
		print(e)
		return render(request,"exception.html")

def Expaired_jobs(request):
	pass
	try:
		q=Jobs.objects.filter(status="Expaired")
		return render(request,"expred_jobs.html",{"msg":q})
	
	except Exception as e:
		print(e)
		return render(request,"exception.html")

def pdf_view(request):
	pid=request.POST.get('id1')
	# if request.POST.get('id1'):
	path='/python/pythonvirtul/recruitment/media/'+pid
	print("pid==",pid)
	print("path=",path)

	data=dict()
	with open(path,'rb') as pdf:
		response=HttpResponse(pdf.read(),content_type='application/pdf')
		response['Content-Disposition']='pid.pdf'
		return response
def change_pswd(request):
	return render(request,"change_pswd.html")
def change_passwrd(request):
	try:
		usernme=request.session['logmail']
		paswd=request.POST['pswdreset']
		user=User.objects.get(username=usernme)
		print(paswd)	
		if user:
			print(user)
		user.set_password(paswd)
		user.save()
		print("user",user)
		q=Approved_users.objects.filter(emai=usernme)
		return render(request,"prfle.html",{'msg':q})
	except Exception as e:
		return render(request,"exception.html")

