from django.shortcuts import render
from django.http import HttpRequest, QueryDict, HttpResponse
from .models import testData, users
from .forms import formSelectPlus, formBuildUser, formBuilderComment, formBuilderPositions


def testPage(request):
    if request.method == 'GET':
        if 'widget' in request.GET:  # усли приходит имя виджета тогда нужно его перерисовать, возвращаем только HTML
            return updateWidget(request,formSelectPlus)
        else:
            form = formSelectPlus()
            return render(request, 'test.html', {'form': form})

def buildUserPage(request: HttpRequest):
    if request.method == "GET":
        if 'widget' in request.GET:  # если приходит имя виджета тогда нужно его перерисовать, возвращаем только HTML
            return updateWidget(request,formBuildUser)
        else:
            return castResponse(request, formBuildUser, 'builderUser.html')


def builderCommentPage(request):
    if request.method == "GET":
        if 'widget' in request.GET:  
            return updateWidget(request,formBuilderComment)
        else:
            return castResponse(request, formBuilderComment, 'builderComment.html')


def builderPosition(request):
    if request.method == "GET":
        if 'widget' in request.GET: 
            return updateWidget(request,formBuilderPositions)
        else:
            return castResponse(request, formBuilderPositions, 'builderPositions.html')


def updateWidget(request,base_form):
            name_widget = request.GET['widget']
            # какую форму рендерить ?
            form = base_form()
            field = form.fields[name_widget].widget
            # первый аргумент имя формы, соответсвует имени формы которую перерисовываем
            # второй аргумент порядковый номер списка который будет выбран по умолчанию
            if 'id' in request.GET:
                rnd = field.render(name_widget, request.GET['id'])
            else:
                rnd = field.render(name_widget, '0')
            return HttpResponse(rnd)


def castResponse(request, base_form, template):
    # Имеем 4 варианта формы add, edit, delete
    # add при первом вхождении пуста. При вхождении с данными,
    # создаём элемент и возвращаем только его
    # edit первое вхождение с данными, проверяем по ID элемента
    #  есть ли изменения по сравнению с содержимым в БД.
    # Если есть возвращаем изменённый элемент
    # delete -
    last_elemet_path = request.path.split('/')[-1]
    model_form = base_form.Meta.model
    if last_elemet_path == 'add':
        if all(elementForm in request.GET for elementForm in base_form.Meta.fields):
            form = base_form(data=request.GET)
            if form.is_valid:
                new_row_db = form.save()
                return HttpResponse('id='+str(new_row_db.id))
        else:
            form = base_form()
    elif last_elemet_path == 'edit' and model_form.objects.filter(id__exact=request.GET['id']).exists():
        serch_element = model_form.objects.get(id=request.GET['id'])
        if all(elementForm in request.GET for elementForm in base_form.Meta.fields):  # Заполненная форма
            form = base_form(instance=serch_element, data=request.GET)
            if form.has_changed() and form.is_valid():
                form.save()
                return HttpResponse('id='+request.GET['id'])
        else:  # Первый запрос или пустая форма
            form = base_form(instance=serch_element)

    elif last_elemet_path == 'delete' and request.GET['id']:
        serch_element = model_form.objects.get(id=request.GET['id'])
        serch_element.delete()
        return HttpResponse('id='+request.GET['id'])
    # ###########
    if form:
        return render(request, template, {'form_builder': form, })
