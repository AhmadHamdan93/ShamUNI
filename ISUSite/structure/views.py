from django.shortcuts import render
from .models import NavBar, MotionImage, News, Question, Adds, Success, Contact, Doctors, Photo


def homepage(request):
    doctor_list = Doctors.objects.all()

    nav = NavBar.objects.all()
    nav_new = check_nav_has_son(nav)

    motion = MotionImage.objects.all()
    all_news = News.objects.all()
    news = all_news[::-1]
    if len(news) > 3:
        news_list = news[:3]
    else:
        news_list = news[:]

    all_advert = Adds.objects.all()
    advert = all_advert[::-1]
    if len(advert) > 3:
        advert_list = advert[:3]
    else:
        advert_list = advert[:]

    short = []
    for item in news:
        if item.NShort != "":
            short.append(item.NShort)
    news_short = short[:5]
    success = Success.objects.all()
    contact = Contact.objects.all().first()
    question = Question.objects.all()
    context = {'nav': nav, 'motion': motion, 'news_list': news_list, 'success': success, 'news_short': news_short,
               'advert_list': advert_list, 'question': question, 'contact': contact, 'doctor_list': doctor_list,
               'nav_new': nav_new}
    return render(request, 'structure/Main.html', context)


def check_nav_has_son(nav):
    check_son = []
    for idx in range(nav.count()):
        check_son.append(False)
    for idx in range(nav.count()):
        for n1 in nav:
            if str(n1.NAVHasFather) == str(nav[idx].NAVName):
                check_son[idx] = True
    new_nav = []
    for idx in range(nav.count()):
        n = {'NAVName': nav[idx].NAVName, 'NAVHasFather': nav[idx].NAVHasFather, 'NAVHtml': nav[idx].NAVHtml,
             'NAVSlug': nav[idx].NAVSlug, 'son': check_son[idx]}

        new_nav.append(n)

    return new_nav


def nav_detail(request, slug):
    all_news = News.objects.all()
    news = all_news[::-1]
    short = []
    for item in news:
        if item.NShort != "":
            short.append(item.NShort)
    news_short = short[:5]

    nav_detail = NavBar.objects.get(NAVSlug=slug)
    nav = NavBar.objects.all()
    nav_new = check_nav_has_son(nav)
    motion = MotionImage.objects.all()
    smotion = MotionImage.objects.filter(MIRelation=nav_detail)
    contact = Contact.objects.all().first()
    context = {'nav_detail': nav_detail, 'nav': nav, 'contact': contact, 'nav_new': nav_new, 'motion': motion, 'news_short': news_short, 'smotion': smotion}
    return render(request, 'structure/nav_detail.html', context)


def news_list_Page(request):
    news = News.objects.all()
    num = 1
    nav = NavBar.objects.all()
    nav_new = check_nav_has_son(nav)
    news_list = news[::-1]
    contact = Contact.objects.all().first()
    context = {'nav': nav, 'nav_new': nav_new, 'num': num, 'news_list': news_list, 'contact': contact}
    return render(request, 'structure/News_List.html', context)


def news_detail_page(request, id):
    nav = NavBar.objects.all()
    nav_new = check_nav_has_son(nav)
    num = 1
    news = News.objects.get(id=id)
    contact = Contact.objects.all().first()
    context = {'nav': nav, 'nav_new': nav_new, 'num': num, 'news': news, 'contact': contact}
    return render(request, 'structure/News_Details.html', context)


def advert_page(request, id):
    nav = NavBar.objects.all()
    nav_new = check_nav_has_son(nav)
    num = 2
    advert = Adds.objects.get(id=id)
    contact = Contact.objects.all().first()
    context = {'nav': nav, 'nav_new': nav_new, 'num': num, 'advert': advert, 'contact': contact}
    return render(request, 'structure/News_Details.html', context)


def ads_list_page(request):
    ads = Adds.objects.all()
    num = 2
    nav = NavBar.objects.all()
    nav_new = check_nav_has_son(nav)
    ads_list = ads[::-1]
    contact = Contact.objects.all().first()
    context = {'nav': nav, 'nav_new': nav_new, 'num': num, 'ads_list': ads_list, 'contact': contact}
    return render(request, 'structure/News_List.html', context)


def show_gallery(request):
    nav = NavBar.objects.all()
    nav_new = check_nav_has_son(nav)
    images = Photo.objects.all()
    contact = Contact.objects.all().first()
    context = {'nav': nav, 'nav_new': nav_new, 'images': images, 'contact': contact}
    return render(request, 'structure/Photo_Gallary.html', context)
