(function(){
  if(!window.bookmarklet) {
    bookmarklet_js = document.body.appendChild(document.createElement('script'));
    bookmarklet_js.src = 'https://social-app-uploads-bucket.s3.ap-northeast-2.amazonaws.com/js/bookmarklet.js';
    window.bookmarklet = true;
  }
  else {
    bookmarkletLaunch();
  }
})();
