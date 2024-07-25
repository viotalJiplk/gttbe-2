redirect_url = "http://127.0.0.1:5000/backend/test/testpages/discord/login.html#getjws";
document.getElementById("getDiscordURL").addConnection(function(text) {
    const input = JSON.parse(text);
    let discordhref = input.redirect_url + "&redirect_uri=" +  encodeURIComponent(redirect_url);
    document.getElementById("redirectLink").innerText = discordhref;
    document.getElementById("redirectLink").setAttribute("href", discordhref);
});

params = new URLSearchParams(location.search);
code = params.get("code");
state = params.get("state");
if(code != null & state != null){
    document.getElementById("getjws").setAttribute("data-options", JSON.stringify({"body":"{\"code\":\"" + code +"\", \"state\":\"" + state +"\", \"redirect_uri\":\"" + redirect_url +"\", \"name\":\"Name\", \"surname\":\"surName\",\"adult\":1, \"school_id\":1}"}))
}

document.getElementById("getjws").addConnection(function(text) {
    const input = JSON.parse(text);
    localStorage.setItem("jws", input.jws)
});
