function ajax(src, callback) {
    const httpRequest = new XMLHttpRequest();
    const url = src

    httpRequest.onreadystatechange = () => {
        if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
            callback(httpRequest.response);
        } else {
            // alert('not ready');
            return false;
        }
    }
    httpRequest.open("GET", url, true);
    httpRequest.send();
};

function render(data) {
    const dataJson = JSON.parse(data)
    const dataDict = Object.values(dataJson) 
    const cols = Object.keys(Object.values(dataDict)[0]) // name, price, description
    const dataKeys = Object.keys(dataDict)

    i = 1
    for (let key of dataKeys) { // key = 0, 1, 2
        let itemDict = dataDict[key]; 
        var newLi = document.createElement("li")
        var newContent = document.createTextNode(`Item${i}`); // i = 1, 2, 3
        newLi.appendChild(newContent);
        var currentLi = document.getElementById("li");
        document.body.insertBefore(newLi, currentLi);
        i += 1

        for (let itemKey of cols) { //name, price, description
            let itemValue = itemDict[itemKey] // pixel3, 1700, ...
            var newDiv = document.createElement("ul");
            var newContent = document.createTextNode(`${itemKey}: ${itemValue}`);
            newDiv.appendChild(newContent);
            var currentDiv = document.getElementById("ul");
            document.body.insertBefore(newDiv, currentDiv);
        }
    }
};

ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
    function(response) { 
        render(response);
});

