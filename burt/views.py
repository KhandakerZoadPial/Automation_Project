from django.shortcuts import render, redirect
from .models import QueryHolder

# Create your views here.
def home(request):
    if request.method == 'POST':
        query = request.POST.get('query_select')
        if query == 'burt':
            return redirect('/burt')
        elif query == 'Jira':
            pass
        elif query == 'QTest':
            pass
    else:
        return render(request, 'burt/home.html')


def burt_(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if 'submit' in request.POST:
            print('submit button pressed')
            import os
            return render(request, 'burt/result.html')
        elif 'save' in request.POST:
            # save the query in Database
            obj = QueryHolder()
            obj.query = query
            obj.save()
            return redirect('/burt')
    else:
        return render(request, 'burt/save_or_submit.html')