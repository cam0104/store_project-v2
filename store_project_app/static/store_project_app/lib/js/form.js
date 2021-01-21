var tblProductos;
var ventas = {
    items: {
        id_cliente: '',
        id_empleado: '',
        fecha_venta: '',
        forma_pago: '',
        precio_total: 0.00,
        productos: []
    },

    calcular_factura: function () {
        var total = 0.00;
        $.each(this.items.productos, function (pos, dict) {
            dict.subtotal = dict.cantidad * parseFloat(dict.precio)
            total += dict.subtotal;
        });
        this.items.precio_total = total;
        $('input[name="precio_total"]').val(this.items.precio_total);
    },

    add: function (item) {
        this.items.productos.push(item);
        this.list();
    },

    list: function () {

        this.calcular_factura();

        tblProductos = $('#dataTable').DataTable({
            responsive: true,
            autoWidth: false,
            data: this.items.productos,
            destroy: true,
            deferRender: true,

            columns: [
                { "data": "id_producto" },
                { "data": "nombre" },
                { "data": "categoria.nombre" },
                { "data": "precio" },
                { "data": "cantidad" },
                { "data": "subtotal" },
                { "data": "botones" },
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="eliminar" class="btn btn-danger btn-circle"><i class="fas fa-trash"></i></a>'
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cantidad + '">';
                    }
                },
                {
                    targets: [-4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                }
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {
                $(row).find('input[name="cantidad"]').TouchSpin({
                    min: 1,
                    initval: 1000000,
                    step: 1
                });

            },
            initComplete: function (settings, json) {
            }
        });
    },
};

function alerta(titulo, contenido, callback) {
    $.confirm({
        theme: 'material',
        title: titulo,
        icon: 'fa fa-info',
        content: contenido,
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
                    callback();
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
};

$(function () {

    $("#search").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'autocomplete',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (data) {
                alert("Error");
            }).always(function (jqXHR, textStatus, errorThrown) {

            })
        },
        delay: 500,
        minLenght: 3,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cantidad = 1
            ui.item.subtotal = 0
            console.log(ventas.items);
            ventas.add(ui.item);
            $(this).val('');
        }
    });

    $(".btnCancelarVenta").on('click', function () {
        if (ventas.items.productos == 0) return false;
        alerta('Notificación', '¿Está seguro de cancelar la venta?', function () {
            ventas.items.productos = [];
            ventas.list();
        });
    });

    $("#dataTable tbody").on('click', 'a[rel="eliminar"]', function () {
        var tr = tblProductos.cell($(this).closest('td, li')).index();
        alerta('Notificación', '¿Está seguro de eliminar este producto de la venta?', function () {
            ventas.items.productos.splice(tr.row, 1);
            ventas.list();
            console.log(ventas.list);
        });

    }).on('change', 'input[name="cantidad"]', function () {

        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblProductos.cell($(this).closest('td, li')).index();
        //console.log(tr);
        var data = tblProductos.row(tr.row).node();
        ventas.items.productos[tr.row].cantidad = cant;
        ventas.calcular_factura();
        $('td:eq(5)', tblProductos.row(tr.row).node()).html('$' + ventas.items.productos[tr.row].subtotal);
        console.log(ventas.items.productos[tr.row].subtotal);

    })

    //Registrar venta
    $('form').on('submit', function (e) {

        e.preventDefault();

        ventas.items.id_cliente = $('select[name="id_empleado"]').val();
        ventas.items.id_empleado = $('select[name="id_empleado"]').val();
        ventas.items.fecha_venta = $('input[name="fecha_venta"]').val();
        ventas.items.forma_pago = $('select[name="forma_pago"]').val();
        ventas.items.precio_total = $('input[name="precio_total"]').val();
        console.log(ventas.items)

        var parametros = new FormData();
        console.log(parametros);
        parametros.append('action', $('input[name="action"]').val());
        console.log($('input[name="action"]').val());
        parametros.append('ventas', JSON.stringify(ventas.items));
        console.log(JSON.stringify(ventas.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Esta seguro de realizar la siguiente acción?',parametros, function () {
            location.href = 'crear_venta';
        });
    });
});

function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
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
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        console.log(data);
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                        console.log(textStatus + ': ' + errorThrown);
                        var err = new Error();
                        console.log(err.stack)
                    }).always(function (data) {

                    });
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

