from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .models import ReserveSelfcar
from _ast import Try

# Create your views here.
def selfcar(request):

    solutions = ReserveSelfcar.objects.all()
    
    # 1차 예약 정보 
    reservation_temp = []

    # test = Selfcar.objects.all()
    for i in range(1, 5):
        for j in range(1, 5):
            try:
                if ReserveSelfcar.objects.filter(reserv_day = i, reserv_time = j).count() > 0:
                    temp = ReserveSelfcar.objects.filter(reserv_day = i, reserv_time = j).count() 
                    reservation_temp.append(temp)
                else:
                    reservation_temp.append(None)
            except:
                reservation_temp.append(None)
 
    context = {"one": reservation_temp[0:4],
               "two": reservation_temp[4:8],
               "three": reservation_temp[8:12],
               "four": reservation_temp[12:16],}

    return render(request, 'selfcar/selfcar.html', context)


def selfcar_insert(request):
    try :
        count = ReserveSelfcar.objects.all().count()
    except:
        return HttpResponseRedirect('/selfcar/selfcar')
    
    context = { 'count' : count }

    return render(request, 'selfcar/selfcar_insert.html', context)


def selfcar_comf(request):
    return render(request, 'selfcar/selfcar_comf.html')


def exe_selfcar(request):
    
    # 동일 이름 이메일
    if ReserveSelfcar.objects.filter(name=request.POST['name'], email=request.POST['email']).count() > 0:
        return HttpResponseRedirect('/selfcar/selfcar_reject')
    
    # 10건이 넘은 경우
    if ReserveSelfcar.objects.filter(reserv_day = request.POST['day'], reserv_time =request.POST['time']).count() >= 10:
        return HttpResponseRedirect('/selfcar/selfcar_reject')
        
    reply = ReserveSelfcar()
    reply.name = request.POST['name']
    reply.email = request.POST['email']
    reply.reserv_day = request.POST['day']
    reply.reserv_time = request.POST['time']
    reply.save()
    
    return HttpResponseRedirect('/selfcar')


def selfcar_reject(request):
    return render(request, 'selfcar/selfcar_reject.html')


def exe_search_selfcar(request):
    
    selfcar_list = ReserveSelfcar.objects.filter(email=request.POST['email'])
    
    count = ReserveSelfcar.objects.filter(email=request.POST['email']).count()
    
    context = {'selfcar_list': selfcar_list, 'count': count,
               'email': request.POST['email'],}
    
    return render(request, 'selfcar/selfcar_comf.html', context)


def exe_delete_selfcar(request, selfcarid):
    try:
        person = ReserveSelfcar.objects.get(pk=selfcarid)
        person.delete()
        print("어디로 이동????????")
        return HttpResponseRedirect('/selfcar/selfcar_comf')
    except:
        return HttpResponseRedirect('/selfcar/selfcar_comf')


def selfcar_admin(request):
    return render(request, 'selfcar/selfcar_admin.html')
    
    
def exe_list_selfcar(request):
    
    rday = request.POST['day']
    rtime = request.POST['time']
    
    try:
        if rtime in [ '1', '2', '3', '4' ]:
            selfcar_list = ReserveSelfcar.objects.filter(reserv_day=rday, reserv_time=rtime)
        else:
            selfcar_list = ReserveSelfcar.objects.filter(reserv_day=rday)
        
        selfcar_list = selfcar_list.order_by('reserv_day', 'reserv_time')
    except:
        return HttpResponseRedirect('/selfcar/selfcar_reject')

    paginator = Paginator(selfcar_list, 41)
    page = request.GET.get('page')
    
    try:
        quest = paginator.page(page)
    except PageNotAnInteger:
        quest = paginator.page(1)
    except EmptyPage:
        quest = paginator.page(paginator.num_pages)
        
    context = {'questions': quest, 'q_list': selfcar_list, 'day': rday, 'time': rtime}
    
    return render(request, 'selfcar/selfcar_admin.html', context)
