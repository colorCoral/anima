from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import auth

from app01 import form
from app01 import models

# Create your views here.


# 注册
def register(request):

    if request.method == 'GET':
        form_obj = form.UserForm
        return render(request, 'register.html', {'form_obj': form_obj})
    else:
        form_obj = form.UserForm(request.POST)

        if form_obj.is_valid():
            data = form_obj.cleaned_data
            data.pop('r_password')
            models.UserInfo.objects.create_user(**data)
            return redirect('login')
        else:
            return render(request, 'register.html', {'form_obj': form_obj})


# 后端登录 color  w123456
def login(request):

    response_msg = {'code': None, 'msg': None}
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # valid_code = request.POST.get('valid_code')
        valid_code = '1111'

        # 后端暂时不调用验证码，后期加上
        # if valid_code.upper() == request.session.get('valid_str').upper():
        if valid_code.upper() == '1111':
            # 这里auth是django提供的方法，用来检验用户名和密码
            user_obj = auth.authenticate(username=username, password=password)
            if user_obj:
                # 这里使用了auth方法，自动添加了session
                auth.login(request, user_obj)
                response_msg['code'] = 1000
                response_msg['msg'] = '登录成功'
                request.session['username'] = username
                # 暂时不打开，后期权限
                # initial_session(request, user_obj)
            else:
                response_msg['code'] = 1001
                response_msg['msg'] = '用户名或者密码错误'
        else:
            response_msg['code'] = 1001
            response_msg['msg'] = '验证码错误'

    return JsonResponse(response_msg)


#  后端首页
def index(request):

    if request.method == 'GET':

        return render(request, 'h_index.html')
    else:
        pass

