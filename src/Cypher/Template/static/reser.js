function color_box(list){
var colors = []
var col = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for(var i=0; i <= list.length; i++){
  color = "#" + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))]
          + col[Math.round((Math.random() *10))];
  colors.push(color);  
}
return colors;
}



deck = document.querySelector(".info-cont");
const link = document.querySelector("#network-page");
var cards = deck.children;
var color = color_box(cards);
for(i=0; i < cards.length; i++){
    cards[i].style.backgroundColor = color[i];
}



