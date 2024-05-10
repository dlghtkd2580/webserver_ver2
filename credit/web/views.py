from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from .models import *
import datetime
import os
import subprocess


path = "/root/"

@method_decorator(csrf_exempt)
def new_form(request):

	try:
		if request.method == 'POST':
			add_phone_number = request.POST['phone_number_1'] + request.POST['phone_number_2'] + request.POST['phone_number_3']

			Form.objects.create(
				name=request.POST['name'],
				phone_number=add_phone_number,
				region=request.POST['region'],
				age=request.POST['age'],
				gender=request.POST['gender'],
				job=request.POST['job'],
				pay=request.POST['pay'],
				pay_day=request.POST['pay_day'],
				use_bool=request.POST['use_bool'],
				use_ps=request.POST['use_ps'],
				credit_grade=request.POST['credit_grade'],
				holding_credit=request.POST['holding_credit'],
				is_married=request.POST['is_married'],
				is_child=request.POST['is_child'],
				holding_house=request.POST['holding_house'],
				holding_car=request.POST['holding_car'],
				credit_amount=request.POST['credit_amount'],
				credit_date=request.POST.get('credit_date', None)
			)

			return render(request, 'web/success_form.html')

		else:
			return render(request, 'web/new_form.html')

	except Exception as err:
		print(err)
		HttpResponse(status=404)

def login(request):

	try:

	    user_pk = request.session.get('user')
	    user = None

	    if user_pk:
	        user = User.objects.get(pk=user_pk)
	        return render(request, 'web/list.html', {'user':user})

	    if request.method == 'POST':

	        if User.objects.filter(user_id=request.POST['user_id']):
	            user = User.objects.filter(user_id=request.POST['user_id']).first()

	            if user.user_pw == request.POST['user_pw']:
	                request.session['user']=user.pk


	                return HttpResponseRedirect(reverse('web:list'), {'user':user})

	            else:
	                return render(request, 'web/login_fail.html', {'user':user})

	        else:
	            return render(request, 'web/login_fail.html', {'user':user})

	    elif request.method == 'GET':
	        return render(request, 'web/login.html')

	except Exception as err:
		HttpResponse(status=404)

def logout(request):

	try:

	    request.session['user']=None
	    user_pk = request.session.get('user')
	    user = None

	    return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)

def list(request):

	try:

		user_pk = request.session.get('user')
		user = None

		if user_pk:
			user = User.objects.get(pk=user_pk)
			forms = Form.objects.all().order_by('-date')
			time_arr = []

			file_list = os.listdir(path)
			file_list = [file for file in file_list if file.endswith(".txt")]
			full_list = [os.path.join(path,i) for i in file_list]
			time_sorted_txt_list = sorted(full_list, key=os.path.getctime, reverse=True)
			for file in time_sorted_txt_list:
			    create_time = os.path.getctime(file)
			    create_time_stamp = datetime.datetime.fromtimestamp(create_time)
			    time_string = datetime.datetime.strftime(create_time_stamp, '%Y-%m-%d %H:%M')
			    time_arr.append(time_string)

			zip_file = zip(time_arr,time_sorted_txt_list)
			txt_list = time_sorted_txt_list
			
			return render(request, 'web/list.html', {'user':user,'forms':forms,'zip_file':zip_file,'txt_list':txt_list})



		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)


def form_view(request, form_pk):

	try:

		user_pk = request.session.get('user')
		user = None
		if user_pk:
			user = User.objects.get(pk=user_pk)
			form = Form.objects.get(pk=form_pk)

			return render(request, 'web/form_view.html', {'user':user,'form':form})

		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)

def form_delete(request, form_pk):

	try:

		user_pk = request.session.get('user')
		user = None

		if user_pk:
			user = User.objects.get(pk=user_pk)
			form = Form.objects.get(pk=form_pk)
			form.delete()
			sp = subprocess.Popen(['/bin/bash', '-i', '-c', 'delete'])
			sp.communicate()
			return HttpResponseRedirect(reverse('web:list'), {'user':user})

		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)

def form_delete_all(request):

	try:

		user_pk = request.session.get('user')
		user = None

		if user_pk:
			user = User.objects.get(pk=user_pk)
			Form.objects.all().delete()
			sp = subprocess.Popen(['/bin/bash', '-i', '-c', 'delete'])
			sp.communicate()
			HttpResponseRedirect(reverse('web:list'), {'user':user})

		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)

def file_delete(request):

	try:

		user_pk = request.session.get('user')
		user = None

		if user_pk:
			user = User.objects.get(pk=user_pk)
			if request.method == 'POST':
				file = request.POST.get('file_name', None)
				os.system("rm -rf "+file)
				sp = subprocess.Popen(['/bin/bash', '-i', '-c', 'delete'])
				sp.communicate()

			return HttpResponseRedirect(reverse('web:list'), {'user':user})

		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)

def file_delete_all(request):

	try:

		user_pk = request.session.get('user')
		user = None

		if user_pk:
			user = User.objects.get(pk=user_pk)
			sp = subprocess.Popen(['/bin/bash', '-i', '-c', 'file_delete'])
			sp.communicate()
			sp = subprocess.Popen(['/bin/bash', '-i', '-c', 'delete'])
			sp.communicate()

			return HttpResponseRedirect(reverse('web:list'), {'user':user})

		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)

def file_view(request):

	try:

		user_pk = request.session.get('user')
		user = None

		if user_pk:
			user = User.objects.get(pk=user_pk)
			if request.method == 'POST':
				file_name = request.POST.get('file_name', None)
				file = open(file_name, 'r', encoding='UTF8')
				text = file.readlines()
				file.close()

			return render(request, 'web/file_view.html', {'user':user,'text':text,'file_name':file_name})

		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)

def file_edit(request):

	try:

		user_pk = request.session.get('user')
		user = None

		if user_pk:
			user = User.objects.get(pk=user_pk)
			if request.method == 'POST':
				file = request.POST.get('file_name', None)
				new_name = request.POST.get('file_new_name', None)
				new_file = path+new_name+".txt"
				os.system("mv "+file+" "+new_file)
				sp = subprocess.Popen(['/bin/bash', '-i', '-c', 'delete'])
				sp.communicate()

			return HttpResponseRedirect(reverse('web:list'), {'user':user})

		return HttpResponseRedirect(reverse('web:login'))

	except Exception as err:
		HttpResponse(status=404)
