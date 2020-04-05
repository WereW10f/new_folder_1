from django import forms
#виджет добавляет 3 кнопки. Кнопака на ссылку с формой создания нового элемента
#кнопка редактирования 
#кнопка удаления элемента
class selectPlus(forms.Select):
    def __init__(self, attrs=None, choices=(),baseURL=None):
        super().__init__(attrs)
        # choices can be any iterable, but we may need to render this widget
        # multiple times. Thus, collapse it into a list so it can be consumed
        # more than once.
        self.choices = list(choices)
        self.baseURL=baseURL

    template_name = 'selectPlus.html'
    #template_name = 'django/forms/widgets/selectPlus.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['baseURL']=self.baseURL
        if self.allow_multiple_selected:
            context['widget']['attrs']['multiple'] = True
        return context