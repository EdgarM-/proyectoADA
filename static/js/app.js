var app = angular.module("akariApp",[]);

app.controller("akariController",[ '$scope', function($scope){
	$scope.created = false;
	$scope.matrix = [];
	$scope.matCreate = function()
	{
		$scope.created = true;
		for(var i=0; i< $scope.rows; i++) {
			$scope.matrix[i] = new Array($scope.cols);
		}
	};
	
	$scope.matFile = function()
	{
		console.log($scope.file);
	};
	
}]);