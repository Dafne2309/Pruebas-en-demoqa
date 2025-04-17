# Pruebas-en-demoqa
Este proyecto tiene como objetivo automatizar algunas pruebas en la página **https://demoqa.com/** utilizando Python y Selenium y desarrollandolo en el IDE Visual Studio.

##¿QUE PRUEBAS SE REALIZARON?

-Completar un formulario con datos ya definidos en el codigo(nombre, correo, dirección, etc.)
-Crear un archivo .txt y luego subirlo en la pagina correspondiente.
-Descargar un archivo automáticamente desde la misma página anterior.
-Manejar alertas emergentes: aceptar confirmaciones, enviar texto en un cuadro de prompt, etc.
-Generar reportes en formato HTML con los resultados de las pruebas realizadas.

##CONTENIDO DEL REPOSITORIO

-Código fuente de cada una de las pruebas.

-Códigos Python para generar archivos HTML con los resultados.

-Los archivos .html que muestran esos resultados.

-Este archivo README.md con la explicación del proyecto.

-Video demostrativo de como se ejecutan las pruebas en el IDE

##REQUISITOS PARA COMENZAR

-Tener Python 3.11 (o una versión más reciente) instalado.
-Tener Selenium instalado.

NOTA:Desde la versión Selenium 4.6.0, ya viene incluido el WebDriver, por lo que no es necesario instalarlo por separado.

Si por alguna razón no funciona, se puede consultar cómo instalar el WebDriver aquí:
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

##COMO EJECUTAR LAS PRUEBAS

Las pruebas fueron ejecutadas directamente desde Visual Studio Code, abriendo el archivo .py correspondiente y presionando el botón de "Run".

No es necesario usar comandos ni abrir una terminal.

VIDEO:

##QUE ES EL MODO HEADLESS

El modo headless es una forma de ejecutar pruebas sin que se abra el navegador en pantalla. El navegador trabaja en segundo plano.

En este proyecto, todas las pruebas se ejecutan en modo headless. Si alguien quiere ver el navegador funcionando, puede comentar o quitar esta línea en el código:chrome_options.add_argument("--headless")

##COMO SE MANEJARON LAS DESCARGAS DE LOS ARCHIVOS

Durante la prueba, se incluyó una parte donde el navegador descarga un archivo directamente desde la página. Como las pruebas están en modo headless, no se abre una ventana para que el usuario escoja la carpeta de descarga.
Para eso, el navegador ya está configurado para guardar automáticamente el archivo en una carpeta definida, sin pedir confirmación. El archivo se descarga sin intervención del usuario y se puede verificar en el código si efectivamente se descargó o no.
Esto se hace desde el código de prueba y no requiere abrir el navegador ni hacer clic manualmente.

