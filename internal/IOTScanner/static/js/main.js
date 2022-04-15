$(function () {

    $("#scan").on('click', function(){
        $("#loading").show();
        $("#scan").hide();
        $("#maintext").html("Scanning Your Network For Vulnerable IOT Devices")
    })

});