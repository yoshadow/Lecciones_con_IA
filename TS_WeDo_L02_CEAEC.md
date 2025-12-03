| Lección | Título de la lección | Identificador   | Nivel         | Objetivo                                                                 | Habilidades                                      | Materiales                                                     |
|---------|----------------------|-----------------|--------------|---------------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------|
| 2       | Pateador             | TS_WeDo_L02     | Primaria Baja| Activar un mecanismo de patada cuando el robot detecta un objeto cercano. | Pensamiento crítico, experimentación, trabajo colaborativo | Kit de robótica educativa con ladrillos y Software WeDo 2.0 |

---

## Contextualizo

Lucía y Diego estaban jugando fútbol en el recreo.  
Diego intentó patear la pelota hacia la portería, pero se cansó muy rápido.

—“Ojalá tuviéramos un robot que pateara por nosotros cuando la pelota se acercara”, dijo Diego, jadeando.  
—“¡Sí! Un robot que espere quieto y, cuando la pelota esté cerca, ¡patee solo!”, respondió Lucía emocionada.

En clase de robótica, la maestra les contó que existen robots que **reaccionan a cosas que suceden a su alrededor**, como cuando un objeto se acerca.  
Lucía pensó: “Si nuestro robot pudiera sentir que la pelota está cerca, podríamos hacer que dé una patada fuerte o suave, según lo que queramos”.

Hoy tú vas a construir un **robot pateador** que usa **engranajes y un sensor de proximidad** para reaccionar cuando un objeto se pone enfrente.  
Así aprenderás cómo un robot puede **“ver” con un sensor y mover su pierna con engranajes** para patear justo en el momento correcto.

**Instrucción para el ilustrador (IA de imagen, estilo animación 3D):**  
Crear una ilustración en estilo animación 3D donde aparezcan dos niños, Lucía y Diego, en un patio de escuela. Frente a ellos hay una portería pequeña y un robot hecho de piezas tipo LEGO con una pierna levantada listo para patear una pelota. La pelota está justo frente al robot, cerca de un pequeño sensor. Los niños están sorprendidos y señalando al robot mientras éste parece a punto de patear. Fondo con escuela y cielo despejado.

Piensa un momento:  
- ¿Cómo sabrá el robot que la pelota está cerca para dar la patada?  
- ¿Crees que la patada será igual de fuerte si cambiamos los engranajes?  
- ¿Para qué te serviría controlar la fuerza de la patada en un partido robótico?

---

## Examino

**Observa con atención la imagen del proyecto que vas a armar.**

Mira cómo está formado el robot pateador:  
- Localiza la **pierna** o parte que hará la patada.  
- Busca dónde están los **engranajes** que conectan el motor con la pierna.  
- Identifica el **sensor de proximidad** (el que “ve” los objetos cercanos).

Imagina:  
- ¿Qué parte se moverá más rápido cuando el motor gire?  
- ¿En qué lugar crees que debes poner la pelota para que el robot la patee?

**Nombre del archivo:** Imagen_Pateador_1a.png

---

## Armo

Sigue los pasos a continuación para armar tu proyecto.  
Coloca cada pieza con cuidado y asegúrate de que todo quede bien conectado.

[Carrusel]

Colocar un carrusel con el paso a paso en imágenes para armar el modelo “Pateador”.  
Obtener las imágenes de la carpeta de instructivo correspondiente al proyecto.

---

## Exploro

Ha llegado el momento de poner manos a la obra.  
Ya tienes tu **pateador** armado, ahora vamos a descubrir cómo funciona su **sensor de proximidad** y sus **engranajes** para que pueda reaccionar y dar una patada cuando algo se acerque.

---

### 1) Primera actividad: Conozco cómo reacciona el pateador

En esta actividad vas a aprender cómo tu robot **detecta un objeto** y cómo usa los **engranajes** para mover la pierna.

#### a) Conecto y preparo el programa

1. Conecta el **motor** y el **sensor de proximidad** al hub de WeDo 2.0.  
2. Abre el **software WeDo 2.0** en la tableta o computadora.  
3. Crea un **nuevo proyecto** y ponle el nombre: “Pateador”.  

Ahora vas a crear un programa sencillo para que el robot patee cuando algo esté cerca.

Ejemplo de programa (descrito de forma general):  
1. Bloque de **inicio** (para comenzar el programa).  
2. Bloque que **lee el sensor de proximidad**.  
3. Condición: “Si el objeto está cerca, entonces…”  
4. Bloque para **encender el motor** por unos segundos para que la pierna patee.  
5. Bloque para **detener el motor**.

El docente te mostrará en la pantalla los bloques exactos que usarás.

#### b) Pruebo el sensor de proximidad

El **sensor de proximidad** ayuda al robot a “sentir” si algo está cerca o lejos.

- Coloca tu mano o una pelota **frente al sensor**, a poca distancia.  
- Pide al profesor que ejecute el programa.  
- Observa: ¿La pierna se mueve cuando el objeto está cerca?  
- Ahora, retira el objeto y vuelve a probar, pero esta vez **más lejos**.

Piensa:  
- ¿El robot patea igual cuando el objeto está lejos?  
- ¿En qué punto el sensor deja de detectar el objeto?

#### c) Observo los engranajes

Los **engranajes** son ruedas con dientes que se encajan unas con otras.  
Sirven para **transmitir el movimiento** del motor a la pierna del robot.

Mira tu robot pateador:  
- Localiza el **engranaje unido al motor**.  
- Observa el **engranaje conectado a la pierna**.

Cuando el motor gira:  
- Un engranaje hace girar al otro.  
- Ese giro hace que la pierna se mueva y dé la patada.

Concepto clave:  
- Si usamos **engranajes de diferentes tamaños**, la **fuerza y la velocidad** de la patada pueden cambiar.  
- Un engranaje pequeño moviendo uno grande puede hacer una patada **más fuerte pero más lenta**, o al revés, según cómo estén colocados.

Preguntas para pensar:  
- ¿Qué pasaría si los engranajes fueran más grandes?  
- ¿Cómo crees que cambia la patada si el engranaje del motor es pequeño y el de la pierna es grande?

---

### 2) Segunda actividad (Reto): Ajusto la fuerza de la patada

Ahora vas a realizar un pequeño reto para cambiar **qué tan fuerte o suave** patea tu robot.

**Reto:**  
Lograr que tu robot pueda dar **dos tipos de patada**:  
- Una **patada suave** para que la pelota no vaya muy lejos.  
- Una **patada fuerte** para que la pelota viaje más lejos.

#### a) Modifico la parte mecánica (engranajes)

Con la ayuda del docente:  
1. Cambia el tamaño de **al menos uno de los engranajes** del mecanismo de la pierna.  
   - Prueba usar un engranaje **más grande** o **más pequeño**.  
2. Vuelve a colocar bien las piezas para que los dientes de los engranajes sigan encajando.  
3. Coloca la pelota frente al sensor.

Ahora prueba:  
- ¿La patada se siente más fuerte o más suave que antes?  
- ¿La pelota llega más lejos o menos lejos?

#### b) Ajusto el programa (si aplica en tu grupo)

Pide al docente que te permita cambiar un parámetro en el programa:  
1. Modifica el **tiempo** que el motor está encendido (por ejemplo, menos segundos para una patada suave y más segundos para una patada fuerte).  
2. Vuelve a ejecutar el programa con la pelota frente al sensor.

Observa:  
- ¿Qué cambio hace el tiempo en el movimiento de la pierna?  
- ¿Qué combinación funciona mejor: engranajes cambiados + tiempo del motor?

Preguntas detonadoras:  
- ¿Qué combinación de engranajes y tiempo te da la **patada más fuerte**?  
- ¿Cómo te ayuda el sensor a que la patada salga en el **momento justo** sin que tú toques el robot?  
- ¿En qué situación de la vida real serviría tener un robot que patea solo cuando algo se acerca?

---

## Concluyo

Responde las siguientes preguntas de opción múltiple.  
Rodea o marca la respuesta correcta.

1. ¿Para qué sirve el **sensor de proximidad** en tu robot pateador?  
   a) Para cambiar el color de las piezas.  
   b) Para detectar cuándo un objeto está cerca y activar la patada.  
   c) Para guardar los programas en el motor.  
   **Respuesta correcta: b)**

2. ¿Qué hacen los **engranajes** en el robot?  
   a) Solo decoran el modelo para que se vea más grande.  
   b) Conectan el sensor con la tableta.  
   c) Transmiten el movimiento del motor hasta la pierna que patea.  
   **Respuesta correcta: c)**

3. Si cambias el tamaño de los engranajes, ¿qué puede cambiar en la patada del robot?  
   a) El color del robot.  
   b) La fuerza y la velocidad de la patada.  
   c) El idioma del programa.  
   **Respuesta correcta: b)**

4. ¿Qué tiene que pasar para que el robot patee la pelota?  
   a) Que el sensor detecte que la pelota está lo suficientemente cerca.  
   b) Que el robot esté apagado.  
   c) Que alguien mueva la pierna con la mano.  
   **Respuesta correcta: a)**

5. ¿Qué aprendiste sobre los robots que reaccionan a estímulos?  
   a) Que solo sirven para jugar fútbol.  
   b) Que pueden usar sensores para saber qué pasa a su alrededor y actuar solos.  
   c) Que no necesitan programas para funcionar.  
   **Respuesta correcta: b)**

---

## Actividades complementarias (para el alumno)

1. **Actividad complementaria 1 (20 min):  
   “Distancias de disparo”**  
   - Coloca una marca en el piso a corta distancia de la portería.  
   - Programa o ajusta tu robot para que dé una **patada suave** que llegue justo a esa marca.  
   - Después, coloca otra marca más lejos e intenta ajustar engranajes o tiempo del motor para que la pelota llegue a la segunda marca sin pasarse.

2. **Actividad complementaria 2 (20 min):  
   “Penales robóticos en equipo”**  
   - Forma parejas o pequeños equipos.  
   - Cada equipo ajusta los engranajes o el tiempo del motor para lograr **tres tiros de penal**: uno muy corto, uno mediano y uno largo.  
   - Registra en una hoja qué cambios hiciste en el robot para cada tipo de tiro.

---

# Instrucciones para el profesor

### Contextualizo
- Presenta la historia de Lucía y Diego en voz alta, usando entonación para mantener la atención.  
- Pregunta al grupo:  
  - “¿Han visto máquinas que se mueven solas cuando algo se acerca, como puertas automáticas?”  
  - “¿Cómo creen que un robot podría saber que una pelota está cerca?”  
- Muestra (en pantalla o impreso) la ilustración generada según el prompt sugerido.  
- Conecta la historia con el objetivo de la lección: explicar que construirán un **pateador robótico que reacciona a estímulos** usando un sensor de proximidad y engranajes.

### Examino
- Proyecta o reparte la imagen **Imagen_Pateador_1a.png** del modelo completamente armado.  
- Di explícitamente: **“Observa con atención la imagen del proyecto que vas a armar.”**  
- Pide a los alumnos que señalen visualmente:  
  - Dónde creen que está el sensor de proximidad.  
  - Qué piezas podrían ser los engranajes.  
  - Qué parte será la pierna que patea.  
- Solicita predicciones orales:  
  - “¿Qué parte creen que se moverá cuando el motor gire?”  
  - “¿Dónde pondrías la pelota para que el robot la patee?”

### Armo
- Organiza a los alumnos en parejas o pequeños equipos, según la cantidad de kits disponibles.  
- Indica que sigan el carrusel de imágenes del instructivo paso a paso, sin saltarse pasos.  
- Supervisa que:  
  - Los motores y el sensor de proximidad se conecten en los puertos correctos del hub.  
  - Los engranajes queden correctamente engranados (dientes bien alineados).  
- Da apoyo adicional a quienes tengan dificultades motrices o de lectura de imágenes.  
- Antes de pasar a “Exploro”, revisa rápidamente cada modelo para asegurar que la pierna esté libre para moverse.

### Exploro – Primera actividad
- Guía la conexión del hub con el dispositivo (tableta o computadora) usando WeDo 2.0.  
- En una pantalla grande, modela la creación del programa básico:  
  - Bloque de inicio.  
  - Lectura del sensor de proximidad.  
  - Condición para activar el motor cuando el objeto esté cerca.  
  - Duración del motor y detención.  
- Acompaña a los alumnos a replicar el programa en sus dispositivos.  
- Indica que