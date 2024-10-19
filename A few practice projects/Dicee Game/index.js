let max = 6;
let min = 1;
let difference = max - min;
let randomNumber1 = Math.random() * difference;
randomNumber1 = randomNumber1 + min;
randomNumber1  = Math.round(randomNumber1);

var  randomDiceImage = "dice" + randomNumber1 + ".png"; 
var randomDiceSource = "images/" + randomDiceImage;



var max2 = 6;
var min2 = 1;
var difference2 = max2 - min2;
var randomNumber2 = Math.random() * difference2;
randomNumber2 = Math.floor(randomNumber2 + min2);

var randomDiceSource2 = "./images/dice" + randomNumber2 + ".png";

 



document.querySelector("img.img1").setAttribute("src" ,randomDiceSource);

document.querySelector("img.img2").setAttribute("src" ,randomDiceSource2);

if(randomNumber1 > randomNumber2){
    document.querySelector("h1").innerHTML = "Player 1 wins!"
}
else if (randomNumber1 < randomNumber2){
    document.querySelector("h1").innerHTML = "Player 2 wins!"
}
else if(randomNumber1 === randomNumber2) {
    document.querySelector("h1").innerHTML = "Draw!"
}
else {
    document.querySelector("h1").innerHTML = "Refresh Me"
}