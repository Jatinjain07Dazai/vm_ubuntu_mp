const detailsElement = document.querySelector('.details-example');


detailsElement.addEventListener('toggle', event => {
    if (event.target.open) {
        console.log('open');
    } else {
        console.log('closed');
    }
});


var id = setInterval(function(){
  fetch('../sig/')
  .then( data => {
    if(data.ok){
      link.style.display = 'block';
      clearInterval(id);
      }
    else{
      
      console.log("wait");
    }
  })
}
, 5000);