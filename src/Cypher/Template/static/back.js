const butt = document.querySelectorAll(".opt");
const screen =  document.querySelector("#screen");
const inp =  document.querySelector("input");
const sub = document.querySelector("input[submit]");
const submer = document.querySelector("#submer")
const urlcatcher = document.querySelector("p");
let i=0;


console.log(inp);

screen.scrollTop = screen.scrollHeight - screen.clientHeight;

function Writer(renderbox, txt) {
   if(i < txt.length) {
     renderbox.innerHTML += txt.charAt(i);
     i++;
     setTimeout(function(){Writer(renderbox, txt);}, 200);
  }
  else{
    i = 0;
    // querybutton.disabled = false;
  }
}


function listen(item){
	item.addEventListener('click', (e) =>{
	prefix = "<br> jatin@linux:Cypher/home> "
	text = "nettacker -i "+ urlcatcher.innerHTML  +" -m "  + item.querySelector('.front').innerHTML
	screen.innerHTML += prefix
	Writer(screen, text)
  inp.value = item.querySelector('.front').innerHTML
	})
}

submer.addEventListener('click', () =>{
  sub.click();
})



butt.forEach(listen)
