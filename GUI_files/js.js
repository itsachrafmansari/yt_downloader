function geturl() {
    
    var url = document.getElementById("url").value;
    var type = url.includes("playlist");
    
    if (type) {
        eel.playlist_dl(url);
    } else {
        eel.video_dl(url);
    }
}
