from django.contrib.auth.hashers import check_password
from django.core.checks import messages
from django.shortcuts import render, redirect
from shop.models import Category
from accounts.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth import get_user_model


from blog.models import Post
from django.utils import timezone


User = get_user_model()


def register(request):
    if request.method == "POST": #어떤 방식을 사용하여 들어왔는지 알 수 있다.
        # 회원 가입 데이터 입력 완료
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():# 유효성 확인 입력데이터를 모두 입력했는지 확인
            new_user = user_form.save(commit=False) #저장을 진행하면 해당 폼의 인스턴스..?
            new_user.set_password(user_form.cleaned_data['password']) #
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        # 회원 가입 내용을 입력하는 상황
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})


@csrf_exempt
@login_required
def delete(request):
    categories = Category.objects.all()
    if request.method == "POST":
        password_del = request.POST["password_del"]
        user = request.user
        if check_password(password_del, user.password):
            user.delete()
            return redirect('/')
    return render(request, 'registration/delete.html', {'categories': categories})


def change_password(request):
    if request.method == "POST":
        user = request.user
        origin_password = request.POST["origin_password"]
        if check_password(origin_password, user.password):
            new_password = request.POST["new_password"]
            confirm_password = request.POST["confirm_password"]
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return redirect('/')
            else:
                messages.error(request, 'Password not same')
        else:
            messages.error(request, 'Password not correct')
        return render(request, 'registration/change_password.html')
    else:
        return render(request, 'registration/change_password.html')


def mypage(request):
    return render(request, 'registration/mypage.html')


def myboard(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'registration/myboard.html', {'posts': posts})



