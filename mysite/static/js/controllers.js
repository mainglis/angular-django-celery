'use strict';

/* Controllers */

angular.module('blog.controllers', []).
    controller('MyCtrl1', [function() {
        console.log('well i am in controller 1');
    }])
    .controller('MyCtrl2', [function() {
        console.log('and now in controller 2');
    }]);