# SwinIR-Restore

README.txt

Este archivo describe dos modalidades de empleo del algoritmo SwinIR-Restore. La primera modalidad aborda el uso del algoritmo en su forma original, como lo define el autor. La segunda modalidad detalla el uso de una aplicación web desarrollada para ser accesible a usuarios con diversos niveles de competencia tecnológica.

Ambos métodos comparten los siguientes pasos iniciales:

5.1. Descargar el proyecto:

Para descargar el proyecto, acceda al siguiente enlace:
https://github.com/FranCamposC/SwinIR-Restore.git

Una vez en la página, haga clic en el botón "Download ZIP" en el desplegable que se muestra.

Una vez descargado, haga clic derecho sobre el archivo ZIP y seleccione la opción "Extraer aquí". Esto descomprimirá el proyecto. Para abrir el proyecto, utilice Visual Studio Code. Puede iniciar Visual Studio Code haciendo clic derecho en la carpeta extraída y seleccionando "Abrir con Code", o abriendo la carpeta directamente desde Visual Studio Code seleccionando "File" en la barra de menú y luego "Open Folder". También puede arrastrar y soltar la carpeta en la ventana principal de Visual Studio Code.

Una vez que el proyecto esté abierto, abra una terminal integrada en Visual Studio Code. Puede hacerlo seleccionando "View" en la barra de menú y luego "Terminal", o mediante la combinación de teclas "Ctrl+Shift+ñ". En la terminal, escriba el siguiente comando y presione Enter:

pip install -r requirements.txt

Esto instalará todas las dependencias enumeradas en el archivo "requirements.txt". Dependiendo de la cantidad de paquetes y la velocidad de la conexión a Internet, puede llevar algún tiempo completar la instalación de todos los requisitos.

A partir de aquí, se explicarán los dos métodos mencionados anteriormente:

5.2. Primer método (método original del algoritmo):

Crearemos una carpeta en el directorio que hemos extraído que se llamará “testsets” y una carpeta dentro de ella que se llamará “RealSRSet+5images”. Pondremos dentro las imágenes que queramos restaurar. Abriremos la consola y ejecutaremos el siguiente comando:

Abra la consola y ejecute el siguiente comando:

python main_test_swinir.py --task real_sr --scale 4 --model_path model_zoo/swinir/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth --folder_lq testsets/RealSRSet+5images --tile 400

Una vez que el comando haya terminado de ejecutarse, vaya a la carpeta "static" y haga clic en la nueva carpeta que se ha creado. Dentro de esta carpeta encontrará la imagen restaurada.

5.3. Segundo método (recomendado):

Abra la carpeta del proyecto con cualquier IDE, por ejemplo, Visual Studio Code.

Dentro del IDE, abra la consola y ejecute el siguiente comando:

python app.py runserver

Abra el navegador y vaya a la siguiente URL (por defecto): http://127.0.0.1:5000

![Página web](https://github.com/FranCamposC/SwinIR-Restore/blob/main/imagenesReadme/image4.PNG)

Le daremos a 'Cargar imagen' y automáticamente después, pulsaremos en 'Mejorar imagen'. Una vez hecho esto, esperaremos a que concluya el algoritmo y nos aparecerá la foto para que la podamos descargar:

![Descargar imagen](https://github.com/FranCamposC/SwinIR-Restore/blob/main/imagenesReadme/image5.png)

