'use strict';

angular.module('project', ['ngRoute', 'firebase'])
 
.value('fbURL', 'https://crackling-fire-5203.firebaseio.com/')
 
.factory('Projects', function($firebase, fbURL) {
  return $firebase(new Firebase(fbURL));
})
 
.config(function($routeProvider) {
  $routeProvider
    .when('/', {
      controller:'ListCtrl',
      templateUrl:'views/list.html'
    })
    .when('/details/:projectId', {
      controller:'EditCtrl',
      templateUrl:'views/details.html'
    })
    .when('/edit/:projectId', {
      controller:'EditCtrl',
      templateUrl:'views/edit.html'
    })
    .when('/new', {
      controller:'CreateCtrl',
      templateUrl:'views/edit.html'
    })
    .when('/about', {
      templateUrl:'views/about.html'
    })
    .when('/contactus', {
      templateUrl:'views/contactus.html'
    })
    .otherwise({
      redirectTo:'/'
    });
})
 
.controller('ListCtrl', function($scope, Projects) {
  $scope.projects = Projects;
})
 
.controller('CreateCtrl', function($scope, $location, $timeout, Projects) {
  $scope.save = function() {
    Projects.$add($scope.project, function() {
      $timeout(function() { $location.path('/'); });
    });
  };
})
 
.controller('EditCtrl',
  function($scope, $location, $routeParams, $firebase, fbURL) {
    var projectUrl = fbURL + $routeParams.projectId;
    $scope.project = $firebase(new Firebase(projectUrl));
 
    $scope.destroy = function() {
      $scope.project.$remove();
      $location.path('/');
    };
 
    $scope.save = function() {
      $scope.project.$save();
      $location.path('/');
    };
});