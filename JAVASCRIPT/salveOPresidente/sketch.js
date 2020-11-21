
  


function setup() {
  createCanvas(600, 400);
  somTrilha.loop();
}



function draw() {
  background(cenario);
  mostraAtor();
  mostraCorona();
  movimentaCorona();
  movimentaAtor();
  infinito();
  verificaColisao();
  incluiPontos();
  marcaPonto();
  
  
  
 
  
  
}




