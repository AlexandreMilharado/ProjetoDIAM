let cachedTags = [];
let lastTag = 0;

$(document).ready(function () {
  setTags();
  showHideElement($("#create-place-form"), $("#create-modal"));
  addTagHTML($("#add-tag"), $("#remove-tag"), $("#tag-group"));
});

function showHideElement($targetElement, $trigger, onEvent = "click") {
  $trigger.on(onEvent, function () {
    if ($targetElement.is(":visible")) $targetElement.fadeOut();
    else $targetElement.fadeIn();
  });
}

function addTag($targetElement, $trigger, onEvent = "click") {
  $trigger.on(onEvent, function () {
    if ($targetElement.is(":hidden")) $targetElement.fadeIn();
  });
}

function setTags() {
  $.ajax({
    url: `api/tags`,
    method: "GET",
    success: function (response) {
      cachedTags = response.result;
    },
    error: function (xhr, _status, _error) {
      console.error(xhr.responseText);
    },
  });
}

function addTagHTML($triggerOpen, $triggerClose, $target, onEvent = "click") {
  function createTagOptions(size, tags) {
    let html = "";
    for (let i = 0; i < size; i++)
      html += `<option value="${tags[i].id}">${tags[i].name}</option>`;
    return html + `<option value="None" selected="selected"></option>`;
  }

  $triggerOpen.on(onEvent, function () {
    if (lastTag <= cachedTags.length - 1) {
      $target.prepend(`<select name="tag-${lastTag}" id="tag-${lastTag}">
        ${createTagOptions(cachedTags.length, cachedTags)}
        </select>`);
      lastTag++;
    } else $triggerOpen.fadeOut();

    if ($triggerClose.is(":hidden")) $triggerClose.fadeIn();
  });

  $triggerClose.on(onEvent, function () {
    if (lastTag <= 1) $triggerClose.fadeOut();
    if ($triggerOpen.is(":hidden")) $triggerOpen.fadeIn();

    $(`#tag-${--lastTag}`).remove();
  });
}
