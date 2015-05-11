from django.shortcuts import render,render_to_response
from Services.models import Login, Staff
from django.shortcuts import HttpResponse
import pdb
from django.template import Context

# Create your views here.
def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')

def test_login(request):
	uname = request.GET['uname']
	
	pwd = request.GET['pwd']
	
	try:
		obj = Login.objects.get(username=uname)
	except:
		return HttpResponse('User Not available')
	
	if obj:
		if obj.password == pwd:
			Staff_obj=Staff.objects.get(name=uname)
			data={	'username':Staff_obj.name,
					'Employee_Identity':Staff_obj.emp_id,
					'password':Staff_obj.password,
					'email':Staff_obj.email_id,
					'mobile_number':Staff_obj.phone,
					'dateofbirth':Staff_obj.dob,
					'salary':Staff_obj.salary}
			#Data=Context(data)
			return render_to_response('table.html',data)

			#return HttpResponse('Login Successful')
		else:
			return HttpResponse("Incorrect Password")

def register(request):
	return render(request, 'register.html')


def register_user(request):
	if request.method == 'POST':
		emp_id = request.POST['emp_id']
		try :
			obj = Staff.objects.get(emp_id=emp_id)
		except:
			obj = None
		if not obj:
			if request.POST['pwd1'] == request.POST['pwd2']:
				obj = Staff(name=request.POST['user'], password = request.POST['pwd1'], emp_id = request.POST['emp_id'], 
							email_id = request.POST['email'], phone = request.POST['mob'], 
							 dob=request.POST['dob'], salary= request.POST['sal'])
				obj.save()

				obj = Login(username=request.POST['user'], password = request.POST['pwd1'])
				obj.save()
				return render(request, 'login.html')
			else:
				return HttpResponse("Passwords doesn't match")
		else:
			return HttpResponse('User already Exists')


	
