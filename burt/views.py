from multiprocessing import context
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
        open_new = request.POST.get('open_new')
        if 'Dg2Au' in open_new:
            open_new_type = 1
        elif 'Dg2AuPB1' in open_new:
            open_new_type = 2
        
        test_me = request.POST.get('test_me')
        if 'Dg2Au' in test_me:
            test_me_type = 1
        elif 'Dg2AuPB1' in open_new:
            test_me_type = 2

        study = request.POST.get('study')
        if 'Dg2Au' in study:
            study_type = 1
        elif 'Dg2AuPB1' in open_new:
            study_type = 2

        fixed = request.POST.get('fixed')
        if 'Dg2Au' in fixed:
            fixed_type = 1
        elif 'Dg2AuPB1' in open_new:
            fixed_type = 2

        closed = request.POST.get('closed')
        if 'Dg2Au' in open_new:
            closed_type = 1
        elif 'Dg2AuPB1' in open_new:
            closed_type = 2

        if 'submit' in request.POST:
            open_new =   send_req_get_data(open_new).lower()
            test_me =   send_req_get_data(test_me).lower()
            study =   send_req_get_data(study).lower()
            fixed =   send_req_get_data(fixed).lower()
            closed =   send_req_get_data(closed).lower()

            # 0=new/open 1=testme 2=study 3=fixed 4=closed 5=multistate
            Dg2Au = [0, 0, 0, 0, 0, 0]
            Dg2AuPB1 = [0, 0, 0, 0, 0, 0]
            if open_new_type == 1:
                Dg2Au[0] =  Dg2Au[0] + open_new.count('new/open')
                Dg2Au[1] =  Dg2Au[1] + open_new.count('testme')
                Dg2Au[2] =  Dg2Au[2] + open_new.count('study')
                Dg2Au[3] =  Dg2Au[3] + open_new.count('fixed')
                Dg2Au[4] =  Dg2Au[4] + open_new.count('closed')
                Dg2Au[5] =  Dg2Au[5] + open_new.count('multistate')
            else:
                Dg2AuPB1[0] =  Dg2AuPB1[0] + open_new.count('new/open')
                Dg2AuPB1[1] =  Dg2AuPB1[1] + open_new.count('testme')
                Dg2AuPB1[2] =  Dg2AuPB1[2] + open_new.count('study')
                Dg2AuPB1[3] =  Dg2AuPB1[3] + open_new.count('fixed')
                Dg2AuPB1[4] =  Dg2AuPB1[4] + open_new.count('closed')
                Dg2AuPB1[5] =  Dg2AuPB1[5] + open_new.count('multistate')

            if test_me_type == 1:
                Dg2Au[0] =  Dg2Au[0] + test_me.count('new/open')
                Dg2Au[1] =  Dg2Au[1] + test_me.count('testme')
                Dg2Au[2] =  Dg2Au[2] + test_me.count('study')
                Dg2Au[3] =  Dg2Au[3] + test_me.count('fixed')
                Dg2Au[4] =  Dg2Au[4] + test_me.count('closed')
                Dg2Au[5] =  Dg2Au[5] + test_me.count('multistate')
            else:
                Dg2AuPB1[0] =  Dg2AuPB1[0] + test_me.count('new/open')
                Dg2AuPB1[1] =  Dg2AuPB1[1] + test_me.count('testme')
                Dg2AuPB1[2] =  Dg2AuPB1[2] + test_me.count('study')
                Dg2AuPB1[3] =  Dg2AuPB1[3] + test_me.count('fixed')
                Dg2AuPB1[4] =  Dg2AuPB1[4] + test_me.count('closed')
                Dg2AuPB1[5] =  Dg2AuPB1[5] + test_me.count('multistate')

            if study_type == 1:
                Dg2Au[0] =  Dg2Au[0] + study.count('new/open')
                Dg2Au[1] =  Dg2Au[1] + study.count('testme')
                Dg2Au[2] =  Dg2Au[2] + study.count('study')
                Dg2Au[3] =  Dg2Au[3] + study.count('fixed')
                Dg2Au[4] =  Dg2Au[4] + study.count('closed')
                Dg2Au[5] =  Dg2Au[5] + study.count('multistate')
            else:
                Dg2AuPB1[0] =  Dg2AuPB1[0] + study.count('new/open')
                Dg2AuPB1[1] =  Dg2AuPB1[1] + study.count('testme')
                Dg2AuPB1[2] =  Dg2AuPB1[2] + study.count('study')
                Dg2AuPB1[3] =  Dg2AuPB1[3] + study.count('fixed')
                Dg2AuPB1[4] =  Dg2AuPB1[4] + study.count('closed')
                Dg2AuPB1[5] =  Dg2AuPB1[5] + study.count('multistate')

            
            if fixed_type == 1:
                Dg2Au[0] =  Dg2Au[0] + study.fixed('new/open')
                Dg2Au[1] =  Dg2Au[1] + study.fixed('testme')
                Dg2Au[2] =  Dg2Au[2] + study.fixed('study')
                Dg2Au[3] =  Dg2Au[3] + study.fixed('fixed')
                Dg2Au[4] =  Dg2Au[4] + study.fixed('closed')
                Dg2Au[5] =  Dg2Au[5] + study.fixed('multistate')
            else:
                Dg2AuPB1[0] =  Dg2AuPB1[0] + study.fixed('new/open')
                Dg2AuPB1[1] =  Dg2AuPB1[1] + study.fixed('testme')
                Dg2AuPB1[2] =  Dg2AuPB1[2] + study.fixed('study')
                Dg2AuPB1[3] =  Dg2AuPB1[3] + study.fixed('fixed')
                Dg2AuPB1[4] =  Dg2AuPB1[4] + study.fixed('closed')
                Dg2AuPB1[5] =  Dg2AuPB1[5] + study.fixed('multistate')

            
            if closed_type == 1:
                Dg2Au[0] =  Dg2Au[0] + study.closed('new/open')
                Dg2Au[1] =  Dg2Au[1] + study.closed('testme')
                Dg2Au[2] =  Dg2Au[2] + study.closed('study')
                Dg2Au[3] =  Dg2Au[3] + study.closed('fixed')
                Dg2Au[4] =  Dg2Au[4] + study.closed('closed')
                Dg2Au[5] =  Dg2Au[5] + study.closed('multistate')
            else:
                Dg2AuPB1[0] =  Dg2AuPB1[0] + study.closed('new/open')
                Dg2AuPB1[1] =  Dg2AuPB1[1] + study.closed('testme')
                Dg2AuPB1[2] =  Dg2AuPB1[2] + study.closed('study')
                Dg2AuPB1[3] =  Dg2AuPB1[3] + study.closed('fixed')
                Dg2AuPB1[4] =  Dg2AuPB1[4] + study.closed('closed')
                Dg2AuPB1[5] =  Dg2AuPB1[5] + study.closed('multistate')

            context = {
                'Dg2Au': Dg2Au,
                'Dg2AuPB1': Dg2AuPB1
            }

            return render(request, 'burt/result.html', context)
        elif 'save' in request.POST:
            # save the query in Database
            # obj = QueryHolder()
            # obj.query = query
            # obj.save()
            return redirect('/burt')
    else:
        return render(request, 'burt/save_or_submit.html')


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