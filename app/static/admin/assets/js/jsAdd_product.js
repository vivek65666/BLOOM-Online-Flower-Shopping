function validateEmail(paramEmailID) {
    var filter = /^[0-9a-z.]+\@[a-z0-9]+\.[a-zA-z0-9]{2,4}$/;

    if (filter.test(paramEmailID)) {
        return true;
    } else {
        return false;
    }
}

// alert("Hello");

$("#btn_add").click(function (e) {
    //verification
    
  if ($("#selCategory").val().trim().length < 1) {
    alert("Please Select Category");
    $("#selCategory").focus();
    return false;
  }

  // if ($("#selSubCategory").val().trim().length < 1) {
  //   alert("Please Select Sub Category");
  //   $("#selSubCategory").focus();
  //   return false;
  // }

    if ($("#txtName").val().trim().length < 1) {
        alert("Please Enter Name");
        $("#txtName").focus();
        return false;
    }

    if ($("#txtPrice").val().trim().length < 1) {
        alert("Please Enter Price");
        $("#txtPrice").focus();
        return false;
    }


    if ($("#txtQuantity").val().trim().length < 1) {
        alert("Please Enter Quantity");
        $("#txtQuantity").focus();
        return false;
    }
    if ($("#txtImage").val()=="") {
        alert("Please choose Image");
        $("#txtImage").focus();
        return false;
    }

    if ($("#txtDescription").val().trim().length < 1) {
        alert("Please Enter Description");
        $("#txtDescription").focus();
        return false;
    }


    // database
    var formData = new FormData();
    var lclFile = document.getElementById("txtImage");
    lclImage = lclFile.files[0];

    formData.append("selCategory", $("#selCategory").val());
    // formData.append("selSubCategory", $("#selSubCategory").val());
    formData.append("txtName", $("#txtName").val());
    formData.append("txtPrice", $("#txtPrice").val());
    formData.append("txtQuantity", $("#txtQuantity").val());
    formData.append("txtImage", lclImage);
    formData.append("txtDescription", $("#txtDescription").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "add");
  
  
  
    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_add").attr("disabled", true);
      },
      url: "/add/product/",
      type: "POST",
      // headers: {'X-CSRFToken': '{{ csrf_token }}'},
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
  
        alert("Details Added Successfully");
        location.reload();
        table.ajax.reload();
        $("#add_modal").modal('hide');
  
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

  // data fetching (display into admin dashboard )
  function getAdminData() {
    // alert("Hi");
    var formData = new FormData();
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "getData");
  
  
    $.ajax({
  
      url: "/get_data/product/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
  
        console.log(response);
        // $("#dataTables-example tr:gt(0)").remove();
        $("#tableData tr:gt(0)").remove();
        for (var i = 0; i < response.length; i++) {
          var j = i + 1;
          let image = response[i].ap_image.substring(3);
          $("#tableData").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].ap_id +'</td><td>'+response[i].ap_category+ '</td><td>' + response[i].ap_name + '</td><td>'  + response[i].ap_price + '</td><td>' + response[i].ap_quantity + '</td><td>'+ response[i].ap_description + '</td><td><a href="'+image+'" download>download</a></td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal"  class="text-primary" onClick="getRowsUpdate();">Edit</a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Delete</a></div></td></tr>');
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
  
      },
    });
  
  }

  // Edit data
  //Edit modal submit click
  $(document).on("click", "#btn_update", function () {
    // alert("hi");
    if ($("#selCategory1").val().trim().length < 1) {
      alert("Please Select Category");
      $("#selCategory1").focus();
      return false;
    }

    // if ($("#selSubCategory1").val().trim().length < 1) {
    //   alert("Please Select Sub Category");
    //   $("#selSubCategory1").focus();
    //   return false;
    // }

    if ($("#txtName1").val().trim().length < 1) {
      alert("Please Enter Name");
      $("#txtName1").focus();
      return false;
    }


    if ($("#txtPrice1").val().trim().length < 1) {
      alert("Please Enter Price");
      $("#txtPrice1").focus();
      return false;
    }

    // if ($("#txtImage1").val().trim().length < 1) {
    //     alert("Please Choose File");
    //     $("#txtImage1").focus();
    //     return false;
    // }

    if ($("#txtQuantity1").val().trim().length < 1) {
      alert("Please Enter Quantity");
      $("#txtQuantity1").focus();
      return false;
    }

    
    if ($("#txtDescription1").val().trim().length < 1) {
        alert("Please Enter Description");
        $("#txtDescription1").focus();
        return false;
      }
 
    var formData = new FormData()
    formData.append("selCategory1", $("#selCategory1").val());
    // formData.append("selSubCategory1", $("#selSubCategory1").val());
    formData.append("txtName1", $("#txtName1").val());
    formData.append("txtPrice1", $("#txtPrice1").val());
    // formData.append("txtImage1", $("#txtImage1").val());
    formData.append("txtQuantity1", $("#txtQuantity1").val());
    formData.append("txtDescription1", $("#txtDescription1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");

    // var table = $("#dataTables-example").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/update/product/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert(" Details Updated Succesfully");
        location.reload();
        table.ajax.reload();
        $("#edit_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        $("#btn_update").attr("disabled", false);
      },
    });
  });

  
  function getRowsUpdate() {
    $("#tableData tr").click(function() {
        var currentRow = $(this).closest("tr");
        var lclID = currentRow.find("td:eq(1)").text();
        var lclCategory = currentRow.find("td:eq(2)").text();
      // var lclSubCategory = currentRow.find("td:eq(3)").text();
        var lclName = currentRow.find("td:eq(3)").text();
        var lclPrice = currentRow.find("td:eq(4)").text();
        // var lclImage = currentRow.find("td:eq(4)").text();
        var lclQuantity= currentRow.find("td:eq(5)").text();
        var lclDescription= currentRow.find("td:eq(6)").text();


  
        // alert(lclName);  
        $("#selCategory1").val(lclCategory);
      // $("#selSubCategory1").append('<option value="'+lclSubCategory+'">'+lclSubCategory+'</option>');
        $("#txtName1").val(lclName);
        $("#txtPrice1").val(lclPrice);
        // $("#txtImage1").val(lclImage);
        $("#txtQuantity1").val(lclQuantity);
        $("#txtDescription1").val(lclDescription);
        $("#edit_id").val(lclID);
  
    });
  }

  // Delete
 //Delete work step
 $(document).on("click", "#btn_delete", function () {

  var formData = new FormData();
  formData.append("id", $("#delete_id").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());

  // var table = $("#tableData").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
    },

    url: "/delete/product/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function () {
      alert("Product deleted succesfully");
      location.reload();
      table.ajax.reload();
      $("#delete_modal").modal('hide');
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      // Reset Form
      //$("#view_field_form")[0].reset();
      $(".close").click();
    },
  });
});

$(document).on("click", "#add_user", function () {

  $("#txtName").val('');
  $("#txtImage").val('');
  $("#txtDescription").val('');

});


  function getRowsDelete() {
    $("#tableData tr").click(function () {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      // alert(lclID);
      $("#delete_id").val(lclID);
  
    });
  }
  getAdminData()

  
function getCategory() {

  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  
  $.ajax({

      url: "/get_data/category/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        for(var i = 0; i < response.length; i++) {
          $("#selCategory").append("<option value='"+response[i].ca_name+"'>"+response[i].ca_name+"</option>");
          $("#selCategory1").append("<option value='"+response[i].ca_name+"'>"+response[i].ca_name+"</option>");
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}
getCategory();


// $("#selCategory").change(function() {

//   // alert($("#selShopCity").val());
//   var formData = new FormData();
//   formData.append("selCategory", $("#selCategory").val());
//   formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  
//   $.ajax({

//       url: "/get_sub_Category/",
//       type: "POST",
//       data: formData,
//       processData: false,
//       contentType: false,
//       success: function (response) {
//         $("#selSubCategory").empty();
//         $("#selSubCategory").append("<option value=''>Please Select Sub Category</option>");
//         for(var i = 0; i < response.length; i++) {
//           $("#selSubCategory").append("<option value='"+response[i].sc_name+"'>"+response[i].sc_name+"</option>");

//         }
//       },
//       error: function (request, error) {
//         console.error(error);
//       },
//       complete: function () {

//       },
//     });

// });


// $("#selCategory1").change(function() {

//   // alert($("#selShopCity").val());
//   var formData = new FormData();
//   formData.append("selCategory1", $("#selCategory1").val());
//   formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  
//   $.ajax({

//       url: "/get_sub_Category/",
//       type: "POST",
//       data: formData,
//       processData: false,
//       contentType: false,
//       success: function (response) {
//         $("#selSubCategory1").empty();
//         $("#selSubCategory1").append("<option value=''>Please Select Sub Category</option>");
//         for(var i = 0; i < response.length; i++) {
//           $("#selSubCategory").append("<option value='"+response[i].sc_name+"'>"+response[i].sc_name+"</option>");

//         }
//       },
//       error: function (request, error) {
//         console.error(error);
//       },
//       complete: function () {

//       },
//     });

// });