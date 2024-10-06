const submit = document.getElementById("submit");
const url = document.getElementById("url");
const file = document.getElementById("file");
const statusEl = document.getElementById("status");
const result = document.getElementById("result");

const jws = localStorage.getItem("jws");
if(jws == ""){
    alert("Go to login page to get jws");
}

async function upload() {
    let uploadFile = file.files[0];
    const response = await fetch(url.value, {
        method: 'PUT',
        body: uploadFile,
        headers: {
            'Content-Type': uploadFile.type,
            "Authorization": "Bearer " + jws,
        },
    });
    statusEl.innerText = response.status;
    result.innerText = await response.text();
}

submit.addEventListener("click", upload);
