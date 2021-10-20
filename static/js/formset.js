function addRow(e, className){
    if(e != undefined){
        index = Number(e.target.parentElement.parentElement.id.split("-")[1])
    } else{
        index = -1;
    }
    
    var length = $("." + className).length;   

    var div = document.getElementsByClassName(className)[0],
        clone = div.cloneNode(true);

    if(index == length - 1 || e == undefined){
        div.parentElement.appendChild(clone);
    } else{
        div.parentElement.insertBefore(clone, div.parentElement.children[index + 1]);
    }

    resetIndex(className, div.parentElement.children);

    for(var i=0; i<clone.children.length; i++){
        element = clone.children[i];
        input = element.children[0];
        if(input != undefined){
            input.value = "";
        }
    }

    /*var id = $("." + className)[length -1].id;
    var num = Number(id.split("-")[1]) + 1;
    var OuterId = id.split("-")[0] + "-" + num;
    clone.id = OuterId;
    for(var i=0; i<clone.children.length; i++){
        element = clone.children[i];
        input = element.children[0];
        if(input != undefined){
            id = input.id;
            Name = OuterId  + id.split("0")[1];
            input.setAttribute('name', Name);
            input.id = Name;
            input.value = "";
        }
    }*/
    
    nofields = Number(document.getElementById(className + "-fields").value);
    document.getElementById(className + "-fields").value = (nofields + 1).toString(); 
}

function removeRow(e){
    if (e.target == undefined){
        var div = e.parentElement.parentElement;
    } else{
        var div = e.target.parentElement.parentElement;
    }
    
    var className = div.classList[1];
    if($("." + className).length > 1){
        
        children = div.parentElement.children;
        div.remove();
        resetIndex(className, children);
        nofields = Number(document.getElementById(className + "-fields").value);
        document.getElementById(className + "-fields").value = (nofields - 1).toString(); 
    }
}

function resetFormSet(){
    formsets = ["fs1", "fs2"]
    formsets.forEach((formset)=>{
        divs = document.getElementsByClassName(formset);
        var result = Object.keys(divs).map((key) => [Number(key), divs[key]]);
        for(var i=1; i<result.length; i++){
            result[i][1].remove();
        }
    });
}

function resetIndex(className, children){
    for(var i=0; i<children.length; i++){
        outer_id = className + "-" + i;
        children[i].id = outer_id
        els = children[i].children;
        for(var j=0; j<els.length; j++){
            input = els[j].children[0];
            parts = input.id.split("-");
            id = outer_id + "-" + parts[2];
            input.id = id;
            input.name = id;
        }
    }
}