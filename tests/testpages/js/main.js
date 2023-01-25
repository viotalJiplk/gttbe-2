methodes = {
    "GET":{
        "name": "GET",
        "body": "unused" 
    },
    "POST":{
        "name": "POST",
        "body": "used"
    },
    "DELETE":{
        "name": "DELETE",
        "body": "unused"
    }
};
mimes = ["text/plain","application/json"]

class ReqElem extends HTMLElement{
    constructor(settings){
        super();
        let selfref = this;
        this.callbacks = new Array();
        const div = document.createElement("div");
        const p = document.createElement("p");

        this.shadowRootReference = this.attachShadow({mode: 'closed'});
        this.root_element = this;
        
        {
            //adding stylesheet
            let link = document.createElement("link");
            link.setAttribute("rel","stylesheet");
            link.setAttribute("href", "../css/section.css");
            this.shadowRootReference.appendChild(link);
        }

        {
            //headers textarea
            let reqheaders = div.cloneNode();
            
            let reqp = p.cloneNode();
            reqp.innerText = "request headers:";
            reqheaders.appendChild(reqp);

            reqheaders.setAttribute("id", "headers");
            let textarea = document.createElement("textarea");
            textarea.setAttribute("id", "headersarea");
            reqheaders.appendChild(textarea);
            
            this.shadowRootReference.appendChild(reqheaders);
        }

        {
            //body textarea
            let reqbody = div.cloneNode();
            
            let reqp = p.cloneNode();
            reqp.innerText = "request body:";
            reqbody.appendChild(reqp);

            reqbody.setAttribute("id", "body");
            let textarea = document.createElement("textarea");
            textarea.setAttribute("id", "textarea");
            reqbody.appendChild(textarea);
            
            this.shadowRootReference.appendChild(reqbody);
        }

        // {
        //     //mime selector
        //     let mimediv = div.cloneNode()
        //     mimediv.setAttribute("id", "divMime");

        //     let mimep = p.cloneNode();
        //     mimep.innerText = "select mime:";
        //     mimediv.appendChild(mimep);
            
        //     let mime = document.createElement("select");
        //     mime.setAttribute("id", "selectMime");
        //     mimes.forEach(function(element){
        //         let option = document.createElement("option");
        //         option.setAttribute("value", element);
        //         option.innerText = element;
        //         mime.appendChild(option);
        //     });
        //     mimediv.appendChild(mime);

        //     this.shadowRootReference.appendChild(mimediv);
        // }
        
        {
            //method selection
            let selectdiv = div.cloneNode()
            selectdiv.setAttribute("id", "selectMime");

            let selectp = p.cloneNode();
            selectp.innerText = "select method:";
            selectdiv.appendChild(selectp);

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
                    selfref.shadowRootReference.getElementById("body").style.display = "none";
                    // selfref.shadowRootReference.getElementById("divMime").style.display = "none";
                }else{
                    selfref.shadowRootReference.getElementById("body").style.display = "";
                    // selfref.shadowRootReference.getElementById("divMime").style.display = "";
                }
            });
            selectdiv.appendChild(select)
            this.shadowRootReference.appendChild(selectdiv);
            this.shadowRootReference.getElementById("selectMethod").dispatchEvent(new Event("change"));
        }

        {
            //url selection

            let urldiv = div.cloneNode()
            urldiv.setAttribute("id", "selectUrl");

            let urlp = p.cloneNode();
            urlp.innerText = "select url:";
            urldiv.appendChild(urlp);
            
            let url =  document.createElement("input");
            url.setAttribute("id", "url");
            
            urldiv.appendChild(url);
            this.shadowRootReference.appendChild(urldiv);
        }

        {
            // submit button
            let button = document.createElement("button");
            button.setAttribute("id", "submitButton");
            button.innerText = "Try";
            button.addEventListener("click",function(event){
                // TODO lets send this
                selfref.execute(event);
            });
            this.shadowRootReference.appendChild(button);
        }

        {
            //httprescode bar
            let httprescode = document.createElement("p");
            let span = document.createElement("span");
            span.setAttribute("id", "httprescode");
            httprescode.innerText = "Response code: ";
            httprescode.appendChild(span);
            this.shadowRootReference.appendChild(httprescode);
        }
        
        {
            //output textarea
            let outtextarea = document.createElement("textarea");
            outtextarea.setAttribute("id", "outtextarea");
            this.shadowRootReference.appendChild(outtextarea);
        }
    }
    
    static get observedAttributes(){return ["data-options", "class"];}

    getInputs(){
        let headers = this.shadowRootReference.getElementById("headersarea").value;
        if(headers != ""){
            headers = JSON.parse(this.shadowRootReference.getElementById("headersarea").value);
        }
        else{
            headers = undefined;
        }

        return { 
            "body": this.shadowRootReference.getElementById("textarea").value,
            "method": this.shadowRootReference.getElementById("selectMethod").value,
            "url": this.shadowRootReference.getElementById("url").value,
            "outcode": this.shadowRootReference.getElementById("httprescode"),
            "out": this.shadowRootReference.getElementById("outtextarea"),
            "mime": this.shadowRootReference.getElementById("selectMime").value,
            "headers": headers
        }
    }

    async execute(event){
        const inputs = this.getInputs();
        console.log(inputs);
        try {
            let result;
            if(methodes[inputs.method].body == "unused"){
                result = await fetch(inputs.url, {
                    method:inputs.method,
                    headers: inputs.headers
                });
            }else{
                result = await fetch(inputs.url, {
                    method:inputs.method,
                    body: inputs.body,
                    headers: inputs.headers
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
            if (newValue.headers){
                this.shadowRootReference.getElementById("headersarea").value = newValue.headers;
            }
        }
        this.shadowRootReference.firstChild.setAttribute("data-sheet-name", newValue);
                
    }      
}

customElements.define('req-custom', ReqElem);