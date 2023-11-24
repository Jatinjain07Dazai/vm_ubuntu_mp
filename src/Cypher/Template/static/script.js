function Writer(renderbox, txt) {
   if(i < txt.length) {
     document.querySelector(renderbox).innerHTML += txt.charAt(i);
     i++;
     setTimeout(function(){Writer(renderbox, txt);}, 200);
  }
}
/*                        Useful JS                                       */
const but = document.querySelector('#send');
const inp =  document.querySelector('input');
let i = 0
Writer( "p", "Frameworks, Languages, Loopholes ...");




but.addEventListener('click', () =>{
  document.querySelector('input[submit]').click();
});



