$(document).ready(function () {
    $("#btn_add").click(function () {
        if ($("#txtName").val() == "") {
            alert("Please enter Name");
            return false
        }
        if ($("#txtNumber").val() == "") {
            alert("Please enter Number");
            return false
        }

        if ($("#txtEmail").val() == "") {
            alert("Please enter Email");
            return false
        }
        // if ($("#txtPrice").val() == "") {
        //     alert("Plz enter Price");
        //     return false
        // }
        // if ($("#txtDescription").val() == "") {
        //     alert("Please enter Description");
        //     return false
        // }
        // if ($("#txtImage").val() == "") {
        //     alert("Please upload image");
        //     return false
        // }
        if ($("#selRole").val() == "") {
            alert("Please select your domain");
            $("#selRole").focus();
            return false;
        }



    })
})