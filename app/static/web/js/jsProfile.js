getData1();
function getData1() {
  let formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );

  $(".login").hide();
  $(".logout").show();

  $.ajax({
    url: "/get_my_profile/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      for (let i = 0; i < response.length; i++) {
        $(".login").show();
        $(".logout").hide();
        $("#txtName").val(response[0].rg_name);
        $("#txtEmail").val(response[0].rg_email);
        $("#txtMobileNo").val(response[0].rg_mobile);
        $("#txtAddress").val(response[0].rg_address);
      }
    },
  });
}
