from multiprocessing import context
from django.shortcuts import render, redirect
from .models import QueryHolder, HelperModel

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
        open_new = request.POST.get('open_new')
        test_me = request.POST.get('test_me')
        study = request.POST.get('study')
        fixed = request.POST.get('fixed')
        closed = request.POST.get('closed')
        multistate = request.POST.get('multistate')
        

        if 'submit' in request.POST:
            open_new = send_req_get_data(open_new).lower()
            test_me = send_req_get_data(test_me).lower()
            study = send_req_get_data(study).lower()
            fixed = send_req_get_data(fixed).lower()
            closed = send_req_get_data(closed).lower()
            multistate = send_req_get_data(multistate).lower()

            # 0=new/open 1=testme 2=study 3=fixed 4=closed 5=multistate     
            Dg2Au = [0, 0, 0, 0, 0, 0]    
            Dg2Au[0] =  Dg2Au[0] + open_new.count('new')
            Dg2Au[0] =  Dg2Au[0] + open_new.count('open')
            Dg2Au[1] =  Dg2Au[1] + open_new.count('testme')
            Dg2Au[2] =  Dg2Au[2] + open_new.count('study')
            Dg2Au[3] =  Dg2Au[3] + open_new.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + open_new.count('closed')
            Dg2Au[5] =  Dg2Au[5] + open_new.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + test_me.count('new')
            Dg2Au[0] =  Dg2Au[0] + test_me.count('open')
            Dg2Au[1] =  Dg2Au[1] + test_me.count('testme')
            Dg2Au[2] =  Dg2Au[2] + test_me.count('study')
            Dg2Au[3] =  Dg2Au[3] + test_me.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + test_me.count('closed')
            Dg2Au[5] =  Dg2Au[5] + test_me.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + study.count('new')
            Dg2Au[0] =  Dg2Au[0] + study.count('open')
            Dg2Au[1] =  Dg2Au[1] + study.count('testme')
            Dg2Au[2] =  Dg2Au[2] + study.count('study')
            Dg2Au[3] =  Dg2Au[3] + study.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + study.count('closed')
            Dg2Au[5] =  Dg2Au[5] + study.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + fixed.count('new')
            Dg2Au[0] =  Dg2Au[0] + fixed.count('open')
            Dg2Au[1] =  Dg2Au[1] + fixed.count('testme')
            Dg2Au[2] =  Dg2Au[2] + fixed.count('study')
            Dg2Au[3] =  Dg2Au[3] + fixed.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + fixed.count('closed')
            Dg2Au[5] =  Dg2Au[5] + fixed.count('multistate')

            Dg2Au[0] =  Dg2Au[0] + closed.count('new')
            Dg2Au[0] =  Dg2Au[0] + closed.count('open')
            Dg2Au[1] =  Dg2Au[1] + closed.count('testme')
            Dg2Au[2] =  Dg2Au[2] + closed.count('study')
            Dg2Au[3] =  Dg2Au[3] + closed.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + closed.count('closed')
            Dg2Au[5] =  Dg2Au[5] + closed.count('multistate')


            Dg2Au[0] =  Dg2Au[0] + multistate.count('new')
            Dg2Au[0] =  Dg2Au[0] + multistate.count('open')
            Dg2Au[1] =  Dg2Au[1] + multistate.count('testme')
            Dg2Au[2] =  Dg2Au[2] + multistate.count('study')
            Dg2Au[3] =  Dg2Au[3] + multistate.count('fixed')
            Dg2Au[4] =  Dg2Au[4] + multistate.count('closed')
            Dg2Au[5] =  Dg2Au[5] + multistate.count('multistate') 

            # todo: add the same thing for multistate

            obj = HelperModel()
            obj.open_new = Dg2Au[0]
            obj.test_me = Dg2Au[1]
            obj.study = Dg2Au[2]
            obj.fixed = Dg2Au[3]
            obj.closed = Dg2Au[4]
            obj.multistate = Dg2Au[5]
            obj.total = Dg2Au[0] + Dg2Au[1] + Dg2Au[2] + Dg2Au[3] + Dg2Au[4] + Dg2Au[5]
            obj.save()
            return redirect(f'/burt2/{obj.pk}')

        elif 'save' in request.POST:
            # save the query in Database
            # obj = QueryHolder()
            # obj.query = query
            # obj.save()
            return redirect('/burt')
    else:
        return render(request, 'burt/save_or_submit.html')


def burt__(request, pk):
    obj = HelperModel.objects.get(pk=pk)
    if request.method == 'POST':
        open_new = request.POST.get('open_new')
        test_me = request.POST.get('test_me')
        study = request.POST.get('study')
        fixed = request.POST.get('fixed')
        closed = request.POST.get('closed')
        multistate = request.POST.get('multistate')
        open_new = send_req_get_data(open_new).lower()
        test_me = send_req_get_data(test_me).lower()
        study = send_req_get_data(study).lower()
        fixed = send_req_get_data(fixed).lower()
        closed = send_req_get_data(closed).lower()
        multistate = send_req_get_data(multistate).lower()

        # 0=new/open 1=testme 2=study 3=fixed 4=closed 5=multistate     
        Dg2Au = [0, 0, 0, 0, 0, 0]      
        Dg2Au[0] =  Dg2Au[0] + open_new.count('new')
        Dg2Au[0] =  Dg2Au[0] + open_new.count('open')
        Dg2Au[1] =  Dg2Au[1] + open_new.count('testme')
        Dg2Au[2] =  Dg2Au[2] + open_new.count('study')
        Dg2Au[3] =  Dg2Au[3] + open_new.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + open_new.count('closed')
        Dg2Au[5] =  Dg2Au[5] + open_new.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + test_me.count('new')
        Dg2Au[0] =  Dg2Au[0] + test_me.count('open')
        Dg2Au[1] =  Dg2Au[1] + test_me.count('testme')
        Dg2Au[2] =  Dg2Au[2] + test_me.count('study')
        Dg2Au[3] =  Dg2Au[3] + test_me.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + test_me.count('closed')
        Dg2Au[5] =  Dg2Au[5] + test_me.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + study.count('new')
        Dg2Au[0] =  Dg2Au[0] + study.count('open')
        Dg2Au[1] =  Dg2Au[1] + study.count('testme')
        Dg2Au[2] =  Dg2Au[2] + study.count('study')
        Dg2Au[3] =  Dg2Au[3] + study.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + study.count('closed')
        Dg2Au[5] =  Dg2Au[5] + study.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + fixed.count('new')
        Dg2Au[0] =  Dg2Au[0] + fixed.count('open')
        Dg2Au[1] =  Dg2Au[1] + fixed.count('testme')
        Dg2Au[2] =  Dg2Au[2] + fixed.count('study')
        Dg2Au[3] =  Dg2Au[3] + fixed.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + fixed.count('closed')
        Dg2Au[5] =  Dg2Au[5] + fixed.count('multistate')

        Dg2Au[0] =  Dg2Au[0] + closed.count('new')
        Dg2Au[0] =  Dg2Au[0] + closed.count('open')
        Dg2Au[1] =  Dg2Au[1] + closed.count('testme')
        Dg2Au[2] =  Dg2Au[2] + closed.count('study')
        Dg2Au[3] =  Dg2Au[3] + closed.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + closed.count('closed')
        Dg2Au[5] =  Dg2Au[5] + closed.count('multistate')


        Dg2Au[0] =  Dg2Au[0] + multistate.count('new')
        Dg2Au[0] =  Dg2Au[0] + multistate.count('open')
        Dg2Au[1] =  Dg2Au[1] + multistate.count('testme')
        Dg2Au[2] =  Dg2Au[2] + multistate.count('study')
        Dg2Au[3] =  Dg2Au[3] + multistate.count('fixed')
        Dg2Au[4] =  Dg2Au[4] + multistate.count('closed')
        Dg2Au[5] =  Dg2Au[5] + multistate.count('multistate')        
        total = Dg2Au[0] + Dg2Au[1] + Dg2Au[2] + Dg2Au[3] + Dg2Au[4] + Dg2Au[5]
        # todo: add the same thing for multistate
        context = {
            'dg2au': obj,
            'open_new': Dg2Au[0],
            'test_me': Dg2Au[1],
            'study': Dg2Au[2],
            'fixed': Dg2Au[3],
            'closed': Dg2Au[4],
            'multistate': Dg2Au[5],
            'total1': obj.total,
            'total2': total
        }
        return render(request, 'burt/result.html', context)
    else:
        return render(request, 'burt/burt2.html')

# ----helpers---
def send_req_get_data(query):
    import paramiko

    host = "YOUR_IP_ADDRESS"
    username = "YOUR_LIMITED_USER_ACCOUNT"
    password = "YOUR_PASSWORD"

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout,_stderr = client.exec_command(query)
    x = _stdout.read().decode()
    client.close()
    return x