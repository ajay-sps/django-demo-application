from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import Book
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse('Hello this is the index page of poll app')

def softprodigy(request):
    return render(request,'softprodigy.html')

@csrf_exempt
def book(request):
    if request.method == 'POST' :
        data = json.loads(request.body)
        title = data.get('title')
        author = data.get('author')

        book = Book.objects.create(title = title,author = author)

        response_data = {
            'id' : book.id,
            'title' : book.title,
            'author' : book.author,
        }

        return JsonResponse(response_data,status = 201)
    
    return JsonResponse({'error':'invalid request'},status = 400)

@csrf_exempt
def delete_book(request,pk):
    try:
        book = Book.objects.get(id = pk)
    except Book.DoesNotExist:
        return JsonResponse({"Error ": "Book doesnot exist"},status = 400)
    
    # print(book.id)
    print(pk)
    if request.method == "DELETE" :
        # book = Book.objects.get(id = pk)
        book.delete()
        return JsonResponse({'message':"book deleted successfully"},status = 204)
    
    elif request.method == "PUT" :
        data = json.loads(request.body)

        book.title = data.get('title',book.title)
        book.author = data.get('author',book.author)

        book.save()
        return JsonResponse({'message':"book updated successfully"},status = 200)
    
    return JsonResponse({'Error':'Invalid request'},status = 400)