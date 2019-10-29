from django.core import serializers
from django.http import HttpResponse
from django.template import loader

from .models import Text, Image


def index(request):
    text_menu = Text.objects.filter(language='ES', page='Menu')
    text_page = Text.objects.filter(language='ES', page='Page1')
    last_image = Image.objects.last()
    # return HttpResponse("<img src=\"/media/{}\">".format(last_image.imagefile))

    menu_text = {text.name: text.text for (text) in text_menu}
    page_text = {text.name: text.text for (text) in text_page}
    # {key: value for (key, value) in dictonary.items()}

    # page_text_json = serializers.serialize('json', page_text)
    print(page_text)

    template = loader.get_template('page1.html')
    context = {
        'menu_text': menu_text,
        'page_text': page_text,
    }

    return HttpResponse(template.render(context, request))


def page1(request):
    text_menu = Text.objects.filter(language='EN', page='Menu')
    text_page = Text.objects.filter(language='EN', page='Page1')
    last_image = Image.objects.last()
    # return HttpResponse("<img src=\"/media/{}\">".format(last_image.imagefile))

    menu_text = {text.name: text.text for (text) in text_menu}
    page_text = {text.name: text.text for (text) in text_page}
    # {key: value for (key, value) in dictonary.items()}

    # page_text_json = serializers.serialize('json', page_text)
    print(page_text)

    template = loader.get_template('page1.html')
    context = {
        'menu_text': menu_text,
        'page_text': page_text,
    }

    return HttpResponse(template.render(context, request))


#
# def showimage(request):
#     lastimage = Image.objects.last()
#
#     imagefile = lastimage.imagefile
#
#     form = ImageForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#
#     context = {'imagefile': imagefile,
#                'form': form
#                }
#
#     return render(request, 'Blog/images.html', context)
