$(document).ready(function () {
    $("#btn_add").click(function () {
        if ($("#village").val() == "") {
            alert("Please enter Village");
            return false
        }
        if ($("#state").val() == "") {
            alert("Please enter State");
            return false
        }

        if ($("#zip").val() == "") {
            alert("Please enter Zip");
            return false
        }
        // if ($("#address").val() == "") {
        //     alert("Plz enter Address");
        //     return false
        // }
        // if ($("#city").val() == "") {
        //     alert("Please enter city");
        //     return false
        // }
        // if ($("#zip").val() == "") {
        //     alert("Please Enter Zip");
        //     return false
        // }
        // if ($("#phone").val() == "") {
        //     alert("Please Enter Phone");
        //     return false
        // }
        // if ($("#selRole").val() == "") {
        //     alert("Please select your domain");
        //     $("#selRole").focus();
        //     return false;
        // }



    })
})
