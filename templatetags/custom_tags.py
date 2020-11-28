from django import template
from django import 
# register = template.Library()

# from ..models import contacts
# # @register.simple_tag
# def any_function():
# 	return contacts.objects.count()
# @register .inclusion_tag('view.html')
# def any():
# 	data=contacts.objects.order_by('name')[:5]
# 	return {'variable':data}
# @register.assignment_tag('.view.html')
# def functn():
# 	print()
# 	return data=contacts.objects.all()
def all(request):
	data = contacts.objects.all()
	print(data)