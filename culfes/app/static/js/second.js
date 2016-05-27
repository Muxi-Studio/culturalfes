var body = document.getElementsByTagName('body')[0],
	captcha = document.getElementById('captcha_container'),
    btn = document.getElementById('vote_btn'),
    confirm = document.getElementById('c_confirm_btn'),
    close = document.getElementById('submit_close')
    flash = document.getElementById('submit_flash');
	btn.addEventListener("click",function(){
		body.style.overflow="hidden";
		captcha.style.display="block";
	})
	confirm.addEventListener("click",function(){
		captcha.style.display="none";
		body.style.overflow="visible";
	})
	close.addEventListener("click",function(){
		flash.style.display="none"
	})