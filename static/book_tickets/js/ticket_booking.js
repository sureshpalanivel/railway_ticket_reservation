
/* Added in Main .html File */

// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));   
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');
// console.log(csrftoken)

CURFORM = $('#ticket_booking_frm');

$.ajax({
    type: 'GET',
    url: CURFORM.attr('data-form_data'),
    //url: 'http://127.0.0.1:8000/api/tickets/form-data/',
    //headers : {'csrfmiddlewaretoken':csrftoken},
    dataType: 'json',
    //data: {'csrfmiddlewaretoken':csrftoken},    
    success: function (response) {
        $('#id_gender option').remove();
        $('#id_berth_preference option').remove();
        var gender = '<option value="">-- Select --</option>';      
        $.each(response.gender,function(k,v){ 
            gender += '<option value="'+ v.code +'">'+v.name+'</option>'
        });
        $('#id_gender').append(gender);

        var berth = '<option value="">-- Select --</option>';      
        $.each(response.berth,function(k,v){ 
            berth += '<option value="'+ v.code +'">'+v.name+'</option>'
        });
        $('#id_berth_preference').append(berth);
    },
    // error: function (response) {
    //     //alert('www')
    // }
});

CURFORM.on('submit',function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: CURFORM.attr('data-book'),
        //url: 'http://127.0.0.1:8000/api/tickets/book/',
        dataType: 'json',         
        data: {
            'csrfmiddlewaretoken':csrftoken, 
            'name': $('#id_name',CURFORM).val(), 
            'age': $('#id_age',CURFORM).val(), 
            'gender': $('#id_gender',CURFORM).val(), 
            'berth_preference': $('#id_berth_preference',CURFORM).val(), 
        },      
        success: function (response) {
            console.log(response);
            //url = 'http://127.0.0.1:8000/tickets/status/'+response.id+'/';
            $('input',CURFORM).val('')
            window.location.href = response.url;
        },
        error: function (jqXHR, exception, op) {            
            CURFORM.before('<div class="alert alert-danger col-sm-10">'+jqXHR.responseJSON.error+'<a href="#" class="close" area-label="close" data-dismiss="alert">&times;</a></div>');	
            //$('.alert',CURFORM).fadeOut(6000);			
        }
    });
    //console.log('hai');
});




//alert('fgs')

// $('#good').on('click',function(){
//     alert('Hai...');

//     $.ajax({
//         type: 'POST',
//         url: 'http://127.0.0.1:8000/api/tickets/book/',
//         success: function (response) {
//             console.log(response);
//             alert('qqq')
//         },
//         error: function (response) {
//             alert('www')
//         }
//     });
//     console.log('hai');
// });