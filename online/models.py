
from django.db import models
from django.contrib.auth.models import User
import os

class Registration(models.Model):
	fname=models.CharField(max_length=40)
	lname=models.CharField(max_length=20)
	gnder=models.CharField(max_length=2)
	place=models.CharField(max_length=20)
	emai=models.CharField(max_length=20)
	# paswrd=models.IntegerField()
	phno=models.IntegerField()
	expnce=models.CharField(max_length=20)
	corse=models.CharField(max_length=20)
	qulifcn=models.CharField(max_length=20)
	pasout=models.IntegerField()
	clge=models.CharField(max_length=40)
	mark=models.IntegerField()
	intrested_area=models.CharField(max_length=20)
	status=models.IntegerField(default=1)
	class Meta:
		db_table="registrn"
class Jobs(models.Model):
	designatn=models.CharField(max_length=40)
	cmpny=models.CharField(max_length=40)
	salary=models.IntegerField()
	qualification=models.CharField(max_length=40)
	place=models.CharField(max_length=40)
	district=models.CharField(max_length=40)
	dte=models.DateField() 
	status=models.CharField(max_length=40,default="Not Expaired")
	class Meta:
		db_table="jobs_add"
class Approved_users(models.Model):
	fname=models.CharField(max_length=40)
	lname=models.CharField(max_length=20)
	gnder=models.CharField(max_length=2)
	place=models.CharField(max_length=20)
	emai=models.CharField(max_length=20)
	# paswrd=models.IntegerField()
	phno=models.IntegerField()
	expnce=models.CharField(max_length=20)
	corse=models.CharField(max_length=20)
	qulifcn=models.CharField(max_length=20)
	pasout=models.IntegerField()
	clge=models.CharField(max_length=40)
	mark=models.IntegerField()
	intrested_area=models.CharField(max_length=20)
	admin_status=models.CharField(max_length=20,default="Not Approved")
	class Meta:
		db_table="aproved_users"

class Apply_job(models.Model):
	fullnme=models.CharField(max_length=20)
	mail=models.CharField(max_length=30)
	msg=models.CharField(max_length=60)
	resme_uplod=models.FileField(upload_to='media') 
	company=models.CharField(max_length=30,default='null')
	desination=models.CharField(max_length=30,default='null')
	admin_status=models.CharField(max_length=30,default="Not Scheduled Yet")

	# date=models.DateField()
	class Meta:
		db_table="aply_job"
class intrvew_schedule(models.Model):
	fname=models.CharField(max_length=20)
	email=models.CharField(max_length=30)
	desination=models.CharField(max_length=30)
	company=models.CharField(max_length=30)

	adres=models.CharField(max_length=30)
	# distrct=models.CharField(max_length=30)
	date=models.DateField()
	class Meta:
		db_table="intrviw_schedule"

class Intrview_scheduled_for_user(models.Model):
	fname=models.CharField(max_length=20)
	email=models.CharField(max_length=30)
	desination=models.CharField(max_length=30)
	company=models.CharField(max_length=30)
	adres=models.CharField(max_length=30)
	status=models.CharField(max_length=30,default="Not Scheduled Yet")
	usr_status=models.CharField(max_length=30,default="Null")
	overall_status=models.CharField(max_length=30,default="No action")
	date=models.DateField()
	# time=models.TimeField(auto_now=False)
	class Meta:
		db_table="interviw_scheduled"

class Rejected_applicatn(models.Model):
	fname=models.CharField(max_length=20)
	email=models.CharField(max_length=30)
	desination=models.CharField(max_length=30)
	company=models.CharField(max_length=30)
	adres=models.CharField(max_length=30)
	status=models.CharField(max_length=30,default="Not Scheduled Yet")
	class Meta:
		db_table="rejectd_applicn"





