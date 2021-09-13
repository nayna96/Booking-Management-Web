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

$(".sampleTable").fancyTable({
  sortColumn:0,
  pagination: true,
  perPage:10,
  globalSearch:true
});

$(function() {
  $('input[type=text]').keyup(function() {
      this.value = this.value.toUpperCase();
  });
});

function setGender(e, id){
  var salutation = e.target.value;
  if(salutation == "MR."){
    document.getElementById(id).value = "MALE";
  } else if(salutation == "MRS." || salutation == "MS."){
    document.getElementById(id).value = "FEMALE";
  }
}

function copyPresentAddress(){
  var checkBox = document.getElementById("copy_present");
  if (checkBox.checked == true){
    $("#pe_addLine1").val($("#pr_addLine1").val());
    $("#pe_addLine2").val($("#pr_addLine2").val());
    $("#pe_state").val($("#pr_state").val());
    $("#pe_district").val($("#pr_district").val());
    $("#pe_city").val($("#pr_city").val());
    $("#pe_pincode").val($("#pr_pincode").val());
  } else {
    $("#pe_addLine1").val("");
    $("#pe_addLine2").val("");
    $("#pe_state").val("");
    $("#pe_district").val("");
    $("#pe_city").val("");
    $("#pe_pincode").val("");
  }
}

function copyFrom(e){
  var val = e.target.value;
  $("#contact_p_phone_no").val($("#mobile_no").val());
  if(val == "CUSTOMER"){
    $("#contact_p_salutation").val($("#customer_salutation").val());
    $("#contact_p_name").val($("#customer_fname").val() + " " + $("#customer_mname").val() + " " + $("#customer_lname").val()); 
  } else if(val == "CO-OWNER"){
    $("#contact_p_salutation").val($("#co-owner_salutation").val());
    $("#contact_p_name").val($("#co-owner_fname").val() + " " + $("#co-owner_mname").val() + " " + $("#co-owner_lname").val());
  } else if(val == ""){
    $("#contact_p_salutation").val("");
    $("#contact_p_name").val("");
    $("#contact_p_phone_no").val("");
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

function show_modal(){
  resetDiv();
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