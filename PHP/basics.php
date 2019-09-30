<?php
echo "General Commands are not case Sensitive\n";
Echo "My first PHP script!\n";

echo "but Variables are \n";
$color = "blue";
$Color = "Red";
echo "color is " . $color . "\n";
echo "Color is " . $Color . "\n";

//This is a comment
# This is also a comment
/*
 * This is also a comment
*/

echo "\n\n";
 
$x = 5;
$y = 4;
echo $x + $y . "\n";
echo "What is $x \n";
echo "What is $x + $y \n";

echo "\n\n";
//Scope talk:

function test() {
	global $x;
	echo "Now I have access to x: $x \n";
	$GLOBALS['x'] ++; // This is superglobal, you can access x anywhere from the script
}

test();
echo "Now x is $x";


echo "\n\n";
//Static variables in PHP Persist after declarations in the function's scope
function testStatic() {
	static $z = 1;
	echo "$z \n";
	$z++;
}

testStatic();
testStatic();

// but z is still not in the global scope, just within the scope of testStatic


echo "\n\n";
//Types
echo "Native types: \n";
echo "string\n";
echo "int\n";
echo "float\n";
echo "bool ex. \"\$x = true\" \n";
echo "array ex. \"\$arr = array(1,2,3)\" \n";
echo "\t Not a type, but useful: \"var_dump(\$arr)\" returns object type and value\n";
echo "object See commented code below\n";

// class Car {
//     function Car() {
//         $this->model = "VW";
//     }
// }
// 
// // create an object
// $herbie = new Car();
// 
// // show object properties
// echo $herbie->model;
echo "Also, NULL exists as null\n";



// For loop:
	// for ( _ ; _ ; _ ) {}
// For each Loop:
	// foreach ( _ as _ ) {}
// while loop:
	// while() {}
// do while loop:
	// do {} while ();

?>
