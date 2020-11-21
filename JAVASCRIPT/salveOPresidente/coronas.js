let xCoronas = [600, 600, 600, 600, 600, 600]
let yCoronas = [40, 100, 270, 210, 270, 318]
let velocidades = [2,2.5,4,3,2,5]


//corona

var tCorona= 30;

function mostraCorona(){
  
  for (let i =0; i < imagemCoronas.length;i = i+1){
   
  image(imagemCoronas[i], xCoronas[i], yCoronas[i], tCorona, tCorona);
   }
}

function movimentaCorona(){
  for (let i = 0; i < imagemCoronas.length; i = i + 1){
   xCoronas[i] -= velocidades[i];
  }

}

function infinito(){
  for (let i = 0; i < imagemCoronas.length; i = i + 1){
     if (limiteTela(xCoronas[i])) {
   xCoronas[i] = 600
     
     }
  } 
}

function limiteTela(xCoronas){
 return xCoronas < -30

}
