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
for (i = 1; i < 256; i++) {
    console.log("Trying" + " " + "10.10.10."+ i);
    var xData = $.ajaxCall(`http://10.10.10.${i}:8000/xdd566`);
    console.log(xData);
    if (xData != null){ 
        return i;
    }

}
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(function () {
    sleep(3000).then(() => {
        let data = findHost();
        console.log(data);
        })  
});
