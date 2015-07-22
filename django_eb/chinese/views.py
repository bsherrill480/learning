from django_eb.common.default_render import render

def chineseVocab(request):
    return render(request, 'django_eb/vocab.html')