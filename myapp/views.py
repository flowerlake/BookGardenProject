from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from myapp.models import Book, User, Sta_fkm, Sta_sit2, Sta_push2, Sta_chining2, sleep_status, Book_loan, Book_loan_copy
import json
from datetime import datetime
from myapp.user import Userform


# Create your views here.
@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'base.html')


def detail(request, my_args):
    post = Book.objects.all()[int(my_args)]
    str = ("book_name=%s,add_time=%s".format(post.book_name, post.date_time))
    return HttpResponse(str)


def test(request):
    return render(request, 'template.html', {'current_time': datetime.now()})


def signin(request):
    csrf = {}
    id = request.POST.get('stu_id', False)
    password = request.POST.get('password', False)
    csrf['rlt'] = "denglu"
    if password and id:
        try:
            user = User.objects.get(user_id=id)
        except:
            return render(request, 'login/login.html')
        if user.password == password:
            # 更新登录状态
            User.objects.filter(user_id=id).update(is_authenticated=True)
            return render(request, 'base.html')
    return render(request, 'signin.html', csrf)


def signup(request):
    return render(request, 'register.html')


def activities(request):
    return render(request, 'home.html')


def logout(request):
    id = request.POST.get('stu_id', None)
    User.objects.filter(user_id=id).update(is_authenticated=False)
    return redirect('login/login.html')


def login(request):
    csrf = {}
    if request.method == 'POST':
        infomation = request.POST
        id = request.POST.get('stu_id', None)
        password = request.POST.get('password', None)
        csrf['rlt'] = id
        if infomation.get('email'):
            User.objects.create(email=infomation['email'], user_id=infomation['stu_id'],
                                user_name=infomation['stu_name'], password=infomation['confirmPassword'],
                                user_qd=infomation['stu_qd'], user_class=infomation['stu_class'],
                                dorm_num=infomation['stu_dorm'])
            csrf['rlt'] = "注册"
            return render(request, 'base.html', csrf)
        else:
            if password and id:
                try:
                    user = User.objects.get(user_id=id)
                except:
                    return render(request, 'login/login.html')

                if user.password == password:
                    csrf["rlt"] = "登录"
                    # 更新登录状态
                    User.objects.filter(user_id=id).update(is_authenticated=True)
                    user_info = User.objects.get(user_id=id)
                    csrf = {
                        "id": user_info.user_id,
                        "name": user_info.user_name,
                        "email": user_info.email,
                        "qd": user_info.user_qd,
                        "class": user_info.user_class,
                        "dorm_num": user_info.dorm_num
                    }
                    return render(request, 'people/activities.html', csrf)
    return render(request, 'login/login.html')


def show_books(request):
    response = {}
    csrf = {}
    isbn = ""
    if request.method == 'POST':
        book_info = request.POST
        if book_info['return_time'] == '1':
            try:
                x = list(Book_loan.objects.filter(user_id=book_info['stu_id']))
                if len(x) != 0:
                    response['rlt2'] = "你已借过一本书，请还书后再次借阅."
                    return render(request, 'home.html', response)
                else:
                    Book_loan.objects.create(book_name=book_info['book_name'], user_id=book_info['stu_id'],
                                             add_time=book_info['borrow_time'])
                    obj = Book.objects.get(book_name=book_info['book_name'])
                    obj.book_num -= 1
                    obj.save()
                    response['rlt2'] = "借阅成功"
                    return render(request, 'home.html', response)
            except Exception as e:
                response['rlt2'] = str(e)
                return render(request, 'home.html', response)
        elif book_info['borrow_time'] == '1':
            try:
                obj1 = Book_loan.objects.get(user_id=book_info['stu_id'], book_name=book_info['book_name'])
                obj1.return_time = book_info['return_time']
                obj1.save()
                Book_loan_copy.objects.create(user_id=obj1.user_id, book_name=obj1.book_name, add_time=obj1.add_time,
                                              return_time=obj1.return_time)
                Book_loan.objects.get(user_id=book_info['stu_id'], book_name=book_info['book_name']).delete()
                obj2 = Book.objects.get(book_name=book_info['book_name'])
                obj2.book_num += 1
                obj2.save()
                response['rlt2'] = "还书成功"
                return render(request, 'home.html', response)
            except Exception as e:
                response['rlt2'] = str(e)
                return render(request, 'home.html', response)
        # response['rlt2'] = str(book_info['return_time'])
        return render(request, 'load_book.html')

    if request.method == 'GET':
        try:
            book_search = request.GET.get('book_name')
            info = [str(i) for i in list(Book.objects.filter(book_name__contains=book_search))]
            csrf['rlt'] = []
            for i in info:
                book_obj = Book.objects.get(book_name=i)
                csrf['rlt'].append({
                    "book_id": book_obj.isbn,
                    "book_name": book_obj.book_name,
                    "book_num": book_obj.book_num
                })
            # 所有书籍信息
            # csrf['rlt2'] = [i[0] for i in list(Book.objects.values_list('book_name'))]
        except Exception as e:
            csrf['rlt'] = []
        return render(request, 'load_book.html', csrf)

    return render(request, 'load_book.html')


def stamina(request):
    # csrf = {}
    if request.method == 'POST':
        info_drill = request.POST
        Sta_fkm.objects.create(user_id=info_drill['stu_id'], five_km=info_drill['five_km'])
        Sta_chining2.objects.create(user_id=info_drill['stu_id'], chining=info_drill['sta_chining'])
        Sta_sit2.objects.create(user_id=info_drill['stu_id'], sit_up=info_drill['sta_sit'])
        Sta_push2.objects.create(user_id=info_drill['stu_id'], push_up=info_drill['sta_push'])
        return HttpResponse("添加成功")
    return render(request, 'stamina.html')


def sleep(request):
    if request.method == 'POST':
        info_sleep = request.POST
        sleep_status.objects.create(time_rating=info_sleep['time_rating'], time=info_sleep['time'])
        return HttpResponse("添加成功")

    if request.method == 'GET':
        try:
            csrf = {
                "time": [i[0].strftime("%Y-%m-%d") for i in list(sleep_status.objects.values_list('time'))],
                "time_rating": [i[0] for i in list(sleep_status.objects.values_list('time_rating'))]
            }
            return render(request, "sleep.html", csrf)
        except Exception as e:
            return HttpResponse(e)
