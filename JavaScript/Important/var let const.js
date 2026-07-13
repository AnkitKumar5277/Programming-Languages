// var
var a = 10;
console.log(a);
var a = 20;
a = 30;
console.log(a);
// 10
// 30

// let
let b = 20;
console.log(b);
// let b = 30; // -> failed cannot redeclare
b = 40;
console.log(b);
// 20
// 40

// const
const c = 30;
console.log(c); // 30
// const c = 40; // ❌ Error: Cannot redeclare
// c = 50;        // ❌ Error: Cannot reassign

