# MSFP2
[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212177-ship-it/MSFPO2)

# Práctica 2: modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información del estudiante

Gael Sebastian Andrade Arellano;23212177[l23212177@tijuana.tecnm.mx]

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Calcular la función de transferencia de los casos hipotenso, normotenso e hipertenso.
2. Establecer el sistema de ecuaciones diferenciales ordinarias lineales de primer orden.
3. Emular la respuesta del circuito Windkessel en Simulink/Simscape.
4. Simular la respuesta de los modelos matemáticos en Simulink/MATLAB ante la misma señal aleatoria de excitación.
5. Sintonizar las ganancias de un controlador PID para reducir el error entre la respuesta de cada caso y la respuesta del individuo normotenso.
6. Obtener la respuesta en lazo abierto y en lazo cerrado con el controlador PID en Python con la función de transferencia.
7. Relacionar los elementos del modelo con las estructuras fisiológicas mediante un diagrama biológico.

## Descripción detallada del sistema

El modelo Windkessel de cuatro elementos representa un sistema de segundo orden que modeliza, de manera simplificada, la dinámica del sistema arterial. La presión se representa como voltaje y el flujo sanguíneo como corriente. La impedancia característica Z representa la región proximal del sistema arterial, la capacitancia C la distensibilidad arterial total, la resistencia R la resistencia periférica y la inductancia L la inertancia arterial. El objetivo del modelo eléctrico es predecir la respuesta dinámica de la presión Pp(t) asociada con la distensibilidad arterial a la presión arterial de entrada Pa(t). Se comparan tres casos que difieren únicamente en el valor de C: hipotenso, normotenso (referencia) e hipertenso. Para cada caso hipotenso e hipertenso se diseña un controlador PID que reduce la diferencia con la respuesta normotensa. La práctica se realiza exclusivamente mediante experimentación in silico y con fines académicos.

Palabras clave: Modelo Windkessel; Sistema cardiovascular; Controlador PID; Modelo matemático; Simulaciones numéricas.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB [.mlx y .pdf].
2. Modelo de Simulink [.slx].
3. Archivo de Python [.py].
4. Señal de entrada utilizada en las simulaciones [.xlsx].
5. Imágenes con los parámetros de los controladores.
6. Figuras de las simulaciones en Python y Matlab [.pdf].
7. Diagrama biológico del sistema cardiovascular.

## Referencias

[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: [https://biomath.xyz/course/](https://biomath.xyz/course/)

[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.
