new function() {
    'use strict'
    window.app = window.app || {};
    app.categories = app.categories || {};

    function addCategory(name) {
        return 0;
    }

    function updateCategory(id, name) {

    }

    function deleteCategory(id) {

    }

    app.categories.edit = function(button) {
        var $field = $(button).parents(".category");
        $(".value", $field).hide();
        $("input[name=name]", $field).show();
        $(".btn.edit", $field).hide();
        $(".btn.save", $field).show();
    }

    app.categories.save = function(button) {
        var $field = $(button).parents(".category");
        var isNew = $field.hasClass("category-new")
        if (isNew) {
            var name = $("input[name=name]", $field).val();
            var id = addCategory(name);
            $("input[name=id]", $field).val(id);
            $field.removeClass("category-new");
        }
        $(".value", $field).text($("input[name=name]", $field).val());
        $(".value", $field).show();
        $("input[name=name]", $field).hide();
        $(".btn.edit", $field).show();
        $(".btn.save", $field).hide();
    }

    app.categories.delete = function(button) {
        var $field = $(button).parents(".category");
        if ($field.hasClass("category-new") ||
            confirm('Willst du die Kategorie "' + $('.value', $field).text() + '" sicher löschen?'))
        {
            $field.remove();
        }
    }

    app.categories.addNew = function(button) {
        var $table = $(".table.categories tbody")
        var $newRow = $($.parseHTML($("#newRowTemplate").html()));
        $newRow.appendTo($table);
    }
}();