# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	context = {
		'title' : 'Loja Virtual da Nadja',
		'footer' : 'Desenvolvido Por OmnesTI'
	}

	return render(request, 'index.html', context)

def contact(request):
	return render(request, 'contact.html')

def product(request):
	return render(request, 'product.html')

def products(request):
	return render(request, 'products.html')