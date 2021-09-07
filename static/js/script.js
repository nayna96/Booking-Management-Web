
function AccFunc(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}

  $(".sampleTable").fancyTable({
      sortColumn:0,
      pagination: true,
      perPage:10,
      globalSearch:true
  }); 

function show_modal(_url){
  var modal = document.getElementById("myModal");
  var span = document.getElementsByClassName("_close")[0];
  modal.style.display = "block";
  span.onclick = function() {
    modal.style.display = "none";
  }
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
  
  if(_url != undefined && _url.length > 0){
    $.ajax({
      type: "GET",
      url: _url,    
    });
  }
}      