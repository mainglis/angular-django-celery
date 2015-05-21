'use strict';

// Declare app level module which depends on filters, and services
angular.module('report', ['djangular', 'report.filters', 'report.services', 'report.directives', 'report.controllers']).
  config(['$routeProvider', '$interpolateProvider', 'DjangoProperties', function($routeProvider, $interpolateProvider, DjangoProperties) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $routeProvider.when('/view1', {templateUrl: 'static/partials/partial1.html', controller: 'MyCtrl1'});
    $routeProvider.when('/view2', {templateUrl: 'static/partials/partial2.html', controller: 'MyCtrl2'});
    $routeProvider.when('/view3', {templateUrl: 'static/partials/partial3.html', controller: 'SecondController'});
    $routeProvider.otherwise({redirectTo: '/view1'});
  }]);

//    run([
//     '$http',
//     '$cookies',
//     function($http, $cookies) {
//         $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
//  }]);
//
//

