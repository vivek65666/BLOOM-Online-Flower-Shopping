function getUserData() {
    // alert("Hi");
    var formData = new FormData();
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  
    $.ajax({
  
        url: "/get_order_data/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
          $("#tableData tr:gt(0)").remove();
          for(var i = 0; i < response.length; i++) {
            var j = i + 1;
            $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].or_id+'</td><td>'+response[i].or_name+'</td><td>'+response[i].or_total_amount+'</td><td>'+response[i].or_address+'</td><td>'+response[i].or_date+'</td><td>'+response[i].or_transaction_id+'</td></tr>');
          }
        },
        error: function (request, error) {
          console.error(error);
        },
        complete: function () {
  
        },
      });
  
  }
  
  getUserData();