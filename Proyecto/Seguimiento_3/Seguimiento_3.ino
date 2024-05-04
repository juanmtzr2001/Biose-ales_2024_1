const datos = 13;
float datosEntrada[datos]; //Vector de muestras entrada
float datosSalida[datos]; //Vector de muestras Salida
float CoeficientesNum[datos] = {0.0854, -1.0247, 5.6356, -18.7853, 42.2669, -67.6271, 78.8983, -67.6271, 42.2669, -18.7853, 5.6356, -1.0247, 0.0854}; 
float CoeficientesDen[datos] = {1, -7.1896,  24.3398, -51.0963, 73.8659, -77.2926,  59.9217, -34.6279, 14.7860, -4.54480,  0.9537, -0.1226,0.0073};
bool bandera = 0;
void setup() {
  // put your setup code here, to run once:
  for (int = i;i=datos-1;i++){
    
  }
  Serial.begin(9600);
  for (int i = 0; i=datos-1;i++){
    datosEntrada[i] = analogRead(A0); 
  }
}

void loop() {
  //En esta parte debo calcular la salida  
  for (int i = 0; i=datos-1;i++){
    for (int j = 0; j=datos-1;j++){
      if (bandera = 0){
        int salidaprim += datosEntrada[j]*coeficientesNum[j] 
      }
      else{
        int salidaprim += (datosEntrada[j]*coeficientesNum[j])/(datosSalida[j]*coeficientesDen[j])
      }
    }
    bandera = 1;
    datosSalida[i] = salidaprim
  }
  
  // Voy a hacer una funcion en la que renueve los coeficientes para solo llamarla


}
