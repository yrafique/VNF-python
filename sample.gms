$gdxin input.gdx
$load CNFNameSet

Set i /1*3/;
Parameter c(i) /1 10, 2 20, 3 30/;
Variable x(i), z;
Positive Variable x;
Equation cost;

cost.. z =e= sum(i, c(i)*x(i));

Model simpleModel /all/;
Solve simpleModel using lp minimizing z;

$gdxout output.gdx
$unload z x
$gdxout
