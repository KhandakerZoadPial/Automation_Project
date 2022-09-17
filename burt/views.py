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
            my_str = """
            /usr/software/rats/bin/burt report -q'$date_create gt "20220101" && $state =~ /STUDY/ && $type =~ /TESTCASE/ && $subteam =~ /^(0|4|217)$/ && $subtype =~ /platform_scripts/ && ($title =~ /Dagger2|Dagger-2/i || $hw_platform =~ /dagger2/i)  && $keywords =~ /Dg2Au($|\s+|\,)/i' -f':date_create id state sev pri impact type subtype sub_by time_est keywords:30 owner mgr_owner title' -s'id date_create pri sev'
            """
            os.system(my_str)
            return render(request, 'burt/result.html')
        elif 'save' in request.POST:
            # save the query in Database
            obj = QueryHolder()
            obj.query = query
            obj.save()
            return redirect('/burt')
    else:
        return render(request, 'burt/save_or_submit.html')