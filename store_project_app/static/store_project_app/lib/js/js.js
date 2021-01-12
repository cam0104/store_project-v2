// function myFunction() {
//     $.ajax({
//         url: "{% url 'Categoria' %}",
//         type: 'POST',
//         data: { id: 1 },
//         dataType: 'json '
//     }).done(function (data) {
//         console.log(data)
//     }).fail(function (data) {
//         alert("Error");
//     }).always(function (jqXHR, textStatus, errorThrown) {
//         alert("Completado");
//     })
// }

function mensaje_error(obj){
    $.each(obj, function(key,valor){
        console.log(key);
        console.log(valor);
    });
}



