function AccFunc(id) {
  var x = document.getElementById(id);
  if(x.classList.contains("w3-show")){
    x.classList.remove("w3-show");
    x.classList.add("w3-hide");
  } else if(x.classList.contains("w3-hide")){
    x.classList.remove("w3-hide");
    x.classList.add("w3-show");
  }
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
  
function show_modal(){
  resetFileDiv();
  resetFormSet();
  document.getElementById("form").reset();

  var modal = document.getElementById("myModal");
  var span = document.getElementsByClassName("_close")[0];
  modal.style.display = "block";
  span.onclick = function() {
    modal.style.display = "none";
  }
  /*window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }*/
  document.getElementById("btn").value = "Save";
  document.getElementById("btn").name = "Save";    
} 

function getMaxDate(){
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1; //January is 0!
  var yyyy = today.getFullYear();

  if (dd < 10) {
    dd = '0' + dd;
  }

  if (mm < 10) {
    mm = '0' + mm;
  } 
      
  today = yyyy + '-' + mm + '-' + dd;
  
  return today
}

function formatDate(dateString){
  var dateParts = dateString.split("-");
  if(dateParts.length == 1){
    dateParts = dateString.split("/");
  }
  var dateObj = new Date(+dateParts[2], dateParts[1] - 1, +dateParts[0]); 
  var dd = String(dateObj.getDate()).padStart(2, '0');
  var mm = String(dateObj.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = dateObj.getFullYear();

  date = yyyy + '-' + mm + '-' + dd;
  return date;
}

function maxdateValidation(e){
  today = getMaxDate();
  if(e.target.value > today){
      e.target.value = "";
      alert("Date is greater than max date");
  } 
}

//Move to next tab on Enter
document.addEventListener('keydown', function (event) {
  if (event.key === "Enter" && event.target.nodeName === 'INPUT') {
    var form = event.target.form;
    var index = Array.prototype.indexOf.call(form, event.target);
    form.elements[index + 1].focus();
    event.preventDefault();
  }
});

function requiredValidation(){
  var requiredElements = document.getElementById("form").querySelectorAll("[required]");

  var s = "";
  for (var i = 0; i < requiredElements.length; i++) {
    var e = requiredElements[i];
    s += e.value.length? "" : e.id + ": Not Filled" + "\n";
  }

  if(s.length > 0){
    alert(s);
    return false;
  }

  return true;
}

$(document).ready(function() {
  $("#fancyTable").fancyTable({
    sortColumn:0,
    pagination: true,
    perPage:10,
    globalSearch:true
  });

  //ALLSTRING
  $('body').on('input', '.allstring', function() {
    this.value = this.value.toUpperCase();
    this.value = this.value.replace(/[^a-zA-Z .]/g, '').replace(/(\..*)\./g, '$1');
  });

  //ALLCAPS STRING
  $('body').on('input', '.allcaps', function() {
    this.value = this.value.toUpperCase();
  });
  
  //ALLNUMS 
  $('body').on('input', '.allnums', function() {
    this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');
  });

  $("#project_name").change(function () {
    var block_url = $("#form").attr("data-blocks-url");
    var project_name = $(this).val();

    $.ajax({
      url: block_url,
      data: {
        'project_name': project_name
      },
      success: function(result){
          $("#block_name").html(result);
      }
    });
  })

  $("#block_name").change(function () {
    var floor_url = $("#form").attr("data-floors-url");
    var project_name = $("#project_name").val();
    var block_name = $(this).val();

    $.ajax({
      url: floor_url,
      data: {
        'project_name': project_name,
        'block_name': block_name
      },
      success: function(result){
          $("#floor_no").html(result);
      }
    });
  })

});
