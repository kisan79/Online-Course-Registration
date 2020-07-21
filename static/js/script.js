var btn = document.getElementById('btnSubmit');
function ajaxCall(inputId,url_path,msgId) {
            let textInput = document.getElementById(inputId).value;
            let msgSpan = document.getElementById(msgId);
            // console.log(textInput);
            var val = "inputValue="+textInput;


            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if(xhr.readyState === 4 && xhr.status === 200)
                {
                    var jsonObject = JSON.parse(xhr.responseText); //converting string to object
                    if(jsonObject['error']){
                        msgSpan.innerText = jsonObject.error;
                        msgSpan.style.color = "red";
                        btn.disabled = true;

                    }else {
                        msgSpan.innerText = jsonObject.success;
                        msgSpan.style.color = "green" ;
                        btn.disabled = false;

                    }
                    // console.log(xhr.responseText);
                    // console.log(typeof xhr.responseText); // string
                    // console.log(JSON.parse(xhr.responseText));
                    // console.log(typeof JSON.parse(xhr.responseText));
                }
            };

            xhr.open(method="POST",url=url_path,async=true);
            xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
            xhr.send(val);


        }