// Build log method
var log = console.log.bind(console)

var ajax = function () {
    // Create an xhr object
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:80', true);


    xhr.send(null)
    if (xhr.readyState == 4) {
        var content = xhr.responseText;
        console.log(content);
        document.getElementById('test').innerHTML = content
    }
}

function run_ajax() {
    console.log('Start');
    ajax();
}