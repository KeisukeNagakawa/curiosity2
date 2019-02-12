function runScript() {
    $.ajax({
        url: 'forward', //The URL you defined in urls.py
        success: function(data) {
            console.log("ajax is called")
        }

    });
}