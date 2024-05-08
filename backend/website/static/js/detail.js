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
  });

  
