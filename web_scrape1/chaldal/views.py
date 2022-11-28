from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from .models import chaldal

# Create your views here

def input(request):
    # return render(request, 'chaldal/input.html')
    # request.method == "POST"
    # url = request.POST.get('landPage')
    # x1 = request.POST.get('xpath1')
    # x2 = request.POST.get('xpath2')
    # totalPro = request.POST.get('totalPro')
    #
    # options = Options()
    # options.headless = True
    # options.add_argument("--window-size=1920,1200")
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get(url)
    # titleList = []
    # for i in range(1,int(totalPro)+1):
    #     title = driver.find_element(by=By.XPATH,value=x1+"["+str(i)+"]"+x2)
    #     titleList.append(title.text)
    #     product = chaldal(title=title.text)
    #     product.save()
    #
    # print(titleList)
    # driver.quit()
    # return redirect('/chaldal/output/')

    if (request.method == "POST"):

        url = request.POST.get('landPage')
        x1 = request.POST.get('xpath1')
        x2 = request.POST.get('xpath2')
        totalPro = request.POST.get('totalPro')

        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        titleList = []
        for i in range(1,int(totalPro)+1):
            title = driver.find_element(by=By.XPATH,value=x1+"["+str(i)+"]"+x2)
            titleList.append(title.text)
            product = chaldal(title=title.text)
            product.save()

        print(titleList)
        driver.quit()

        return redirect('/chaldal/output/')
    else:
        return HttpResponse("This is not POST METHOD")


def output(request):
    allData = chaldal.objects.all()
    all_data_dict = {'data':allData}
    return render(request,'chaldal/output.html', context=all_data_dict)
