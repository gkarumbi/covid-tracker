from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.contrib.auth.models import User
from .models import   Contact
# Create your views here.
def home(request):
    pass

def index_test(request):
    title = "Covid Index Bootstrap Test"

    return render(request, 'index.html', {"title": title})



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    contact = Contact.objects.get(pk=current_user.id)

    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact =form.save(commit=False)
            contact.save()

        return redirect('/')
    else:
        form = ContactForm()

    return render(request, 'profile.html', {'contact':contact,'form':form}, locals())


