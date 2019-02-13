from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader
from TestApp.models import AppDetails, Screen
from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.

def index(request):
    all_apps = AppDetails.objects.all()
    # template = loader.get_template('TestApp/index.html')
    context = {
        'all_apps' : all_apps
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'TestApp/index.html', context)


def detail(request, id):
    # try:
    #     app = AppDetails.objects.get(pk=id)
    # except AppDetails.DoesNotExist:
    #     raise Http404('app detail does not exist')
    app = get_object_or_404(AppDetails, pk=id)
    return render(request, 'TestApp/detail.html', {'app' : app})

def fav(request, id):
    app = get_object_or_404(AppDetails, pk=id)
    print(app)
    print('******')
    try:
        selected_screen = app.screen_set.get(pk=request.POST['screen'])
        print('selected screen : ', selected_screen)
    except (KeyError, Screen.DoesNotExist):
        return render(request, 'TestApp/detail.html', {
            'app': app,
            'error_message' :   'You did not select a valid screen.'
        })
    else:
        selected_screen.is_fav = True
        selected_screen.save()
        return render(request, 'TestApp/detail.html', {'app': app})

