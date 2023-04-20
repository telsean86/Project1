from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
import requests
from shop.models import Product, Category
from .models import City
from .forms import CityForm
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    cities = City.objects.all()  # return all the cities in the database
    products = Product.objects.filter(available_display=True).order_by('category')
    category = Category.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&rang=kr&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    url1 = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&rang=kr&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()
    weather_data = []
    weather_data1 = []

    for city in cities:  # 반복문 시티스에 시티를 넣는 작업 그런데 여기서 없는 시티이름을 넣는다면 제이슨으로 바꿀떄 받아들일수 잇는게 없음
        city_weather = requests.get(
            url.format(city)).json()  # url을 json으로 바꾸는 작업 그래야 아래의 날씨 정보들을 가져옴
    try:

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],  # 없는 지역을 입력할때 오류가 나는 부분, 시티에 맞는 온도를 못찾기 때문 !잘못된 url전달
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }
        weather_data.append(weather)

        temps = weather.get('temperature')
        temps = int(temps)

        city_weather1 = requests.get(url1.format(city)).json()  # url을 json으로 바꾸는 작업 그래야 아래의 날씨 정보들을 가져옴
        for i in range(0, 40, 8):
            weekweather = {
                'city': city,
                'tempnext': city_weather1['list'][i]['main']['temp'],
                'icon': city_weather1['list'][i]['weather'][0]['icon'],
                'dt': city_weather1['list'][i+3]['dt_txt'],  # 가장 가까운 3시간마다 예보
                'dt2': city_weather1['list'][i + 6]['dt_txt'],  # 9시간 뒤 기온
                'tempnext9': city_weather1['list'][i + 3]['main']['temp'],
                'icon2': city_weather1['list'][i+3]['weather'][0]['icon'],
            }
            weather_data1.append(weekweather)
        if temps >= 28:
            temps = 8
            products = products.filter(temp__icontains=8)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)
        elif temps >= 23:
            temps = 7
            products = products.filter(temp__icontains=7)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)
        elif temps >= 20:
            temps = 6
            products = products.filter(temp__icontains=6)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)
        elif temps >= 17:
            temps = 5
            products = products.filter(temp__icontains=5)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)

        elif temps >= 12:
            temps = 4
            products = products.filter(temp__icontains=4)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)

        elif temps >= 9:
            temps = 3
            products = products.filter(temp__icontains=3)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)

        elif temps >= 5:
            temps = 2
            products = products.filter(temp__icontains=2)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)

        else:
            temps = 1
            products = products.filter(temp__icontains=1)
            if products:
                products_outer = products.filter(category=13)
                products_top = products.filter(category=14)
                products_onepiece = products.filter(category=15)
                products_skirt = products.filter(category=16)
                products_bottom = products.filter(category=17)
                f = request.GET.getlist('f')
                if f:
                    query = Q()
                    for i in f:
                        query = query | Q(style__icontains=i)
                        products_outer = products_outer.filter(query)
                        products_top = products_top.filter(query)
                        products_onepiece = products_onepiece.filter(query)
                        products_skirt = products_skirt.filter(query)
                        products_bottom = products_bottom.filter(query)
        randomot = Product.objects.filter(category=13).order_by('?')[0]
        randomto = Product.objects.filter(category=14).order_by('?')[0]
        randomon = Product.objects.filter(category=15).order_by('?')[0]
        randomsk = Product.objects.filter(category=16).order_by('?')[0]
        randombt = Product.objects.filter(category=17).order_by('?')[0]
    except KeyError:
        messages.error(request, '주소를 정확히 입력해주세요. (예: 서울특별시)')

    context = {'weather_data': weather_data, 'form': form, 'products': products, 'temps': temps, 'category': category,
               'products_top': products_top, 'products_outer': products_outer, 'products_onepiece': products_onepiece,
               'products_skirt': products_skirt, 'products_bottom': products_bottom, 'weather_data1': weather_data1,
               'randomot': randomot, 'randomto': randomto, 'randomon': randomon, 'randomsk': randomsk,'randombt': randombt}

    return render(request, 'weather/index.html', context)  # returns the index.html template


