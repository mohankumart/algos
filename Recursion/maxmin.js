/**
 * Find max and min from given array of numbers
 */

var numbers = [5000,9,25,2,34,5000,12,0,200,35];

function recursive(i, j, numbers){
	var max,min,k;
	if(i-j == 0){
		max = numbers[i];
		min = numbers[i];
	}else if(i == j-1){
		if(numbers[i] > numbers[j]){
			max = numbers[i];
			min = numbers[j];
		}else{
			max = numbers[j];
			min = numbers[i];
		}
	}else{
		k = Math.floor((i + j)/2);
		maxmin1 = recursive(i, k, numbers);
		maxmin2 = recursive(k+1, j, numbers);
		if(maxmin1[0] > maxmin2[0]){
			max = maxmin1[0]
		}else{
			max = maxmin2[0]
		}
		if(maxmin1[1] < maxmin2[1]){
			min = maxmin1[1]
		}else{
			min = maxmin2[1]
		}
	}
	return [max, min];
}

function findMaxMin(){
	var start = 0;
	var end = numbers.length - 1;
	var maxmin = recursive(start, end, numbers);
	console.log("max----->"+maxmin[0]);
	console.log("min----->"+maxmin[1]);
}


findMaxMin()

