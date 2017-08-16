function myTimer() {
    var theTime = new Date();
    document.getElementById('clock').innerHTML = theTime.toLocaleTimeString();
}
