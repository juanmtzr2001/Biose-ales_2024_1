datos = importdata('datos_EMG_sujeto9_3');
offset = mean(datos)-210;

[b, a] = butter(3, [50 200]/(1000/2));

% Filtrado pasa banda 
datos1 = filtfilt(b, a, datos);
datos1 = datos1 + offset;

datos_atipicos = find(datos1 > 350 | datos1 < 250);

% Elimina los datos atípicos
senal_sin_atipicos = datos1;
senal_sin_atipicos(datos_atipicos) = 300;

figure;
plot(senal_sin_atipicos);
title('Original');
%save('datos_EMG_sujeto9.mat', "senal_sin_atipicos")

%%

