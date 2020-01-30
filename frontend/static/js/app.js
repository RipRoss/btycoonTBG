email = document.getElementById('user_input')
password = document.getElementById("password_input")


function send_user(){
    payload = {
        "username": email.value,
        "password": password.value
    }
    $.ajax({
        type: 'POST',
        url: 'http://localhost:5000/da/auth_user',
        contentType: "application/json;",
        dataType: 'json',
        data: JSON.stringify(payload),
        success: function(data){
            console.log(data)
        },
        error: function(xhr) {
            console.log(xhr.status)
        }
    })
}