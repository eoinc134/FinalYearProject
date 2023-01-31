int: nc = 3;

var 1..nc: v1;
var 1..nc: v2;
var 1..nc: v3;
var 1..nc: v4;
var 1..nc: v5;
var 1..nc: v6;

constraint v1 != v2;
constraint v1 != v3;
constraint v1 != v5;
constraint v1 != v6;
constraint v2 != v3;
constraint v2 != v4;
constraint v2 != v6;
constraint v3 != v4;
constraint v3 != v5;
constraint v4 != v5;
constraint v4 != v6;
constraint v5 != v6;
solve satisfy;

output ["v1:\(v1) v2:\(v2) v3:\(v3) v4:\(v4) v5:\(v5) v6:\(v6)"];