$(function () {

    $('#dataTable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action' : 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "id_categoria"},
            { "data": "nombre"},
            { "data": "descripcion"},
            { "data": "botones"},
        ],
        columnDefs: [
            {
                targets: [2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return data;
                }
            },
        ],
        initComplete: function(settings, json) {
        
          }
        });

});