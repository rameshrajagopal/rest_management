$(document).ready(function() {
    var counter = 0;
    var gtotal  = 0;
    $("#id_form-"+ counter + "-item").focus();
    $("#id_form-"+ counter + "-quantity").val(0);
    $(".bill_item").change(function() {
        var item = $("#id_form-" + counter + "-item").val();
        var quantity = $("#id_form-"+ counter + "-quantity").val();
        if ((item != NaN) && (quantity > 0)) {
            $.get("/billing/get_price/", {item: item}, function(data) {
                $("#id_form-"+ counter + "-price").val(data);
                $("#id_form-"+ counter + "-total").prop("readonly", false);
                $("#id_form-"+ counter + "-total").val(quantity * data); 
                $("#id_form-"+ counter + "-total").prop("readonly", true);
                gtotal = gtotal + (quantity * data);
                $("#gtotal").val(gtotal);
                $("#add_more").focus();
            });
        } else {
          //  alert(item + " " + quantity);
        }
    });
    $("#add_more").click(function() {
        var newElement = $("div.bill_items:last").clone(true);
        var total = $('#id_form-TOTAL_FORMS').val();
        newElement.find('div').each(function() {
            var id = 'bill-' + total;
            $(this).attr({'id':id}).val('').removeAttr('checked');
            });
        newElement.find(':input').each(function() {
             var name = $(this).attr('name').replace('-' + (total-1) + '-',
                 '-' + total + '-');
             var id = 'id_' + name;
             $(this).attr({'name': name, 'id':
              id, 'value': 0}).val('').removeAttr('checked');
             });
        
        newElement.find('label').each(function() {
            var newFor =
            $(this).attr('for').replace('-' +
                (total-1) + '-','-' + total + '-');
            $(this).attr('for', newFor);
            });
        counter = total;
        total++;
        $('#id_form-TOTAL_FORMS').val(total);
        $("div.bill_items:last").append(newElement);
        $('#id_form-'+ counter +'-srno').val(total);
        $('#id_form-'+ counter +'-quantity').val(0);
        $('#id_form-'+ counter +'-price').val(0);
        $('#id_form-'+ counter +'-total').val(0);
        $('#id_form-'+ counter +'-item').val(16);
        $('#id_form-'+ counter +'-item').focus();
     });
    $('#suggestion').keyup(function() {
      var query;
      query = $(this).val();
      $.get('/billing/suggest_food/', {suggestion: query},
                function(data) {
                $('#fooditems').html(data)
                });
    });
    var g_counter = 0;
    var g_gtotal  = 0;
    $(".goods_item").change(function() {
        var item = $("#id_form-" + g_counter + "-item").val();
        var quantity = $("#id_form-"+ g_counter + "-quantity").val();
        var total = $("#id_form-"+ g_counter +"-total").val();
        if ((item != NaN) && (quantity > 0) && (total > 0)) {
                $('#id_form-'+ g_counter +'-price').val(parseInt(total, 10));
                g_gtotal = g_gtotal + parseInt(total, 10);
                $("#goods_gtotal").val(g_gtotal);
                $("#goods_add_more").focus();
        } else {
          //  alert(item + " " + quantity);
        }
    });
    $("#goods_add_more").click(function() {
        var newElement = $("div.goods_items:last").clone(true);
        var total = $('#id_form-TOTAL_FORMS').val();
        newElement.find('div').each(function() {
            var id = 'goods-' + total;
            $(this).attr({'id':id}).val('').removeAttr('checked');
            });
        newElement.find(':input').each(function() {
             var name = $(this).attr('name').replace('-' + (total-1) + '-',
                 '-' + total + '-');
             var id = 'id_' + name;
             $(this).attr({'name': name, 'id':
              id, 'value': 0}).val('').removeAttr('checked');
             });
        
        newElement.find('label').each(function() {
            var newFor =
            $(this).attr('for').replace('-' +
                (total-1) + '-','-' + total + '-');
            $(this).attr('for', newFor);
            });
        g_counter = total;
        total++;
        $('#id_form-TOTAL_FORMS').val(total);
        $("div.goods_items:last").append(newElement);
        $('#id_form-'+ g_counter +'-srno').val(total);
        $('#id_form-'+ g_counter +'-quantity').val(0);
        $('#id_form-'+ g_counter +'-total').val(0);
        $('#id_form-'+ g_counter +'-item').val(1);
        $('#id_form-'+ g_counter +'-item').focus();
     });
});
