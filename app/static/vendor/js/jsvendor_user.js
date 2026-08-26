function getUserData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );

  $.ajax({
    url: "/get_user_data/",
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
            response[i].rg_id +
            "</td><td>" +
            response[i].rg_name +
            "</td><td>" +
            response[i].rg_email +
            "</td><td>" +
            response[i].rg_mobile +
            "</td><td>" +
            response[i].rg_address +
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
