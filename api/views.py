from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 

from .models import Item

def test(request):
    return JsonResponse({'message':'hello world..!!'})


def add_item(request):
    if request.method == 'POST':
        title = request.POST.get('title','notdefined')
        description = request.POST.get('description','NOt')

        item = Item(title=title,description=description)
        item.save()
        return HttpResponse("item added..")


def delete_item(request,id):
    Item.objects.get(id=id).delete()
    return HttpResponse("delete")

def list_item(request):
    list = Item.objects.all()
    context = {'list': list}
    return render(request , 'index.html', context)


def update_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title','notdefined')
        description = request.POST.get('description','NOt')

        item.title = title
        item.description = description
        item.save()
        return HttpResponse("item updated..")


    