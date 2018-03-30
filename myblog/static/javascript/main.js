'use strict';
var jq = jQuery.noConflict();
jq(function () {
    jq('img').on('click', function () {
        jq(this).slideToggle()
    })
})