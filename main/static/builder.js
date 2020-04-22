function onClickSave()//
    {

        //1. ищем форму
        //2. перебираем элементы формы и из заполненых формируем GET запрос
        //3. ждём получения нового ID или ID изменённого 
        //4. если id пришёл то вызываем функцию обновления field родительского окна
        //5. в аргументы передаём имя field и id элемента который обновляли
        form = document.querySelector("#builder_form")
        let GETQuery = '?', formOK = true

        for (var i = 0; i < form.elements.length; i++) {
            if (form.elements[i].value) {
                GETQuery = GETQuery + form.elements[i].name + '=' + form.elements[i].value + '&'
            }
            else {
                if (form.elements[i].type != 'button') {
                    alert('Элемент: ' + form.elements[i].name + ' не заполнен')
                    formOK = false
                    break;
                }
            }
        }
        if (formOK) {
            var x = new XMLHttpRequest();
            x.open("GET", GETQuery, true);
            x.onload = function () {
                response = x.responseText.split('=')
                if (response[0] == 'id') {
                    window.opener.updateField(self.id_parent_field, response[1])
                }
                window.close()
            }
            x.send(null);
        }

    }
