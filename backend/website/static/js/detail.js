$(document).ready(function() {
    $('.button-like')
      .bind('click', function(event) {
        
        $.ajax({
          url: `/api/${$(this).attr("place")}/favorite`,
          headers: {
            "X-CSRFToken": $("#csrf-token").attr("content"),
          },
          method: "POST",
          success: function (_response) {
            $(".button-like").toggleClass("liked");
          },
          error: function (xhr, _status, _error) {
            console.error(xhr.responseText);
          },
        });
      })
    handleSubmit($("#dropdown-options"));
});


function handleSubmit($form) {
 $form.submit(function (event) {
    event.preventDefault();
    if($(this).find('input[type="submit"][name="submeter"]:focus').val() == "Apagar")
      deletePlace();
    else 
      window.location.href = `/${place_id}/editPlace`;
  })
}

function deletePlace() {
  $.ajax({
    url: `/api/${place_id}/operationPlace`,
    method: "DELETE",
    headers: {
      "X-CSRFToken": $("#csrf-token").attr("content"),
    },
    success: function (_response) {
      window.location.href = "/";
    },
    error: function (xhr, _status, _error) {
      console.error(xhr.responseText);
    },
  });
}



  
