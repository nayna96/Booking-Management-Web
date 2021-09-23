function addRow(className){
    var div = document.getElementsByClassName(className)[0],
        clone = div.cloneNode(true);     
    var id = div.parentElement.lastElementChild.getAttribute('id');
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
    var parentDiv = e.target.parentElement.parentElement;
    if(parentDiv.childElementCount > 1){
        var div = e.target.parentElement;
        div.remove();
        
        className = e.target.parentElement.classList[0];
        nofields = Number(document.getElementById(className + "-fields").value);
        document.getElementById(className + "-fields").value = (nofields - 1).toString(); 
    }
}

function resetFormSet(){
    formsets = ["fs1", "fs2"]
    formsets.forEach((formset)=>{
        divs = document.getElementsByClassName(formset);
        for(i=1; i<divs.length; i++){
            divs[i].remove();
        }
    });
}

$('').on('keypress',function(e) {
    if(e.which == 13) {
        
    }
});