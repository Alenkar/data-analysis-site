$(function () {
    $('login').submit(function (e) {
        let $this = $(this);

        e.preventDefault();

        if (Validate.check($this)) {
            $.post($this.attr('action'), $this.serialize(), function (data) {
                if (data.success == 'yep')
                    window.location.replace(data.redirect);
                else {
                    $this.removeClass('shake');

                    setTimeout(function () {
                        $this.addClass('shake');
                    }, 1);
                }
            }, 'json');
        }
    })
});
