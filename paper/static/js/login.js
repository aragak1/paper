$(document).ready(function () {
    $('#login').click(function () {
        var username = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();
        if (username == '' || password == '') {
            alert('用户名和密码都不能为空！');
        }
        else {
            $.post('/login', {
                'username': username,
                'password': password
            }, function (status) {
                if (status == 'success') {
                    location.href = '/';
                }
                else {
                    alert('登陆失败');
                }
            });
        }
    });
    $('#register').click(function () {
        var username = $('input[name="username"]').val();
        var email = $('input[name="email"]').val();
        var password = $('input[name="password"]').val();
        var re_password = $('input[name="re_password"]').val();


        if (username == '' || email == '' || password == '' || re_password == '') {
            alert('请填写全部选项！');
        }
        else
        {
            $.post('/register', {
                'username': username,
                'password': password,
                're_password': re_password,
                'email': email
            }, function (status) {
                if (status == 'success') {
                    alert('注册成功');
                    location.href = '/';
                }
                else {
                    alert(status);
                }
            });
        }
    });
});