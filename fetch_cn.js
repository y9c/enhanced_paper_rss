function a() {
    if (document.getElementById('__tr_display')) {
            return;
        }
    window.__tr_api = 'da18b76ad944a10529b06a145c693b02';
    window.__tr_base = 'http://www.zhaowenxian.com/';
    var d = document,
        s = d.createElement('script');
    s.setAttribute('type', 'text/javascript');
    s.setAttribute('src', __tr_base + 'js?y=' + (Math.random()));
    d.body.appendChild(s);
}

a();
