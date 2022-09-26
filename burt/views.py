from multiprocessing import context
from django.shortcuts import render, redirect
from .models import QueryHolder, HelperModel




def new_home(request):
    if request.method == 'POST':
        type_new_modify = request.POST.get('type_new_modify')
        report_name = request.POST.get('report_name')
        if type_new_modify == 'new':
            return render(request, 'burt/home.html')
        else:
            pass
    else:
        return render(request, 'burt/new_home.html')


def home(request):
    if request.method == 'POST':
        query = request.POST.get('query_select')
        if query == 'burt':
            num_of_queries = request.POST.get('num_of_queries')
            return redirect(f'/query_boss/{num_of_queries}')
        elif query == 'Jira':
            pass
        elif query == 'QTest':
            pass
    else:
        return render(request, 'burt/home.html')


def query_boss(request, num_of_queries):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        keywords = keywords.split(',')
        names = []
        new = []
        for i in range(int(num_of_queries)):
            name = request.POST.get(f'name_{i+1}')

            query_ = request.POST.get(f'q_{i+1}')

            # counting for every keyword then keeping the result inside res dict
            result = send_req_get_data(query_).lower()
            tmp_dict = {}
            for word in keywords:
                tmp = result.count(word.lower())
                tmp_dict[word] = tmp
            
            if name not in names:
                names.append(name)
                new.append([name, tmp_dict])
            else:
                for item in new:
                    if name in item[0]:
                        pial_ = item[1]
                        for w in keywords:
                            pial_[w] = pial_[w] + tmp_dict[w]
                        item[1] = pial_
                        # names.append(name)
                        break
        context = {
            'result': new,
            'keywords': keywords
        }

        return render(request, 'burt/new_result.html', context)

    else:
        my_list = []
        for i in range(int(num_of_queries)):
            my_list.append(i+1)
        context = {
            'list_': my_list,
            'num_of_queries': num_of_queries
        }
        return render(request, 'burt/query_boss.html', context)

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