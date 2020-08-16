
/* Closemodal add product by default */
$('#modal_add').hide();

/* Open modal add */
$('.reports').on('click', '.button_add', function (e) {
    let id = $(this).parent().attr("id");
    let name = $(this).parent().attr("data-name");
    $("#id_product").val(id);
    $("#name_product").text(name);
    $('#modal_add').show();
});

/* Close modal add */
$('#btn_modal_add--close').click(function () {
    $('#modal_add').hide();
});

/* Closemodal order cart by default */
$('#modal_products').hide();


/* Open modal order cart */
$('#open_order').click(function () {
    $('#modal_products').show();
});

/* Close modal order cart */
$('#close_order').click(function () {
    $('#modal_products').hide();
});

/* charge products to cart */
$('#charge_product').click(function () {
    let id_product = $("#id_product").val();
    let name_product = $("#name_product").text();
    let cant_product = $("#cant_product").val();

    //Validation product
    let tr_product = $('#tbody_products').children();
    let exist = false;
    for (let index = 0; index < tr_product.length; index++) {
        let my_id = tr_product[index].id
        if (my_id == id_product) {
            exist = true;
            alert("Este producto ya fue agregado, por favor verifique su carrito y cambie la cantidad si es lo que desea.")
        }
    }
    if (exist == false) {
        $('#tbody_products').append(
            "<tr id='" + id_product + "'> \
                <td style='width:30%' > <input class='input input_table' type='number' value='" + cant_product + "' ></td>\
                <td style='width:60%'>" + name_product + "</td>\
                <td style='width:10%'> <button class='button button_remove_product' style='width:80px'> Quitar </button> </td>\
            </tr>\
            "
        );
    }

    $('#modal_add').hide();
});

/* Remove a product from cart */
$('#tbody_products').on('click', '.button_remove_product', function (e) {
    $(this).parent().parent().remove();

});

/* Remove all products from cart */
$('#clean_cart').click(function () {
    $('#tbody_products').children().remove();
});