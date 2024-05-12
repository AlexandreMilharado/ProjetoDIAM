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

    $(".remove-review").each(function() {
      bindRemoveReview($(this))
    })
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

function bindRemoveReview($target) {
  function removeReview(review_id) {
    $.ajax({
      url: `/api/${review_id}/operationReview`,
      method: "DELETE",
      headers: {
        "X-CSRFToken": $("#csrf-token").attr("content"),
      },
      success: function (_response) { window.location.href = `/${place_id}/detalhe`;},
      error: function (xhr, _status, _error) {
        console.error(xhr.responseText);
      },
    });
  }

  $target.click(function () {
    const reviewID = $(this).attr("review");
    removeReview(reviewID);
    console.log( $(`#review-${reviewID}`))
    $(`#review-${reviewID}`).remove();
  });
}

