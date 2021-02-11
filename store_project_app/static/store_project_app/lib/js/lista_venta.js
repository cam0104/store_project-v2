function format(d) {
    console.log(d)
    var html = '<table class="table">';
    html += '<thead';
    html += '<tr><th scope="col">Producto</th>';
    html += '<th scope="col">Categoria</th>';
    html += '<th scope="col">Cantidad</th>';
    html += '<th scope="col">Subtotal</th></tr>';
    html += '</thead>';
    html += '<tbody></tbody>';
    return html
}

var tblVenta;

$(function () {
    var tblVenta = $('#dataTable').DataTable({
        responsive: true,
        autoWidth: false,
        language: {
            url: '/static/store_project_app/vendor/datatables/spanish.txt'  
        },
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
            { "data": "cliente.nombre" },
            { "data": "creacion_user" },
            { "data": "fecha_venta" },
            { "data": "forma_pago.nombre" },
            { "data": "precio_total" },
            { "data": "botones" },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var botones = '<a rel="detalle" class="btn btn-success btn-circle"><i class="fas fa-search"></i></a> ';
                    if (window.location.pathname == '/ventas'){
                        botones += '<a href="anular_venta/' + row.id_venta + '/" class="btn btn-danger btn-circle"><i class="fas fa-times"></i></a> '
                    }
                    botones += '<a href="/factura_venta/' + row.id_venta + '/" target="_blank" class="btn btn-info btn-circle"><i class="fas fa-file-pdf"></i></a> '
                    return botones
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (data == "Contado") {
                        return '<span class="badge badge-success">' + data + '</span>'
                    }
                    return '<span class="badge badge-danger">' + data + '</span>'
                    
                }
            },

            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$' + parseFloat(data).toFixed(0);
                }, 
            },
        ],
        initComplete: function (settings, json) {
        }

    });

    $("#dataTable tbody").on('click', 'a[rel="detalle"]', function () {
        var tr = tblVenta.cell($(this).closest('td, li')).index();
        var data = tblVenta.row(tr.row).data();
        console.log(data.id_venta);
        console.log(data);

        $('#tblDetalles').DataTable({
            responsive: true,
            autoWidth: false,
            language: {
                url: '/static/store_project_app/vendor/datatables/spanish.txt'  
            },
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'searchdata_detalle',
                    'id': data.id_venta,
                },
                dataSrc: ""
            },
            columns: [

                { "data": "producto.nombre" },
                { "data": "producto.categoria.nombre" },
                { "data": "producto.precio" },
                { "data": "cantidad" },
                { "data": "subtotal" },
            ],
            columnDefs: [
                {
                    targets: [-1, -3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    },

                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return data;
                    }
                },
            ],
            initComplete: function (settings, json) {
            }

        });

        $('#ventaModal').modal('show');


    })




});