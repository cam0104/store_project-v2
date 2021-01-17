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
        console.log(this.items.precio_total);
        //$('input[name="precio_total"]').val(this.items.total);
    },

    add: function (item) {
        this.items.productos.push(item);
        this.list();
    },

    list: function () {

        this.calcular_factura();

        $('#dataTable').DataTable({
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
                        return '<a rel="remove" class="btn btn-danger btn-circle"><i class="fas fa-trash"></i></a>'
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
                        return '<input type="text" name="cantidad" class="form-control form-control-sm" autocomplete="off" value="' + row.cantidad + '">';
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
                    step:1
                });
                console.log(row);
                console.log(data);
            },
            initComplete: function (settings, json) {
            }
        });
    },
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

    $("#dataTable tbody").on('change keyup', 'input[name="cantidad"]', function () {
        console.clear();
        var cant = parseInt($(this).val());
        console.log(cant);
    })
});
