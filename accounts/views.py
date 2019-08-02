import re 
from django.shortcuts import render, redirect, Http404
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm #ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import EmailConfirmed, Role
from django.urls import reverse

# Create your views here.
def dashboard(request):
	return render(request, 'accounts/dashboard.html', {'user':request.user})
def register(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			print('VALID')
			username = form.cleaned_data.get('username')
			position = form.cleaned_data.get('position')
			role = Role(title=position)
			role.save()
			messages.success(request, f'Account created for {username}! Check your email to confirm your email address.')
			return redirect('register')

	else:
		form = UserRegisterForm()
	return render(request, 'accounts/register.html', {'form':form})

SHA1_RE = re.compile('^[a-f0-9]{40}$')
def activation_view(request, activation_key):
	if SHA1_RE.search(activation_key):
		print ('activation key is valid')
		try:
			user_confirmed = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			user_confirmed = None
			messages.success(request, 'There was an error with your request')
			return redirect('register')
		if user_confirmed is not None and not user_confirmed.confirmed:
			message = 'Confirmation Successful!!'
			user_confirmed.confirmed = True
			#user_confirmed.activation_key = 'confirmed'
			user_confirmed.save()
			messages.success(request, 'Your account has been activated! You can now <a href={}>Login</a>'.format(reverse("login")), extra_tags='safe')
		
		elif user_confirmed is not None and user_confirmed.confirmed:
			message = 'Already confirmed'
			messages.success(request, 'Your account has already been activated! <a href={}>Login</a>'.format(reverse("login")), extra_tags='safe')
		
		
		else:
			message = ''
		context = {'message':message}
		return render(request, 'accounts/activation.html', context)
	else:
		raise Http404

# @login_required
# def profile(request):
# 	if request.method=='POST':
# 		u_form = UserUpdateForm(request.POST, instance=request.user)
# 		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

# 		if u_form.is_valid() and p_form.is_valid():
# 			u_form.save()
# 			p_form.save()
# 			messages.success(request, f'Your account has been updated!')
# 			return redirect('profile')


# 	else:
# 		u_form = UserUpdateForm(instance=request.user)
# 		p_form = ProfileUpdateForm(instance=request.user.profile)


# 	context = {
# 		'u_form': u_form,
# 		'p_form': p_form
# 	}
# 	return render(request, 'profile.html', context)