window.onload = function() {
    var image = document.getElementById('image');
    var canvas = document.getElementById('canvas');
    var video = document.getElementById('video');
    var allow = document.getElementById('allow');
    var context = canvas.getContext('2d');

    if('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices){
console.log("Let's get this party started")
}

    navigator.GetUserMedia({video: true, audio: false})
        .then(stream => {
        video.srcObject = stream
        }, function () {
            console.log('что-то не так с видеостримом или пользователь запретил его использовать :P');
        });

    console.log("Init")
}

var start = function() {
    // запрашиваем разрешение на доступ к поточному видео камеры

};

var snapshot = function () {
    context.translate(canvas.width, 0);
    context.scale(-1, 1);
    context.drawImage(video, 0, 0,
                      video.width, video.height);
    // Отправка на сервер
    // var base64dataUrl = canvas.toDataURL('image/png');
    // var img = new Image();
    // img.src = base64dataUrl;
    // window.document.body.appendChild(img);
}
