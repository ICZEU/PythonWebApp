$.expr[":"].contains = $.expr.createPseudo(function(arg) {
    return function( elem ) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});

$(function() {
    'use strict'

    $(".searchbox input").focus();

    $(".searchbox input").keyup(function() {
        var $sb = $(this);
        var text = $sb.val();

        if (text)
        {
            $(".speakers .speaker").hide();
            $(".speakers .speaker").has("h4:contains('" + text + "')").show();
        }
        else
        {
            $(".speakers .speaker").show();
        }
        
    });
});