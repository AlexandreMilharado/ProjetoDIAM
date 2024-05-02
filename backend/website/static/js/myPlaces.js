$(document).ready(function () {
  showHideElement($("#create-place-form"), $("#create-modal"));
});

function showHideElement($targetElement, $trigger, onEvent = "click") {
  $trigger.on(onEvent, function () {
    if ($targetElement.is(":visible")) $targetElement.fadeOut();
    else $targetElement.fadeIn();
  });
}
