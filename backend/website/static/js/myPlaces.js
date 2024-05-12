import { addTagHTML, showHideElement } from "./utils.js";

$(document).ready(function () {
  setTags();
  showHideElement($("#create-place-form"), $("#create-modal"));
  addTagHTML($("#add-tag"), $("#remove-tag"), $("#tag-group"));
});

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
