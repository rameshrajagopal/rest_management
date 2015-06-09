$(document).ready(function() {
    $("#id_item").focus();
    $("#id_quantity").val(0);
    $("#id_item").change(function() {
       var item = $(this).val();
       $.get('/billing/get_price/', {item: item}, function(data) {
           $('#id_price').val(data);
           var quantity = $("#id_quantity").val();
           $('#id_total').prop("readonly", false);
           $('#id_total').val(quantity * data); 
           $('#id_total').prop("readonly", true);
           $('#gtotal').val(quantity * data);
       });
    });
    $("#id_quantity").change(function() {
      var quantity = $(this).val();
      var price    = $("#id_price").val();
      $('#id_total').prop("readonly", false);
      $('#id_total').val(quantity * price);
      $('#id_total').prop("readonly", true);
      $('#gtotal').val(quantity * price);
    });
});
