from django.shortcuts import render
from .forms import FichaForm

# Create your views here.

#Show fichas
def fichas_list(request):
	return render(request, 'fichas/fichas_list.html')

#Instert and update operation
def fichas_form(request):
	form = FichaForm()
	return render(request, 'fichas/fichas_form.html', {'form':form})

#Delete ficha
def fichas_delete(request):
	return