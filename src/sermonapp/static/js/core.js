new function() {
    'use strict'
    window.app = window.app || {};

    var $http = app.$http = function(options) {
        // Make absolute url.
        if (options.url && !options.url.indexOf('://') > -1) {
            options.url = trimSlashRight(window.UrlRoot) + '/' + trimSlashLeft(options.url);
        }
        return $.ajax(options)
            .fail(function(response, text) {
                alert("<strong>Es ist ein Fehler aufgetreten:</strong><br />" + text);
            });
    }

    $http.delete = function(url, options) {
        options = options || {};
        options.method = 'DELETE';
        options.url = url;
        return $http(options);
    }

    $http.get = function(url, options) {
        options = options || {};
        options.method = 'GET';
        options.url = url;
        return $http(options);
    }

    $http.getJson = function(url, options) {
        options = options || {};
        options.dataType = 'json';
        return $http.get(url, options);
    }

    $http.post = function(url, options) {
        options = options || {};
        options.method = 'POST';
        options.url = url;
        return $http(options);
    }

    $http.postJson = function(url, data, options) {
        options = options || {};
        options.dataType = 'json';
        options.contentType = "application/json; charset=utf-8";
        options.data = JSON.stringify(data);
        return $http.post(url, options);
    }

    $http.put = function(url, options) {
        options = options || {};
        options.method = 'PUT';
        options.url = url;
        return $http(options);
    }

    $http.putJson = function(url, data, options) {
        options = options || {};
        options.dataType = 'json';
        options.contentType = "application/json; charset=utf-8";
        options.data = JSON.stringify(data);
        return $http.put(url, options);
    }

    var alert = app.alert = function(message, state) {
        state = state || "danger";
        var $a = $(
            '<div class="alert alert-' + state + '">' + 
                message + 
                '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                    '<span aria-hidden="true">&times;</span>' +
                '</button>' +
            '</div>')
        $a.prependTo("#content")
    }

    function trimSlashRight(text) {
        return text.replace(/\/$/, '');
    }

    function trimSlashLeft(text) {
        return text.replace(/^\//, '');
    }

}();