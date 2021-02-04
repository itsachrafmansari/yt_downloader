function geturl() {
    var url = document.getElementById('url').value;
    var selected_type = document.getElementById('type');
    var type = selected_type.options[selected_type.selectedIndex].value;

    if (type == "v") {
        eel.video_dl(url);
    } else if (type == "p") {
        eel.playlist_dl(url);
    }
}