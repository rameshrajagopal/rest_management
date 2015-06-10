$(document).ready(function() {
    var counter = 0;
    $("#id_form-"+ counter + "-item").focus();
    $("#id_form-"+ counter + "-quantity").val(0);
    $("#id_form-"+ counter + "-item").change(function() {
       var item = $(this).val();
       $.get("/billing/get_price/", {item: item}, function(data) {
           $("#id_form-"+ counter + "-price").val(data);
           var quantity = $("#id_form-"+ counter + "-quantity").val();
           $("#id_form-"+ counter + "-total").prop("readonly", false);
           $("#id_form-"+ counter + "-total").val(quantity * data); 
           $("#id_form-"+ counter + "-total").prop("readonly", true);
           $("#gtotal").val(quantity * data);
       });
    });
    $("#id_form-"+ counter + "-quantity").change(function() {
      var quantity = $(this).val();
      var price    = $("#id_form-"+ counter + "-price").val();
      $("#id_form-"+ counter + "-total").prop("readonly", false);
      $("#id_form-"+ counter + "-total").val(quantity * price);
      $("#id_form-"+ counter + "-total").prop("readonly", true);
      $("#gtotal").val(quantity * price);
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
              id}).val('').removeAttr('checked');
             });
        
        newElement.find('label').each(function() {
            var newFor =
            $(this).attr('for').replace('-' +
                (total-1) + '-','-' + total + '-');
            $(this).attr('for', newFor);
            });
        total++;
        counter = total;
        $('#id_form-TOTAL_FORMS').val(total);
        $("div.bill_items:last").append(newElement);
     });
});
