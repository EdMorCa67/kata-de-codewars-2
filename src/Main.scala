def multiTable(n: Int): String = {
  var resultado = ""
  var multiplo = 1
  
  while (multiplo <= 10){
    resultado += s"$multiplo * $n = ${multiplo * n}"
    
    
    if (multiplo < 10){
      resultado += "\n"
    }
    
    multiplo += 1
  }
  
  return resultado
}
