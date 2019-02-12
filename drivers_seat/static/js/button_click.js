function forward() {
    $.ajax({
        url: 'forward', //The URL you defined in urls.py
        success: function(data) {
            console.log("forward function is called in ajax")
        }

    });
}

function backward() {
    $.ajax({
        url: 'backward', //The URL you defined in urls.py
        success: function(data) {
            console.log("backward function is called in ajax")
        }

    });
}

function left() {
    $.ajax({
        url: 'left', //The URL you defined in urls.py
        success: function(data) {
            console.log("left function is called in ajax")
        }

    });
}

function right() {
    $.ajax({
        url: 'right', //The URL you defined in urls.py
        success: function(data) {
            console.log("right function is called in ajax")
        }

    });
}


function stop() {
    $.ajax({
        url: 'stop', //The URL you defined in urls.py
        success: function(data) {
            console.log("stop function is called in ajax")
        }

    });
}
