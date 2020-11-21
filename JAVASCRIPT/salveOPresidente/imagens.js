let cenario;
let imagemDoAtor;
let imagemCorona;
let imagemCorona2;
let ImagemCorona3;
let somTrilha;
let somPontos;
let somColisao;



function preload(){
cenario = loadImage("imagens/estrada.png")
imagemDoAtor = loadImage("imagens/bolsonaro.png")
imagemCorona = loadImage("imagens/coronavirus1.png")
imagemCorona2 = loadImage("imagens/coronavirus2.png")
imagemCorona3 = loadImage("imagens/coronavirus3.png")
imagemCoronas = [imagemCorona3, imagemCorona3, imagemCorona3, imagemCorona3]
somTrilha = loadSound("som/trilha.mp3");
somPontos = loadSound("som/resfriadinho.mp3");
somColisao = loadSound("som/curadadoenca.mp3");
  
}
