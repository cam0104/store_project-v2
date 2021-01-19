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
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "id_venta" },
            { "data": "id_cliente" },
            { "data": "id_empleado" },
            { "data": "fecha_venta" },
            { "data": "forma_pago" },
            { "data": "precio_total" },
            { "data": "botones" },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var botones = '<a href="editar_categoria/' + row.id_categoria + '/" class="btn btn-warning btn-circle"><i class="fas fa-edit"></i></a>';
                    botones += '<a href="eliminar_categoria/' + row.id_categoria + '/" class="btn btn-danger btn-circle"><i class="fas fa-trash"></i></a>'
                    return botones
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});