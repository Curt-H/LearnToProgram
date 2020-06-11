function main() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://wwww.bilibili.com', true);
    if (xhr.readyState == 4) {
        var content = xhr.responseText;
        document.getElementById('test').innerHTML = content
    }
}

function run_ajax() {
    interval = setInterval(main, '1000');
}