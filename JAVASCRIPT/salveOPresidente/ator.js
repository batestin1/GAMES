//ator

var xAtor = 85;
var yAtor = 330;
let colisao = false;
let meusPontos = 0;
let computadorPontos =0;


function mostraAtor() {
  image(imagemDoAtor, xAtor, yAtor, 140, 60);
}

function movimentaAtor() {

  if (keyIsDown(UP_ARROW)) {
    yAtor -= 1;
  }
  if (keyIsDown(DOWN_ARROW)) {
    yAtor += 1;
  }
  if (keyIsDown(RIGHT_ARROW)) {
    xAtor += 1;
  }

  if (keyIsDown(LEFT_ARROW)) {
    xAtor -= 1;
  }

}



function verificaColisao() {

  for (let i = 0; i < imagemCoronas.length; i = i + 1) {
    colisao = collideRectCircle(xCoronas[i], yCoronas[i], tCorona, tCorona, xAtor, yAtor, 85, 340)
  }
  if (colisao) {
    colidiu();
    function colidiu() {
      somPontos.play();
    yAtor = 330;
  
      
  }
  }

  }


function incluiPontos(){
  textAlign(CENTER);
textSize(25);
text(meusPontos, 505, 25);
}



function marcaPonto(){
if (yAtor < 15){
meusPontos += 1;
  somColisao.play();
  yAtor = 330;
  
}
  

}