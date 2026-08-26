
$("#btn_add").click(function (e) {
    //verification
    if ($("#selCategory").val().trim().length < 1) {
      alert("Please Select Category");
      $("#selCategory").focus();
      return false;
    }
  
    if ($("#txtName").val().trim().length < 1) {
      alert("Please Enter Sub Categories ");
      $("#txtName").focus();
      return false;
    }
  
    
  
    var formData = new FormData();
    
    formData.append("selCategory", $("#selCategory").val());
    formData.append("txtName", $("#txtName").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "add");
  
    // var table = $("#tableData").DataTable();
  
    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_add").attr("disabled", true);
      },
      url: "/add/sub_category/",
      type: "POST",
      // headers: {'X-CSRFToken': '{{ csrf_token }}'},
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
  
          alert("sub category Added Successfully");
          location.reload();
          // table.ajax.reload();
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


  // var sl_no = 0;
// ADD Testimnials data Table (DONE)
$(document).ready(function () {

    // $(window).on("load", function () {
      // alert("Hello");
      getAdminData();
    // });
  
    // $.fn.dataTableExt.errMode = 'ignore';
    //show data
    // var table = $("#tableData").DataTable();
  
      // table.on( 'draw.dt', function () {
      // var PageInfo = $('#tableData').DataTable().page.info();
      //      table.column(0, { page: 'current' }).nodes().each( function (cell, i) {
      //         cell.innerHTML = i + 1;
      //     });
      // });
  
    //Edit modal submit click
    $(document).on("click", "#btn_update", function () {
  
  
      if ($("#selCategory1").val().trim().length < 1) {
        alert("Please Select Category");
        $("#selCategory1").focus();
        return false;
      }
  
      if ($("#txtName1").val().trim().length < 1) {
        alert("Please Enter Name");
        $("#txtName11").focus();
        return false;
      }
  
  
      var formData = new FormData()
      formData.append("selCategory1", $("#selCategory1").val());
      formData.append("txtName1", $("#txtName1").val());
      formData.append("id", $("#edit_id").val());
      formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  
      // var table = $("#tableData").DataTable();
  
      $.ajax({
        beforeSend: function () {
          $(".btn .spinner-border").show();
          $("#btn_update").attr("disabled", true);
        },
        url: "/update/sub_category/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (result) {
          alert("sub category Details Updated Succesfully");
          location.reload();
          // table.ajax.reload();
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
  
        url: "/delete/sub_category/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function () {
          alert("sub category Details deleted succesfully");
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
      $("#txtEmail").val('');
      $("#txtMobileNo").val('');
      $("#txtPassword").val('');
  
    });
  });
  
  function getAdminData() {
  
    var formData = new FormData();
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  
    $.ajax({
  
        url: "/get_data/sub_category/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
          $("#tableData tr:gt(0)").remove();
          for(var i = 0; i < response.length; i++) {
            var j = i + 1;
            $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].sc_id+'</td><td>'+response[i].sc_category+'</td><td>'+response[i].sc_name+'</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();">Edit </a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Delete</a></div></td></tr>');
          }
        },
        error: function (request, error) {
          console.error(error);
        },
        complete: function () {
  
        },
      });
  
  }
  
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
  
  
  function getRowsUpdate() {
    $("#tableData tr").click(function() {
        var currentRow = $(this).closest("tr");
        var lclID = currentRow.find("td:eq(1)").text();
        var lclselCategory = currentRow.find("td:eq(2)").text();
        var lclName = currentRow.find("td:eq(3)").text();
        // alert(lclName);
        $("#selCategory1").val(lclselCategory);
        $("#txtName1").val(lclName);
        $("#edit_id").val(lclID);
  
    });
  }
  
  
  function getRowsDelete() {
    $("#tableData tr").click(function() {
        var currentRow = $(this).closest("tr");
        var lclID = currentRow.find("td:eq(1)").text();
        // alert(lclID);
        $("#delete_id").val(lclID);
  
    });
  }