$(document).ready(function () {
  setTagsEvents($("#tag-list-create"));
});

function setTagsEvents($target) {
  $.ajax({
    url: `api/tags`,
    method: "GET",
    success: function (response) {
      const tags = response.result;
      $target.prepend(createTags(tags.length, tags));
      setListennersTags(tags);
    },
    error: function (xhr, _status, _error) {
      console.error(xhr.responseText);
    },
  });
}

function createTags(size, tags) {
  let html = "";
  for (let i = 0; i < size; i++)
    html += ` <li id="container-tag-${tags[i].id}" class="tag" style="display: flex">
                <form id="update-tag-form-${tags[i].id}" style="display: inherit" >
                    <input id="tag-${tags[i].id}" class="tag-update" value="${tags[i].name}">
                </form>
                <button id="remove-tag-${tags[i].id}" class="btn-svg" type="button"><svg fill="#000000" viewBox="-3.5 0 19 19" xmlns="http://www.w3.org/2000/svg" class="cf-icon-svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M11.383 13.644A1.03 1.03 0 0 1 9.928 15.1L6 11.172 2.072 15.1a1.03 1.03 0 1 1-1.455-1.456l3.928-3.928L.617 5.79a1.03 1.03 0 1 1 1.455-1.456L6 8.261l3.928-3.928a1.03 1.03 0 0 1 1.455 1.456L7.455 9.716z"></path></g></svg></button></li>`;
  return html;
}

function setListennersTags(tags) {
  for (let i = 0; i < tags.length; i++) {
    setDeleteTag(tags[i].id);
    setWidth($(`#tag-${tags[i].id}`));
    setStyllingTag($(`#tag-${tags[i].id}`));
    setUpdateTag(tags[i].id);
  }
}

function setDeleteTag(tag_id) {
  function deleteTag() {
    $.ajax({
      url: `api/${tag_id}/operationTag`,
      method: "DELETE",
      headers: {
        "X-CSRFToken": $("#csrf-token").attr("content"),
      },
      success: function (_response) {
        $(`#container-tag-${tag_id}`).remove();
      },
      error: function (xhr, _status, _error) {
        console.error(xhr.responseText);
      },
    });
  }

  $(`#remove-tag-${tag_id}`).on("click", function () {
    deleteTag();
  });
}

function setUpdateTag(tag_id) {
  function updateTag() {
    $.ajax({
      url: `api/${tag_id}/operationTag`,
      method: "POST",
      headers: {
        "X-CSRFToken": $("#csrf-token").attr("content"),
      },
      data: {
        name: $(`#tag-${tag_id}`).val(),
      },
      success: function (_response) {},
      error: function (xhr, _status, _error) {
        console.error(xhr.responseText);
      },
    });
  }

  $(`#update-tag-form-${tag_id}`).submit(function (event) {
    event.preventDefault();
    updateTag();
  });
}

function setStyllingTag($tag) {
  $tag.on("input", function () {
    setWidth($(this));
  });
}

function setWidth($tag) {
  $tag.css({
    width: $tag.val().replace(/\s+/g, "").length + 3 + "ch",
  });
}
