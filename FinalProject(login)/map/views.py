from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required #可在函數前假如@login_required
from django.views.generic import TemplateView
from map.forms import HomeForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	return render(request, 'map/home.html')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/map/login')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'map/reg_form.html', args)

def add(request):
    return render(request, 'map/add.html')


class HomeView(TemplateView):
    template_name = 'map/add.html'

    def get(self,request):
        form = HomeForm()
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data
            
            form = HomeForm()
            return redirect('/map/diary')


        return render(request, self.template_name, {'form': form,'text' : text,'image':image})



