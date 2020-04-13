from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from django.utils.safestring import mark_safe
from django.utils.html import escape
def index(request):
    return render(request,'main/index.html')

def detail_img(request):

    baseUrl = 'https://gramtower.com/profile/'
    plusUrl = request.GET.get('account')
    plusUrl = str(plusUrl)
    url = baseUrl + quote_plus(plusUrl)

    driver = webdriver.Firefox(executable_path='/Users/kimbyeonguk/Desktop/practice/django/instaPrj/geckodriver')
    driver.get(url)

    pageDown = 30
    while pageDown:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        pageDown -= 1

    html = driver.page_source
    soup = BeautifulSoup(html)

    instaImg = soup.select('div.grid-item>div>a')
    instaText = soup.select('div.grid-item>div.p-4>div.break-words')

    imgSrcList = []
    textList = []
    posts = {}

    for i in instaImg:
        imgSrcList.append(i.img['src'])

    for i in instaText:
        textList.append(i)

    for i in range(len(imgSrcList)):
        img = imgSrcList[i]
        text = textList[i]
        posts.update({img:text})



    driver.close()

    return render(request,'main/detail_img.html',{'posts':posts})
