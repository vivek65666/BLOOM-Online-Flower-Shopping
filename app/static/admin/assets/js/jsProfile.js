function getUserData() {
  // alert("Hi");
  let formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );

  $.ajax({
    url: "/get_profile_data/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      $("#tableData tr:gt(0)").remove();
      for (let i = 0; i < response.length; i++) {
        $("#txtName").val(response[0].ad_name);
        $("#txtEmail").val(response[0].ad_email);
        $("#txtNumber").val(response[0].ad_mobile);
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {},
  });
}

getUserData();

$("#btn_update").click(function (e) {
  //verification
  if ($("#txtName").val().trim().length < 1) {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }
  if ($("#txtNumber").val().trim().length < 10) {
    alert("Please Enter Mobile Number");
    $("#txtNumber").focus();
    return false;
  }

  let formData = new FormData();

  formData.append("txtName", $("#txtName").val());
  formData.append("txtNumber", $("#txtNumber").val());
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "add");

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/admin_update_profile/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {
      alert("Details Updated Successfully");
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_add").attr("disabled", false);
    },
  });
});
