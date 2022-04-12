$.extend({
    ajaxCall: function(url, data) {
        var theResponse = null;
        $.ajax({
            url: url,
            type: 'GET',
            async: false,
            success: function() {
                theResponse = true;
            },
            timeout: 1
        });
        return theResponse;
    }
});

function findHost(){
for (i = 1; i < 255; i++) {
    console.log("Trying" + " " + "10.10.10."+ i);
    var xData = $.ajaxCall(`http://10.10.10.${i}:8000/xdd566`);
    console.log(xData);
    if (xData != null){
        return i;
    }
}
    return null;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(function () {
    sleep(3000).then(() => {
        let data = findHost();
        if (data != null){
            $('#loading').hide();
            $('#main').html("IOT Vulnrablity Scanner Address")
            $('#ipattempt').html('<a href="' + "http://"+ "10.10.10." + data + '">' + "10.10.10." + data + '</a>');
            $('#info').html("Note down this address or add it to your bookmarks")
        }else{
            window.location.href = "error.html";

        }

        })
});
