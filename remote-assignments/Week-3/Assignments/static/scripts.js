var send_botton = document.getElementsByClassName("send_botton")[0];
send_botton.addEventListener('click', () => {
    let number = document.getElementsByClassName("text_bar")[0].value;
    // document.getElementById('N').innerHTML = number
    var xhttp = new XMLHttpRequest(); 
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) { 
        //    let result = xhttp.responseText
            document.getElementById("result").innerHTML = this.responseText;
        }
    }
    xhttp.open("GET", `data?number=${ number }`, true);
    xhttp.send();
})

