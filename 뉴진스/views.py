from django.shortcuts import render

# Create your views here.
def show_혜인(request):
    context ={
        'name' : '혜인',
        'img_src' : 'https://i.namu.wiki/i/z1smLIpL4Q6pwe3ecFjJIHkYfkJ10ZzP84HW_SLDKbZE5wLl401WPvDnS-VSOou4BHKjqvDDksUMwZoqy4ZCDaoTW2U0iv298ae8prCre3lRYyAxfiXFdrLpxI-aUTzusMhzVuikPWnucXnBuprIAQ.webp',
    }
    return render(request, '뉴진스/혜인.html', context=context)

def show_해린(request):
    context ={
        'name' : '해린',
        'img_src' : 'https://a-static.besthdwallpaper.com/newjeans-haerin-omg-mv-shoot-wallpaper-2048x1536-108329_26.jpg',
    }
    return render(request, '뉴진스/해린.html', context=context)