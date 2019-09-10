from django.http import JsonResponse
from django.shortcuts import render
from .models import Event, EventLocation


def index(request):
    locations = EventLocation.objects.all()
    latest_events = Event.objects.all().distinct().order_by('-date_end')[0:20]
    return render(request, 'index.html', {'locations': locations, 'latest_events': latest_events})


def get_events(request):
    """
    Get events (page - 1) + n

    :param request:
    :return:
    """
    page = request.GET.get('page')
    if not page:
        page = 1
    n = request.GET.get('n_events')
    if not n:
        n = 20
    start = (page - 1) + n
    end = start + n
    events = Event.objects.all().distinct().order_by('-date_end')[start:end]
    return JsonResponse({'events': events, 'page': page, 'n_events': n}, status=200)
