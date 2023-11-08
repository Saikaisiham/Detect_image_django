from django.shortcuts import render
from django.http import HttpResponse

from .producer import send_message
from .management.commands.consumer import Command
from .detect_images import detect_image

# def index(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         send_message(message)
#         return HttpResponse(f'Message sent successfully ,{message}')
#     else:
        
#         return render(request, 'index.html')

# def start_consuming_view(request):
#     start_consuming()
#     return HttpResponse('Consuming messages from RabbitMQ')


def index(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        process_image = detect_image(image)
        print('processd')
    return  render(request , 'index.html')