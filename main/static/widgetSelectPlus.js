function newPlusWindow(url, nameSelector) {
    var h = 500,
        w = 500,
        splitURL = url.split('/'),
        action = splitURL[splitURL.length - 1],
        select_field = document.querySelector('#id_' + nameSelector),
        attr='scrollbars=1,height=' + Math.min(h, screen.availHeight) + ',width=' + Math.min(w, screen.availWidth) + ',left=' + Math.max(0, (screen.availWidth - w) / 2) + ',top=' + Math.max(0, (screen.availHeight - h) / 2);
    if (select_field?.value) {
        var GETQuery = url + '?' + 'id' + '=' + select_field.value
    }
    switch (action) {
        case 'edit':
            if (!select_field?.value) { alert("Выберите элемент для редактирования") }
            else{
                chaildWindow = window.open(GETQuery, '',attr );
                
            }
            break;
        case 'delete':
            if (!select_field?.value) { alert("Выберите элемент для удаления") }
            else {
                if (confirm('Удалить элемент ?')) {
                    var x = new XMLHttpRequest();
                    x.open("GET", GETQuery, true);
                    x.onload = function () {
                        updateField(select_field.id)
                    }
                    x.send(null);
                }
            }
            break;
        case 'add':
            chaildWindow = window.open(url, '', attr);
            break;
    }
    chaildWindow.onload= function(){  chaildWindow.id_parent_field=select_field.id }
   chaildWindow?.focus()
    
}
function updateField(id_field, id_select=null)
{
    
   
    var field=document.querySelector('#'+id_field)
    if (field)
    {
        if (id_select==null)
        {
            var GETQuery = '?' + 'widget' + '=' + field.name
        }
        else 
        {
            var GETQuery = '?' + 'widget' + '=' + field.name+'&'+'id='+id_select
        }
        var x = new XMLHttpRequest();
        x.open("GET", GETQuery, true);
        x.onload = function () {
            field.innerHTML=x.responseText
            }
        x.send(null);
    }
}