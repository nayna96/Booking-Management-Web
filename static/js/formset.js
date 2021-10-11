function addRow(className){
    var div = document.getElementsByClassName(className)[0],
        clone = div.cloneNode(true);
    var length = $("." + className).length;     
    var id = $("." + className)[length -1].id;
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
    }
    div.parentElement.appendChild(clone);

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