export function showHideElement($targetElement, $trigger, onEvent = "click") {
  $trigger.on(onEvent, function () {
    if ($targetElement.is(":visible")) $targetElement.fadeOut();
    else $targetElement.fadeIn();
  });
}


