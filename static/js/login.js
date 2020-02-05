function toggle(){
    var blur = document.getElementById("b1");
    blur.classList.toggle('active');
    var log = document.getElementById("log");
    log.classList.toggle('active');
    document.getElementById("log").style.display = 'block';
}