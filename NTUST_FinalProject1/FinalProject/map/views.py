from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Photo,Map
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm


def photo_list(request):
	queryset = Photo.objects.all()
	context = {
		"photos": queryset,
	}
	return render(request, "map/MainPage.html", context)

#def record(request):
#	queryset = Map.objects.all()
#	context = {
#		"maps":queryset,
#	}
#	return  render(request, "map/record.html",context)

def diary(request):
 	maps = Map.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
 	return render(request, 'map/diary.html',{'maps':maps})

def Diary_Page(request):
	queryset = Map.objects.all()
	context = {
		"maps":queryset,
	}
	return  render(request, "map/Diary_Page.html",context)
def home(request):
	return render(request, 'map/MainPage.html')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/map/Login_Page')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'map/Register_Page.html', args)

