new function() {
    'use strict'
    window.app = window.app || {};
    app.categories = app.categories || {};

    var apiUrl = "/api/v1"
    var $http = app.$http;

    app.categories.edit = function(button) {
        var $field = $(button).parents(".category");
        $(".value", $field).hide();
        $("input[name=name]", $field).show();
        $(".btn.edit", $field).hide();
        $(".btn.save", $field).show();
    };

    app.categories.addNew = function(button) {
        var $table = $(".table.categories tbody")
        var $newRow = $($.parseHTML($("#newRowTemplate").html()));
        $newRow.appendTo($table);
    };

    app.categories.save = function(button) {
        var $field = $(button).parents(".category");
        var isNew = $field.hasClass("category-new")
        var id = $("input[name=id]", $field).val();
        var name = $("input[name=name]", $field).val();

        var callback = function(data) {
            if (isNew) {
                $("input[name=id]", $field).val(data.id);
                $field.removeClass("category-new");
            }
            $(".value", $field).text(data.name);
            $(".value", $field).show();
            $("input[name=name]", $field).hide();
            $(".btn.edit", $field).show();
            $(".btn.save", $field).hide();
        };
        if (isNew)
        {
           $http.postJson(apiUrl + '/categories/', {name: name}).done(callback);
        } else
        {
            $http.putJson(apiUrl + '/categories/' + id, {name: name}).done(callback);
        }
    };

    app.categories.delete = function(button) {
        var $field = $(button).parents(".category");
        if ($field.hasClass("category-new")) {
            $field.remove();
        }
        else if (confirm('Willst du die Kategorie "' + $('.value', $field).text() + '" sicher löschen?'))
        {
            var categoryId = $("input[name=id]", $field).val();
            $http.delete(apiUrl + '/categories/' + categoryId)
                .done(function() {
                    $field.remove();
                });
        }
    };
}();