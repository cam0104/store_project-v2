function myFunction() {
    $.ajax({
        url: "{% url 'Categoria' %}",
        type: 'POST',
        data: { id: 1 },
        dataType: 'json '
    }).done(function (data) {
        console.log(data)
    }).fail(function (data) {
        alert("Error");
    }).always(function (jqXHR, textStatus, errorThrown) {
        alert("Completado");
    })
}

function mensaje_error(obj) {
    $.each(obj, function (key, valor) {
        console.log(key);
        console.log(valor);
    });
}


// $('form').on('submit', function (e) {
//     e.preventDefault();
//     var parametros = $(this).serializeArray();
//     //console.log(parametros);
//     $.ajax({
//         url: window.location.pathname,
//         type: 'POST',
//         data: parametros,
//         dataType: 'json '
//     }).done(function (data) {
//         if (!data.hasOwnProperty('error')) {
//             location.href = "{% url 'Categoria' %}"
//             return false;
//         }
//         mensaje_error(data.error);
//     }).fail(function (data) {
//         alert("Error");
//     }).always(function (jqXHR, textStatus, errorThrown) {
//         alert("Completado");
//     })

// })

function submit(url,parametros,callback){

    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: '¿Estás seguro de realizar la siguiente acción',
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url,
                        type: 'POST',
                        data: parametros,
                        dataType: 'json '
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        mensaje_error(data.error);
                    }).fail(function (jqXHR,textStatus,errorThrown) {
                        alert(textStatus + ':' + errorThrown);
                    }).always(function (jqXHR, textStatus, errorThrown) {
                        
                    })
                    
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    
                }
            },
        }
    })
}





