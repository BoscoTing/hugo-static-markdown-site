function ajax(src, callback){
    // your code here
    let xhr = new XMLHttpRequest();
    var url = src;
    xhr.open("GET", url, true)
    xhr.onreadystatechange == function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    }
};

function render(data){
    // your code here.
    // document.createElement() and appendChild() methods are preferred.
        var newDiv = document.createElement('div')
        var newContent = document.createTextNode('Textnode created.')
        newDiv.appendChild(newContent)
};

ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
    function(response) { render(response);
}); // you should get product information in JSON format and render data in the page