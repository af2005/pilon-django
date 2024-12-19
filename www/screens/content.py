from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

LOREM_IPSUM = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eget ornare metus. Phasellus molestie
                    viverra euismod. Sed ultrices dolor sed ornare iaculis. Ut ut gravida nulla. Proin urna erat, dictum
                    eu turpis ac, aliquam vulputate erat. Phasellus porttitor ut nisl et cursus. Nam at laoreet leo, id
                    rhoncus erat. Integer lacinia est quis est dictum, non porta elit porttitor. Sed laoreet lectus non
                    magna eleifend lacinia.

                    Vivamus tincidunt, magna eget maximus consectetur, augue lacus fringilla arcu, eu commodo tellus leo
                    sit amet lectus. Maecenas nec lacus lobortis, tincidunt arcu ac, imperdiet eros. Suspendisse
                    suscipit justo nisi, eu aliquet nulla pharetra vel. Etiam volutpat rutrum turpis eu malesuada.
                    Curabitur vitae est lacinia, feugiat sapien quis, accumsan neque. Vestibulum suscipit lacinia
                    varius. Vivamus sapien nibh, imperdiet non sodales et, tempus at enim. Sed aliquet volutpat nunc at
                    condimentum.

                    Vivamus laoreet nec metus vitae aliquam. Nam vel fringilla turpis. Proin sit amet volutpat est.
                    Curabitur sit amet dui eleifend, ultricies sapien ut, eleifend nibh. Pellentesque ac pulvinar lacus.
                    Aenean egestas lacus quis est egestas, consequat commodo nisl convallis. Vestibulum imperdiet id
                    magna eget tincidunt. Proin nec lorem non ex ultricies bibendum. Cras vitae ullamcorper lorem. Proin
                    blandit gravida turpis sed lacinia. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer
                    congue purus varius nulla tincidunt, id tempus purus congue. Lorem ipsum dolor sit amet, consectetur
                    adipiscing elit.

                    Ut bibendum vel dolor a ornare. Integer purus orci, eleifend eget interdum nec, feugiat ut risus.
                    Duis vitae lectus non arcu fringilla placerat. Nullam id tincidunt arcu. Duis et elit porta,
                    sollicitudin mi non, placerat est. Mauris vehicula erat non eros condimentum, in gravida lectus
                    porttitor. Cras ut quam vitae dolor porttitor porttitor. Aliquam lorem massa, consectetur nec lectus
                    vitae, dapibus bibendum tellus. Nam bibendum urna nisl, mollis vestibulum nisi vehicula sed. Aliquam
                    hendrerit, orci eu maximus eleifend, diam sapien maximus nisi, nec rhoncus ipsum lorem quis arcu.
                    Aenean in risus congue ipsum finibus efficitur non et metus. Praesent quis lorem pulvinar, gravida
                    lacus nec, pretium nisi. Mauris id lacus sed tortor vestibulum vulputate egestas sed risus.

                    Fusce eget fringilla neque, vel luctus urna. Vivamus eget dui risus. Phasellus et sodales purus.
                    Nullam sed consectetur tellus, eu tincidunt odio. Morbi efficitur ligula eu aliquet commodo.
                    Interdum et malesuada fames ac ante ipsum primis in faucibus. In justo magna, aliquam eget dapibus
                    non, rutrum non purus. Mauris purus lorem, auctor nec laoreet id, fermentum vitae turpis. Curabitur
                    sit amet finibus neque. Duis dignissim nisi quis ligula lacinia cursus. Proin aliquet lacus enim, at
                    euismod erat posuere vel. Fusce feugiat justo a aliquam pellentesque. Sed ut erat ac urna finibus
                    auctor a eu eros. Proin nec velit non arcu consequat pretium.
'''

def view_dashboard(request):
    template = loader.get_template('www/default.html')
    context = {
        'window_title': "Dashboard",
        'page_title': "Today",
        'sidebar': True,
        'content': LOREM_IPSUM
    }
    return HttpResponse(template.render(context, request))


def view_project_homepage(request):
    return HttpResponse("Project Homepage")


def wiki_page(request):
    return HttpResponse("Wiki Page")


def journal_page(request):
    return HttpResponse("Journal Page")