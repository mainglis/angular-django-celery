'use strict';
alert('i do get to report appjs');

// Declare app level module which depends on filters, and services
angular.module('report', ['report.filters', 'report.services', 'report.directives', 'report.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/view1', {templateUrl: 'static/partials/partial1.html', controller: 'MyCtrl1'});
    $routeProvider.when('/view2', {templateUrl: 'static/partials/partial2.html', controller: 'MyCtrl2'});
    $routeProvider.otherwise({redirectTo: '/view1'});
  }]);

  angular.module('report.filters', []).
  filter('interpolate', ['version', function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/mg, version);
    }
  }]);

