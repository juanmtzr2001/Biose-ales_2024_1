//Variables
const int datos = 13;
float datosEntrada[datos]; // Vector de muestras entrada
float datosSalida[datos]; // Vector de muestras Salida
float datosSalidaCompleto[100]; // Senal salida
float CoeficientesNum[datos] = {0.0854, -1.0247, 5.6356, -18.7853, 42.2669, -67.6271, 78.8983, -67.6271, 42.2669, -18.7853, 5.6356, -1.0247, 0.0854}; 
float CoeficientesDen[datos] = {1, -7.1896, 24.3398, -51.0963, 73.8659, -77.2926, 59.9217, -34.6279, 14.7860, -4.54480, 0.9537, -0.1226, 0.0073};
uint8_t posE = 0;
uint8_t posS = 0;
uint8_t cont = 0;
bool bandera = false;

//Funcion
int sl_sign_c(float arreglo[], int longitud);

void setup() {
  Serial.begin(9600);
  for (int i = 0; i<datos;i++){
      datosEntrada[i] = analogRead(A0); 
      delay(10);
  }

}

void loop() {
  float salidaprim = 0; // Reiniciar el acumulador en cada iteración
  



  for (int i = 0; i < datos; i++) {
    for (int j = 0; j < datos; j++) {
      if (bandera == false) {
        salidaprim += datosEntrada[j] * CoeficientesNum[j]; 
      } else {
        if (datosSalida[j] != 0) { // Evitar división por cero
          salidaprim += (datosEntrada[j] * CoeficientesNum[j]) / (datosSalida[j] * CoeficientesDen[j]);
        }
      }
    } // Aquí cierra el segundo bucle for
    
    bandera = true;
    
    if (datosSalida[datos - 1] == 0) {
      datosSalida[i] = salidaprim;
    } else {
      datosSalida[posS] = salidaprim;
      posS += 1;
      if (posS == datos) {
        posS = 0;
      }
      datosSalidaCompleto[cont] = salidaprim;
      cont+=1;
      if (cont == 101) {
      cont = 0;
      }
    }
  } // Aquí cierra el primer bucle for
  
  if (datosEntrada[datos - 1] != 0) {
    datosEntrada[posE] = analogRead(A0);
    posE += 1;
    if (posE == datos) {
      posE = 0; 
    }
  }
  
  if (datosSalidaCompleto[99] != 0){ // Corregir el índice del arreglo
    int cambios_signo = sl_sign_c(datosSalidaCompleto, 100);
    //Serial.println(datosEntrada);
  }
  
}



int sl_sign_c(float arreglo[], int longitud) {
  int cambios_signo = 0;
  float diferencia_signo[longitud - 1];

  // Calcular la diferencia de signo
  for (int i = 0; i < longitud - 1; i++) {
    diferencia_signo[i] = arreglo[i + 1] - arreglo[i];
  }

  // Calcular el signo de la diferencia
  float signo_diferencia[longitud - 2];
  for (int i = 0; i < longitud - 2; i++) {
    if (diferencia_signo[i] > 0) {
      signo_diferencia[i] = 1;
    } else if (diferencia_signo[i] < 0) {
      signo_diferencia[i] = -1;
    } else {
      signo_diferencia[i] = 0;
    }
  }

  // Calcular el número de cambios de signo
  for (int i = 0; i < longitud - 2; i++) {
    if (signo_diferencia[i + 1] != signo_diferencia[i]) {
      cambios_signo++;
    }
  }

  return cambios_signo;
}






















