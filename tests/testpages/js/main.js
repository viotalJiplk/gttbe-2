methodes = {
    "GET":{
        "name": "GET",
        "body": "unused" 
    },
    "POST":{
        "name": "POST",
        "body": "used"
    }
};
mimes = ["text/plain","application/json"]

class ReqElem extends HTMLElement{
    constructor(settings){
        super();
        let selfref = this;
        this.callbacks = new Array();

        this.shadowRootReference = this.attachShadow({mode: 'closed'});
        this.root_element = this;
        
        //adding stylesheet
        let link = document.createElement("link");
        link.setAttribute("rel","stylesheet");
        link.setAttribute("href", "../css/section.css");
        this.shadowRootReference.appendChild(link);

        //body textarea
        let textarea = document.createElement("textarea");
        textarea.setAttribute("id", "textarea");
        this.shadowRootReference.appendChild(textarea);
        
        //mime selector
        let mime = document.createElement("select");
        mime.setAttribute("id", "selectMime");
        mimes.forEach(function(element){
            let option = document.createElement("option");
            option.setAttribute("value", element);
            option.innerText = element;
            mime.appendChild(option);
        });
        this.shadowRootReference.appendChild(mime);

        //method selection
        let select = document.createElement("select");
        select.setAttribute("id", "selectMethod");
        for (const key in methodes) {
            let element = methodes[key]
            let option = document.createElement("option");
            option.setAttribute("value", element.name);
            option.innerText = element.name;
            select.appendChild(option);
        }
        select.addEventListener('change', function (event){
            if(methodes[event.target.value].body == "unused"){
                selfref.shadowRootReference.getElementById("textarea").style.display = "none";
                selfref.shadowRootReference.getElementById("selectMime").style.display = "none";
            }else{
                selfref.shadowRootReference.getElementById("textarea").style.display = "";
                selfref.shadowRootReference.getElementById("selectMime").style.display = "";
            }
        });
        this.shadowRootReference.appendChild(select);
        this.shadowRootReference.getElementById("selectMethod").dispatchEvent(new Event("change"));
        
        //url selection
        let url =  document.createElement("input");
        url.setAttribute("id", "url");
        this.shadowRootReference.appendChild(url);

        // submit button
        let button = document.createElement("button");
        button.setAttribute("id", "submitButton");
        button.innerText = "Try";
        button.addEventListener("click",function(event){
            // TODO lets send this
            selfref.execute(event);
        });
        this.shadowRootReference.appendChild(button);
        
        //httprescode bar
        let httprescode = document.createElement("p");
        let span = document.createElement("span");
        span.setAttribute("id", "httprescode");
        httprescode.innerText = "Response code: ";
        httprescode.appendChild(span);
        this.shadowRootReference.appendChild(httprescode);

        //output textarea
        let outtextarea = document.createElement("textarea");
        outtextarea.setAttribute("id", "outtextarea");
        this.shadowRootReference.appendChild(outtextarea);
    }
    
    static get observedAttributes(){return ["data-options", "class"];}

    getInputs(){
        return { 
            "body": this.shadowRootReference.getElementById("textarea").value,
            "method": this.shadowRootReference.getElementById("selectMethod").value,
            "url": this.shadowRootReference.getElementById("url").value,
            "outcode": this.shadowRootReference.getElementById("httprescode"),
            "out": this.shadowRootReference.getElementById("outtextarea"),
            "mime": this.shadowRootReference.getElementById("selectMime").value
        }
    }

    async execute(event){
        const inputs = this.getInputs();
        console.log(inputs);
        try {
            let result;
            if(methodes[inputs.method].body == "unused"){
                result = await fetch(inputs.url, {method:inputs.method});
            }else{
                result = await fetch(inputs.url, {
                    method:inputs.method,
                    body: inputs.body,
                    headers: {
                        'Content-Type': inputs.mime 
                    },
                });
            }
            inputs.outcode.innerText = result.status;
            result = await result.text();
            inputs.out.value = result;
            this.callbacks.forEach(function(element){
                element(result);
            })          
        } catch (error) {
            inputs.outcode.innerText = "";
            inputs.out.value = error.toString();
        }
    }

    addConnection(callback){
        this.callbacks.push(callback);
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if(name == "data-options"){
            newValue = JSON.parse(newValue);
            if (newValue.body){
                this.shadowRootReference.getElementById("textarea").value = newValue.body;
            }
            if(newValue.method){
                this.shadowRootReference.getElementById("selectMethod").value = newValue.method;
                this.shadowRootReference.getElementById("selectMethod").dispatchEvent(new Event("change"));
            }
            if(newValue.url){
                this.shadowRootReference.getElementById("url").value = newValue.url;
            }
            if(newValue.mime){
                this.shadowRootReference.getElementById("selectMime").value = newValue.mime;
            }
        }
        this.shadowRootReference.firstChild.setAttribute("data-sheet-name", newValue);
                
    }      
}

customElements.define('req-custom', ReqElem);