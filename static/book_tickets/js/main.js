
/* Added in Main .html File */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {          
            const cookie = cookies[i].trim();            
            if (cookie.substring(0, name.length + 1) === (name + '=')) {                
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1)); 
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function isNumberKey(a) { 
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57 || charCode == 46)) {
        return false;
    }
    if ($('#id_age').val().length < 4) {
        return false;
    }
    return true;
    // if(a.key == '5'){
    //     console.log('rrr')
    //     return true
    // }
    // console.log('eee')
    // return false;
}

// function isNumberKey(evt) {    
//     var charCode = (evt.which) ? evt.which : evt.keyCode;
//     if (charCode > 31 && (charCode < 48 || charCode > 57 || charCode == 46)) {
//         return false;
//     }
//     return true;
// }

function alphaBets_withspace(e) {
    var code = e.charCode ? e.charCode : e.keyCode;
    if (((code >= 65 && code <= 90) || (code >= 97 && code <= 122) || (code == 37 && e.charCode == 0) || (code == 39 && e.charCode == 0) || code == 116 || code == 32 || code == 9 || code == 8 || (code == 46 && e.charCode == 0))) {
        return true;
    }
    return false;
}

// function onlyNumberKey(evt) { 
          
//     // Only ASCII charactar in that range allowed 
//     var ASCIICode = (evt.which) ? evt.which : evt.keyCode 
//     if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57)) 
//         return false; 
//     return true; 
// } 

