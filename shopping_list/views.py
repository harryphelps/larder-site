from django.http import HttpResponse

from . import models


def index(request):
    shopping_list = models.Item.objects.all()
    return HttpResponse(shopping_list)
