function showFiles(dbName, collectionName, files_dt) {      
    files_dt.forEach ((file) =>
    {
      var docName = file.metadata["doc_name"];
      var _path = file.filename;
      switch (collectionName)
      {
        case "Project":
            break;
        case "Customer":
            switch (docName)
            {
                case "passport_photo":
                
                    break;
                case "aadhar_card":
                    UpdateDiv(dbName, "aadharCard", _path)
                    break;
                case "pan_card":
                    UpdateDiv(dbName, "panCard", _path)  
                    break;
                case "voter_id_card":
                    UpdateDiv(dbName, "voterIDCard", _path)    
                    break;
                case "gst_doc":
                    UpdateDiv(dbName, "gstDoc", _path)    
                    break;
                case "other_docs":
                    UpdateDiv(dbName, "otherDocs", _path)                  
                    break;
                default:
                    break;
            }
            break;
        case "Bank":
            break;
        default:
            break;
      }
        
    });
}
  
function UpdateDiv(dbName, divID, file){
    var myList = document.getElementById(divID).getElementsByTagName('ul')[0];
    var myNewListItem = document.createElement('li');
    myNewListItem.innerHTML = "<a href='#' onclick=viewFile('/view/" + dbName + "/" + encodeURIComponent(file) + "')>" + file + "</a>"
    myList.appendChild(myNewListItem);
}
  
function viewFile(_url){
    $.ajax({      
        url: _url
    });
}
  
function resetFileDiv(id){
    var divs = document.getElementsByClassName("filesList");
    for(var i=0; i<divs.length; i++){
        divs[i].innerHTML = "<ul></ul>";
    }
}

function updateList(file, divID, toappend) {
    var input = document.getElementById(file);
    var div = document.getElementById(divID);
  
    var children = "";
    for (var i = 0; i < input.files.length; ++i) {
      item = input.files.item(i).name;
      if (!listContains(divID, item)){
        children += '<li>' + item + '</li>';
      }
    }
  
    if(toappend == false){
      div.innerHTML = '<ul>'+children+'</ul>';
    } else if(toappend == true){
      var myList = document.getElementById(divID).getElementsByTagName('ul')[0];
      myList.innerHTML += children;
    }
  }
  
function listContains(divId, item){
    $("#" + divId + "ul li").each((id, elem) => {
      if (elem.innerText == item) {
        found = true;
      }
    });
}