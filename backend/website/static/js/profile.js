$(document).ready(function () {

    $("#profile-photo").mouseout(function () {
        $(".custom-file-upload").css({ "visibility": "visible", "opacity": "0" });
        // $("#submit-photo").css({ "visibility": "visible", "opacity": "0" });
    });

    $("#profile-photo").mouseover(function () {
        $(".custom-file-upload").css({ "visibility": "visible", "opacity": "1" });
        $("#submit-photo").css({ "visibility": "visible", "opacity": "1" });
    });

    $("#profile-description").mouseover(function () {
        $("#edit-profile-description").css({ "visibility": "visible", "opacity": "1" })
    });

    $("#profile-description").mouseout(function () {
        $("#edit-profile-description").css({ "visibility": "visible", "opacity": "0" })
    });

    $(".custom-file-upload").click(async function () {
        $(this).hide();
        await new Promise(r => setTimeout(r, 1000));
        $("#submit-photo").show();
        $("#submit-photo").css({ "visibility": "visible", "opacity": "1" });
    });

    $("#profile-description input").each(function (index, input) {
        input.disabled = true;
    });

    $("#edit-profile-description").click(function () {
        $("#profile-description input").each(function (index, input) {
            input.disabled = false;
        });
        $(this).hide();
        $("#submit-profile-description").show();
        $("#submit-profile-description").css({ "visibility": "visible", "opacity": "1" });
    });

});
