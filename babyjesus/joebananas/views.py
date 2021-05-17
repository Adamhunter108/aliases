from django.shortcuts import render
from .models import Names
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddNameForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.urls import reverse_lazy

def home(request):
	all_names = Names.objects.all()
	random_name = random.choice(all_names)
	context = {
		#'name': Names.objects.first() # this should be changed to random somehow
		'name': random_name
	}
	return render(request, 'joebananas/home.html', context)
	

@login_required
def add_name(request):
	
	model = Names

	form = AddNameForm(request.POST or None)

	if form.is_valid():
		form.save()

	context = {
		'form': form
	}

	print(request.POST)
	# checking the submission in the console

	# return render(request, "joebananas/add_name.html", {'form': form})
	# another way to pass context

	return render(request, "joebananas/add_name.html", context)
	

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
 	
	user =  authenticate(request, username=username, password=password)
	
	if user is not None:
		login(request, user)
		render("joebananas/home.html")
	else:
		render(request, "joebananas/login.html", context)


def log_out(request):
    logout(request)
    return redirect("joebananas/home.html")

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/sign_up.html"