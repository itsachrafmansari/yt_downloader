function geturl() {

    var url = document.getElementById("url").value;

    var is_playlist = url.includes("playlist");
    if (is_playlist) {
        eel.yt_playlist_dl(url);
    } else {
        eel.yt_video_dl(url);
    }
}
