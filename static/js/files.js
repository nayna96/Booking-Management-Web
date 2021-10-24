function showFiles(dbName, collectionName, files_dt) {      
    files_dt.forEach ((file) =>
    {
      var docName = file.metadata["doc_name"];
      var _path = file.filename;
      switch (collectionName)
      {
        case "Project":
            switch (docName)
            {
                case "land_docs":
                    UpdateTable(dbName, "landDocs", _path)
                    break;
                case "agreements_doc":
                    UpdateTable(dbName, "agreementsDoc", _path)
                    break;
                case "pow":
                    UpdateTable(dbName, "Pow", _path)
                    break;
                case "dev_auth_approval":
                    UpdateTable(dbName, "devAuthApproval", _path)
                    break;
                case "rera_certificate":
                    UpdateTable(dbName, "reraCertificate", _path)
                    break;
                case "rent_receipt_doc":
                    UpdateTable(dbName, "rent_receiptDoc", _path)
                    break;
                default:
                    break;
            }
            break;
        case "Customer":
            switch (docName)
            {
                case "passport_photo":
                
                    break;
                case "aadhar_card":
                    UpdateTable(dbName, "aadharCard", _path)
                    break;
                case "pan_card":
                    UpdateTable(dbName, "panCard", _path)  
                    break;
                case "voter_id_card":
                    UpdateTable(dbName, "voterIDCard", _path)    
                    break;
                case "gst_doc":
                    UpdateTable(dbName, "gstDoc", _path)    
                    break;
                case "other_docs":
                    UpdateTable(dbName, "otherDocs", _path)                  
                    break;
                case "broker's_pan_card":
                    UpdateTable(dbName, "broker's_panCard", _path)
                    break;
                default:
                    break;
            }
            break;
        case "Bank":
            switch (docName)
            {
                case "list_docs":
                    UpdateTable(dbName, "listDocs", _path)
                    break;
                case "agreements_doc":
                    UpdateTable(dbName, "agreementsDoc", _path)
                    break;
                default:
                    break;
            }
            break;
        case "OrganisationMaster":
            switch (docName)
            {
                case "":
                    UpdateTable(dbName, "", _path)
                    break;
                default:
                    break;
            }
            break;
        default:
            break;
      }
        
    });
}
  
function UpdateTable(dbName, tableID, file){
    var table = document.getElementById(tableID);
    var n = table.rows.length;
    var row = table.insertRow(n);

    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);

    docname = table.parentElement.previousElementSibling.children[0].id;

    cell1.innerHTML = "<a href='#' onclick=viewFile('/view_file/" + dbName + "/" + docname + "/" + encodeURIComponent(file.replace("'", "\\'")) + "')>" + file + "</a>";
    cell2.innerHTML = "<a href='#' onclick=removeFile(event,'" + dbName + "','" + docname +  "')>remove</a>";
    /*var myList = document.getElementById(divID).getElementsByTagName('ul')[0];
    var myNewListItem = document.createElement('li');
    myNewListItem.innerHTML = 
    "<a href='#' onclick=viewFile('/view/" + dbName + "/" + encodeURIComponent(file) + "')>" + file + "</a>" +
    "<a href='#' class='alert-danger'>x</a>"
    myList.appendChild(myNewListItem);*/
}
  
function viewFile(_url){
    $.ajax({      
        url: _url
    });
}

function removeFile(e, dbName, docname){
    row = e.target.parentNode.parentNode;

    if(dbName != undefined && docname != undefined) {
        file_name = row.cells[0].children[0].innerText;

        _url = "/remove_file/" + file_name + "/" + docname;
        $.ajax({      
            url: _url
        });
    }

   row.remove();
}
  
function resetFileTable(){
    tables = $(".filesList");
    for(var i=0; i<tables.length; i++){
        $(tables[i]).empty();
    }
    /*var divs = document.getElementsByClassName("filesList");
    for(var i=0; i<divs.length; i++){
        divs[i].innerHTML = "<ul></ul>";
    }*/
}

function updateTable(file, tableID, toappend) {
    var table = document.getElementById(tableID);
    var input = document.getElementById(file);
  
    var children = "";
    for (var i = 0; i < input.files.length; ++i) {
        item = input.files.item(i).name;

        var tmppath = URL.createObjectURL(input.files.item(i));

        //row = "<tr><td>" + item + "</td><td><a href='#' onclick=removeFile(event)>remove</a></td></tr>";
        row = "<tr><td><a href='" + tmppath + "' target='_blank'>" + item + "</td><td><a href='#' onclick=removeFile(event)>remove</a></td></tr>";

        [found, index] = tableContains(tableID, item);
        
        if (!found){
            children += row;
        } 
        else {
            docname = table.parentElement.previousElementSibling.children[0].id;
            _url = "/remove_file/" + item + "/" + docname;
            $.ajax({      
                url: _url
            });
            table.rows[index].innerHTML = row;
        }
    }
    
    if(toappend == false){
    table.innerHTML = children;
    } else if(toappend == true){
    table.innerHTML += children;
    }
}
  
function tableContains(tableId, item){
    found = false;
    index = -1;

    var table = document.getElementById(tableId);
    var rows = table.rows;

    for (var i = 0; i < rows.length; i++) {
        cell = rows[i].cells[0];
        children = cell.children;

        if(children.length > 0){
            if(children[0].innerText == item){
                found = true;
                index = i;
                break;
            }
        } else {
            if(cell.innerText == item){
                found = true;
                index = i;
                break;
            }
        }
    }

    return [found, index];
}

function showImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
  
        reader.onload = function (e) {
            $('#pic')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };
  
        reader.readAsDataURL(input.files[0]);
    }
  }