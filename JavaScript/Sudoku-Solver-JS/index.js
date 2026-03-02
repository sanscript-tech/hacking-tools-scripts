var sudoku = []

function checkRow(row, value){
	for(var i=0 ; i<9 ; i++){
		if(sudoku[row][i] === value)
			return false
	}
	return true
}

function checkCol(col, value){
	for(var i=0 ; i<9 ; i++){
		if(sudoku[i][col] === value)
			return false
	}
	return true
}

function checkBox(row, col, value){
	var columnCorner = col- (col%3) , rowCorner = row - (row%3);
	for(var i=0 ; i<3 ; i++){
		for(var j=0 ; j<3 ; j++){
			if(sudoku[i+rowCorner][j + columnCorner] === value)
				return false
		}
	}
	return true
}

function checkValue(row, col, value){
	if(checkRow(row, value) && checkCol(col, value) && checkBox(row, col, value))
		return true
	return false
}

function solveFinal(row, col){
	if(row === 8 && col === 9){
		return true
	}
	if(col === 9){
		row = row+1
		col = 0
	}
	if(sudoku[row][col] > 0){
		return solveFinal(row, col+1)
	}
	for(var i=1; i<=9; i++){
		if(checkValue(row, col, i)){
			sudoku[row][col] = i
			if(solveFinal(row, col+1)){
				return true;
			}
		}
		sudoku[row][col] = 0
	}
	return false
}

function myFunction(){
	s = document.getElementById("sudoku")
	for(var i=0 ; i<9 ; i++){
		var temp = []
		for(var j=0 ; j<9 ; j++){
			temp.push(parseInt(s.rows[i].cells[j].firstElementChild.value))
		}
		sudoku.push(temp)
	}
	console.log(sudoku);
	solveFinal(0, 0);
}

function myFunc2(){
	s2 = document.getElementById("sudoku")
	for(var i=0 ; i<9 ; i++){
		for(var j=0 ; j<9 ; j++){
			s2.rows[i].cells[j].firstElementChild.value = sudoku[i][j]
		}
	}
}

function myFunc3(){
	s3 = document.getElementById("sudoku")
	for(var i=0 ; i<9 ; i++){
		for(var j=0 ; j<9 ; j++){
			s3.rows[i].cells[j].firstElementChild.value = null
		}
	}
}

document.getElementById("solve").addEventListener('click', function() {myFunction(); })
document.getElementById("getResult").addEventListener('click', function(){ myFunc2(); })
document.getElementById("reset").addEventListener('click', function() {myFunc3(); })