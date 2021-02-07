var selected = "youtube";

function edit_reso(x, y) {
    var l = document.getElementsByClassName(x);
    var len=l.length;
    for (var i=0; i < len ; i++) {
        l[i].style.display = y;
    }
}

function youtube() {
    selected = "youtube";
    document.getElementById('desc').innerHTML = "Enter the video/playlist url below :";
    document.getElementById('button').style.background = "var(--yt)";
    document.getElementById('form').style.borderColor = "var(--yt)";
    document.getElementById('resolutions').style.borderColor = "var(--yt)";
    document.getElementById('resolutions').style.color = "var(--yt)";
    document.getElementById('resolutions').style.display = "unset";
    document.getElementById('instagram').classList.remove("selected");
    document.getElementById('facebook').classList.remove("selected");
    document.getElementById('youtube').classList.add("selected");
    
    edit_reso("yt_reso" , "block");
    edit_reso("fb_reso" , "none");
}

function facebook() {
    selected = "facebook";
    document.getElementById('desc').innerHTML = "Enter the video url below :";
    document.getElementById('button').style.background = "var(--fb)";
    document.getElementById('form').style.borderColor = "var(--fb)";
    document.getElementById('resolutions').style.borderColor = "var(--fb)";
    document.getElementById('resolutions').style.color = "var(--fb)";
    document.getElementById('resolutions').style.display = "unset";
    document.getElementById('instagram').classList.remove("selected");
    document.getElementById('youtube').classList.remove("selected");
    document.getElementById('facebook').classList.add("selected");
    edit_reso("fb_reso" , "block");
    edit_reso("yt_reso" , "none");
}

function instagram() {
    selected = "instagram";
    document.getElementById('desc').innerHTML = "Enter your video/IGTV url below :";
    document.getElementById('button').style.background = "var(--ig)";
    document.getElementById('form').style.borderColor = "var(--ig)";
    document.getElementById('resolutions').style.borderColor = "var(--ig)";
    document.getElementById('resolutions').style.color = "var(--ig)";
    document.getElementById('facebook').classList.remove("selected");
    document.getElementById('youtube').classList.remove("selected");
    document.getElementById('instagram').classList.add("selected");
    document.getElementById('resolutions').style.display = "none";
}

function geturl() {

    var url = document.getElementById("url").value;

    if (selected == "youtube") {
        var type = url.includes("playlist");
        if (type) {
            eel.yt_playlist_dl(url);
        } else {
            eel.yt_video_dl(url);
        }
    }
    else if (selected == "facebook") {
        eel.fb_video_dl(url);
    }
    else if (selected == "instagram") {
        eel.ig_video_dl(url);
    }
}
