function submitForm() {
    var uname = $("#user-name").val();
    var password = $("#password").val();

    if(uname == '' || password == ''){
        $('<span>Please enter Uname</span>').css("border","2px solid red");
        $('input[type="text"],input[type="password"]').css("box-shadow","0 0 3px red");
    }else{
        console.log("You are done.")
    }
}