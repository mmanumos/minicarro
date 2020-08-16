/**
 * Get django token
 * 
 */

function getCookie(name) {

    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    //RETORNANDO EL TOKEN
    return cookieValue;

}//end function getCookie


//get token
let csrftoken = getCookie('csrftoken');




/* Closemodal add product by default */
$('#modal_add').hide();

/* Open modal add */
$('.reports').on('click', '.button_add', function (e) {
    let id = $(this).parent().attr("data-id_product");
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

    // Quantity validation
    if (cant_product != "") {
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
                <td style='width:30%' > <input class='input input_table' type='number' id='" + id_product + "-p' value='" + cant_product + "' ></td>\
                <td style='width:60%'>" + name_product + "</td>\
                <td style='width:10%'> <button class='button button_remove_product' style='width:80px'> Quitar </button> </td>\
            </tr>\
            "
            );
        }
        $("#cant_product").val("");
        $('#modal_add').hide();
    }
    else {
        alert("Porfavor digite la cantidad deseada del producto");
    }
});

/* Remove a product from cart */
$('#tbody_products').on('click', '.button_remove_product', function (e) {
    $(this).parent().parent().remove();

});

/* Remove all products from cart */
$('#clean_cart').click(function () {
    $('#tbody_products').children().remove();
});

/* Confirm order */
$('#confirm_order').click(function () {
    let tr_product = $('#tbody_products').children();
    list_order = []
    for (let index = 0; index < tr_product.length; index++) {
        let id_product = tr_product[index].id;
        let cant_product = document.getElementById(id_product + "-p").value;
        list_order.push([id_product, cant_product]);
    }

    //Final data for post
    let order = {
        "list_order": list_order,
    };

    $.ajax({
        type: "POST",
        url: "http://localhost:8000/create_order/",
        data: JSON.stringify(order),
        ContentType: 'Application/json',
        headers: { "X-CSRFToken": csrftoken },
        success: function (result) {
            if (result.status == "success") {
                alert('La orden no ' + result.order_id + " se ha creado exitosamente. Puede verla en la sección mis ordenes de su perfil");
                location.href = "/home/";
            }
            else {
                console.log(result);
            }
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });

});


/* Pay order */
$('#pay_order').click(function () {
    let id_order = $(this).attr("data-id");
    let order = { "id": id_order }
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/pay_order/",
        data: JSON.stringify(order),
        ContentType: 'Application/json',
        headers: { "X-CSRFToken": csrftoken },
        success: function (result) {
            if (result.status == "success") {
                alert('La orden no. ' + result.order_id + " se ha pagado exitosamente.");
                location.href = "/orders/";
            }
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});