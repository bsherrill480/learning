function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function() {
    function modalLogin(event) {
        console.log("loggin in");
        $("#login-form").submit();
    }
    function enterLogin(event){
        if(event.which == 13) {
            modalLogin(event);
        }
    }

    $("#register-button").click(function(event){
        console.log("register-button clicked");
        $("#register-form").submit();
    });
    $("#login-button").click(modalLogin);
    $("#login-password").keypress(enterLogin);
    $("#login-username").keypress(enterLogin);
    $("#logout-button").click(function(event){
        console.log("logout-button clicked");
        $.ajax({
            type: "POST",
            url: "/auth/logout/",
            success: function() {
                window.location = '/';
            }
        });
    });
});