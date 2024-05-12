import { addTagHTML, showHideElement } from "./utils.js";

$(document).ready(function () {
  console.log(placeID);
  setTags();
  showHideElement($("#create-place-form"), $("#create-modal"));
  addTagHTML($("#add-tag"), $("#remove-tag"), $("#tag-group"));
});

function setTags() {
  $.ajax({
    url: `/api/tags`,
    method: "GET",
    success: function (response) {
      cachedTags = response.result;
      loadHTMLTag($("#tag-group"));
    },
    error: function (xhr, _status, _error) {
      console.error(xhr.responseText);
    },
  });
}

function loadHTMLTag($target) {
  function loadTagOptions(selected_id, tags) {
    let html = "";
    for (let i = 0; i < tags.length; i++)
      html += `<option value="${tags[i].id}" ${
        tags[i].id == selected_id ? `selected = "selected"` : ""
      }>${tags[i].name} </option>`;
    return html;
  }
  function getTagsPlace() {
    $.ajax({
      url: `/api/${placeID}/getBestTags`,
      method: "GET",
      success: function (response) {
        addHTML(response.result);
        if (lastTag > 0) $("#remove-tag").fadeIn();
      },
      error: function (xhr, _status, _error) {
        console.error(xhr.responseText);
      },
    });
  }
  function addHTML(tagsPlace) {
    for (let i = 0; i < tagsPlace.length; i++) {
      $target.prepend(`<select name="tag-${lastTag}" id="tag-${lastTag}">
        ${loadTagOptions(tagsPlace[i].id, cachedTags)}
        </select>`);
      lastTag++;
    }
  }

  getTagsPlace();
}
