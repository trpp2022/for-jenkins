from django.http import HttpResponse
from django.shortcuts import render

from .models import Data


def index(request):
    latest_question_list = Data.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'homeapp/index.html', context)
	
def detail(request, data_id):
    try:
        data = Data.objects.get(pk=data_id)
    except Data.DoesNotExist:
        raise Http404("Data does not exist")
    return render(request, 'homeapp/detail.html', {'data': data})