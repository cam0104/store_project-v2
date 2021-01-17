var tblProductos;
var ventas = {
    items: {
        id_venta: '',
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
        //console.log(this.items.precio_total);
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
}

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

    })

    //Registrar venta

    $('form').on('submit', function (e) {
        e.preventDefault();

        ventas.items.id_cliente = $('input[name="id_cliente"]').val();
        ventas.items.fecha_venta = $('input[name="fecha_venta"]').val();
        ventas.items.forma_pago = $('input[name="forma_pago"]').val();
        ventas.items.precio_total = $('input[name="precio_total"]').val();

        

        var parametros = new FormData();
        parametros.append('action', $('input[name="action"]').val());
        submit(window.location.pathname, parametros, function(){
            location.href = "{% url 'Categoria' %}";

        });
    });



});
