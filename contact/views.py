
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_page(request):
    context = {"name":"MAHDI" , "fullname":"MAHDI GHEZAVATI" ,"city":"GORGAN","prvo":"GOLESTAN","MY_number":"+98-936-833-5378","MY_email":"GorganRoyal@gmail.com", "Languages":"HTML / CSS / PYTHON ","Database":"MySQL","webframework":"DJANGO","telegramID":"@IMEHDIWI" , "xID":"@Meyishonam" , "living_01":"iran", "living_02": "Gorgan", "living_03" : "everywhere","link_telegram":"https://t.me/IMehtiwI","link_x":"https://x.com/Meyishonam?s=09","link_github":"https://github.com/MahdiGhezavati"}
    return render(request , "contact/contact.html" , context)