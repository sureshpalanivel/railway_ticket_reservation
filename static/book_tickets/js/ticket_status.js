
/* Added in Main .html File */


var ticket_url = $('#ticket_id').attr('data-url')
console.log(ticket_url)
console.log(csrftoken)

if(ticket_url != null && ticket_url != '') {   
    $.ajax({
        type: 'GET',
        url: ticket_url,
        dataType: 'json',
        //data: {'csrfmiddlewaretoken':csrftoken},    
        success: function (response) {
            console.log(response.label)
            $('#ticket_code').text(response.id)
            $('#name').text(response.name)
            $('#gender').text(response.gender)
            $('#age').text(response.age)
            $('#coach').text(response.coach)
            $('#berth').text(response.berth)
            $('#status').text(response.ticket_status)
            $('#date').text(response.created_at)
            if(response.label == true){
                $('#ticket_id').attr('class','').text(response.msg).attr('class','text-center text-success')
            }else{
                $('#ticket_id').attr('class','').text(response.msg).attr('class','text-center text-warning')
            }
        },
        // error: function (response) {
        //     //alert('www')
        // }
    });
}

