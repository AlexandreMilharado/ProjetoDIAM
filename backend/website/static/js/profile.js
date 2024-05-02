$(document).ready(function () {

    $("#profile-photo").mouseout(function () {
        $("#edit-profile-photo").hide();
    });

    $("#profile-photo").mouseover(function () {
        $("#edit-profile-photo").show();
    });

    $("#profile-description").mouseover(function () {
        $("#edit-profile-description").show();
    });;

    $("#profile-description").mouseout(function () {
        $("#edit-profile-description").hide();
    });

    $("#profile-description input").each(function (index, input) {
        input.disabled = true;
    });

    $("#edit-profile-description").click(function () {
        $("#profile-description input").each(function (index, input) {
            input.disabled = false;
        });
        $("#submit-profile-description").show();
        $(this).remove();
        // $(this).hide();
    });

});
