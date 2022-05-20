from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import user_form_details
from .models import UserDetails

# Create your views here.
def userDetailsPage(request):
    pwd_err = ""
    if request.method == "POST":
        form = user_form_details(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            if UserDetails.objects.filter(user_email=email).exists():
                pwd_err = "Email already Reagistered"
            else:
                customer = UserDetails.objects.create(name=name)
                customer.user_email=email
                customer.save()
                messages.success(request, 'Your form is Successfully submitted')
                return redirect('userDetailsPage')
        else:
            pwd_err = "Input parameters are not valid, please check again."
            messages.error(request, 'Invalid form submission.')
            messages.error(request, pwd_err)
    else:
        form = user_form_details()
    return render(request, 'userFormPages/userdetailspage.html',{'form':form, 'pwd_err':pwd_err})