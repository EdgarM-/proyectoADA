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
	
	var solverFour = function()
	{
		var len = $scope.matrix.length;
		for (var i = len - 1; i >= 0; i--) {
			for (var j = len - 1; j >= 0; j--) {
				if($scope.matrix[i][j])
				{
					
				}
			}
		}
	};

	$scope.solveAkari = function()
	{
		console.log($scope.matrix);
	};

}]);