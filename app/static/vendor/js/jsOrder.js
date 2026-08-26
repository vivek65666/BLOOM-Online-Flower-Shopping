function getUserData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );

  $.ajax({
    url: "/get_order_data/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      $("#tableData tr:gt(0)").remove();
      for (var i = 0; i < response.length; i++) {
        var j = i + 1;
        $("#tableData").append(
          "<tr><td>" +
            j +
            '</td><td style="display: none;">' +
            response[i].ps_id +
            "</td><td>" +
            response[i].ps_user_name +
            "</td><td>" +
            response[i].ps_date +
            "</td><td>" +
            response[i].ps_product_name +
            "</td><td>" +
            response[i].ps_weight +
            "</td><td>" +
            response[i].ps_price +
            "</td><td>" +
            response[i].ps_total_amt +
            "</td></tr>"
        );
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {},
  });
}

getUserData();
