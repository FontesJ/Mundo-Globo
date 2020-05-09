from django.shortcuts import render
# from django.http import HttpResponse
from .models import Client
from .serializers import ClientSerializer
from django.http import JsonResponse


# def helloWorld(request):
#     return HttpResponse('Hello World!')


def index(request):
    rest_list = Client.objects.order_by('-data_pub')
    context = {'rest_list': rest_list}
    return render(request, 'conn/index.html', context)


# Rest api end point
def get_rest_list(request):
    """
    Retorna lista de usuários
    """
    if request.method == "GET":
        rest_list = Client.objects.order_by('-pub_date')
        serializer = ClientSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)


