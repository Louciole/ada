let og
let desiredLink
let resultInput
let link

function initAda() {
    og = document.querySelector("#og")
    desiredLink = document.querySelector("#desired")
    resultInput = document.querySelector("#result")

    const createForm = document.querySelector("#create")
    createForm.addEventListener("submit", function(e) {
        e.preventDefault()
        createLink()
    });
    initTheme()
}

function createLink(){
    console.log(og.value,desiredLink.value)
    const url = "/addLink?link="+og.value+"&pref="+desiredLink.value
    let request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.onload = function() {
        console.log("loaddeeeddd",request.responseText)
        resultInput.style.display="flex"
        resultInput.addEventListener("click",copylink)
        link = "https://kip.yt/".concat(request.responseText)
        resultInput.value= link
        copylink(link)
    };

    request.onerror = function() {
        console.log("request failed")
    };
    request.send();
}

function copylink(){
    navigator.clipboard.writeText(link);
    createNotif("link copied in clipboard")
}

function createNotif(msg){
    const notif = document.body.querySelector('#notif')
    notif.style.display="flex"
    notif.innerHTML=msg
    setTimeout(() => notif.style.display="none", 1500)
}

