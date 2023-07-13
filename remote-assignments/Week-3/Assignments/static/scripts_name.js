var result = document.getElementById('result');
var textBarContent = document.getElementsByClassName('text_bar')[0];
result.style.display = 'none';
if (textBarContent.getAttribute('value') != "") {
    // alert(textBarContent.getAttribute('value'))
    result.removeAttribute('style');
    textBarContent.setAttribute('type', "hidden");
    document.getElementsByClassName('submit_button')[0].setAttribute('type', "hidden");
}   else {
    alert('Nice to meet you!')
}