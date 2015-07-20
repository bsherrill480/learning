$(document).ready(function() {
    $("#register-button").click(function(event){
        console.log("register-button clicked");
        $("#register-form").submit();
    });
});