$(document).ready(function () {
  let hearts = $(".heart");
  for (let i = 0; i < hearts.length; i += 2) {
    addFavoriteOrUnfavorite($(hearts[i]), $(hearts[i + 1]));
    setFavoritePlace($(hearts[i]), $(hearts[i + 1]));
  }
});

function addFavoriteOrUnfavorite(
  $targetElement1,
  $targetElement2,
  onEvent = "click"
) {
  $targetElement1.on(onEvent, function () {
    const element = $(this);
    $.ajax({
      url: `api/${$(this).attr("place")}/favorite`,
      headers: {
        "X-CSRFToken": $("#csrf-token").attr("content"),
      },
      method: "POST",
      success: function (_response) {
        $targetElement2.fadeIn();
        element.fadeOut();
      },
      error: function (xhr, _status, _error) {
        console.error(xhr.responseText);
      },
    });
  });

  $targetElement2.on(onEvent, function () {
    const element = $(this);
    $.ajax({
      url: `api/${$(this).attr("place")}/favorite`,
      headers: {
        "X-CSRFToken": $("#csrf-token").attr("content"),
      },
      method: "POST",
      success: function (_response) {
        $targetElement1.fadeIn();
        element.fadeOut();
      },
      error: function (xhr, _status, _error) {
        console.error(xhr.responseText);
      },
    });
  });
}

function setFavoritePlace($targetElement1, $targetElement2) {
  $.ajax({
    url: `api/${$targetElement1.attr("place")}/favorite`,
    method: "GET",
    success: function (response) {
      if (response.result) $targetElement1.fadeIn();
      else $targetElement2.fadeIn();
    },
    error: function (xhr, _status, _error) {
      console.error(xhr.responseText);
    },
  });
}
