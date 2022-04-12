$.extend({
    ajaxCall: function(url, data) {  // 
        var theResponse = null;
        $.ajax({ // setting the parameters such as the url and http request type (get)
            url: url,
            type: 'GET',
            async: false,
            success: function() { // on sucess the 
                theResponse = true;
            },
            timeout: 1
        });
        return theResponse; // responce is retunred to be checked by the find hostHost function that called this function
    }
});

function findHost(){
for (i = 1; i < 255; i++) { // Itterating over the possible 254 hosts that the vulnrablity scanner could be on 
    console.log("Trying" + " " + "10.10.10."+ i); // for debugging
    var xData = $.ajaxCall(`http://10.10.10.${i}:5000/64d42a0081addc9bd303ccf4bd598046`);
    console.log(xData);  // for debugging
    if (xData != null){
        return i;
    }
}
    return null; // Null is retunred if no vulnrablity scanner is found
}

function sleep(ms) { // createing a new function that acts as a way to call setTimeout which I am using as sleep
    return new Promise(resolve => setTimeout(resolve, ms));
}

$(function () { // waitnig for the page to load 
    sleep(3000).then(() => { // waiting for the rest of the page to load 
        let data = findHost(); // calling the findHost function and getting data it retunrs in to the data variable 
        if (data != null){ // if the scanner is found 
            $('#loading').hide(); 
            $('#main').html("IOT Vulnrablity Scanner Address") // hiding elements on the page and replacing elements with jquery library
            $('#ipattempt').html('<a href="' + "http://"+ "10.10.10." + data + '">' + "10.10.10." + data + '</a>');
            $('#info').html("Note down this address or add it to your bookmarks")
        }else{
            window.location.href = "error.html"; // showing error page if no vulnerability scanner is found 

        }

        })
});
