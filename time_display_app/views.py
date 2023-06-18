
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from time import gmtime, strftime

def formater(num):
    if num == 1:
        return 'PM'
    return 'AM'

    
def home(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)


def update(request):
    data = get_datetime()
    return JsonResponse(data)



