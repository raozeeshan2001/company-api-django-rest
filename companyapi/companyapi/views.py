
from django.http import HttpResponse
from django.http import JsonResponse
def home_page(request):
    print('home page requested')
    friends=['ali','ahmed','rayyan']
    #return HttpResponse('this is home page')
    return JsonResponse(friends,safe=False)

