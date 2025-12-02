| Lección | 2 |
|--------|---|
| Id Nimbus | TS_WeDo_L02 |
| Título | Pateador |
| Nivel | Primaria Baja |
| Objetivo | Activar un mecanismo de patada cuando el robot detecta un objeto cercano. |
| Habilidades | Pensamiento crítico, experimentación, trabajo colaborativo. |
| Materiales | Kit de robótica educativa con ladrillos y Software WeDo 2.0 |

---

## Contextualizo

Lucía y Bruno estaban jugando fútbol en el recreo.  
A Bruno le encantaba patear el balón, pero a veces se cansaba muy rápido.

—“Ojalá tuviéramos un robot que nos ayudara a patear el balón cuando se acerque”, dijo Bruno, respirando agitado.  
—“¡Eso sería increíble! Un robot que vea el balón y ¡pum!, lo patee solo”, respondió Lucía emocionada.  

Entonces recordaron que en clase de robótica podían construir modelos con sensores.  
—“Si usamos un sensor que detecte cuando el balón está cerca, el robot podría patearlo sin que lo toquemos”, pensó Lucía.  
—“Así aprenderíamos cómo los robots reaccionan cuando algo se acerca, como si tuvieran reflejos”, añadió Bruno.

Hoy tú vas a construir un robot “pateador” que reacciona cuando detecta un objeto cercano.  
Este conocimiento te sirve para crear máquinas que respondan solas a lo que pasa a su alrededor, como puertas que se abren cuando alguien se acerca o robots que evitan chocar.

**Instrucción para el ilustrador (prompt IA, estilo animación 3D):**  
“Ilustración en estilo animación 3D de dos niños de primaria, Lucía y Bruno, en un patio de escuela con una portería de fútbol. Lucía sostiene un balón y Bruno mira emocionado un pequeño robot hecho de bloques tipo LEGO con una pierna mecánica levantada, listo para patear el balón. El ambiente es colorido, alegre y escolar.”

Piensa un momento:  
- ¿Cómo sabrá tu robot que el balón está cerca?  
- ¿Qué crees que pasará cuando el sensor detecte el objeto?  
- ¿Te gustaría que la patada fuera suave o muy fuerte? ¿Por qué?

---

## Examino

**Observa con atención la imagen del proyecto que vas a armar.**

Mira cómo está formada la parte que patea, dónde está colocado el sensor de proximidad y cómo se conectan los engranajes al motor.  
Imagina qué piezas del kit podrías usar para construir la pierna que patea y cómo se moverá cuando el motor gire.

**Nombre del archivo:** Imagen_Pateador_1a.png  
(Imagen del modelo “Pateador” completamente armado, visto de lado, mostrando claramente el sensor de proximidad, el motor y el sistema de engranajes que mueve la pierna.)

---

## Armo

Sigue los pasos a continuación para armar tu proyecto.  
Coloca cada pieza con cuidado y asegúrate de que todo quede bien conectado.

[Carrusel]

Colocar un carrusel con el paso a paso en imágenes para armar el modelo “Pateador”.  
Obtener las imágenes de la carpeta **Instructivo** correspondiente a esta lección.

---

## Exploro

Ha llegado el momento de poner manos a la obra.  
Ya tienes tu robot “Pateador” armado, ahora vamos a descubrir cómo funciona su sensor y sus engranajes para que pueda reaccionar y patear cuando algo se acerca.

### Actividad 1: ¿Cómo patea tu robot cuando detecta algo?

En esta actividad aprenderás cómo el sensor de proximidad y los engranajes hacen que tu robot patee cuando un objeto se acerca.

1. **Conecta tu modelo al software WeDo 2.0.**  
   - Asegúrate de que el motor y el sensor de proximidad estén bien conectados al Smarthub.  
   - En la tableta o computadora, abre WeDo 2.0 y enlaza tu Smarthub.

2. **Observa el sensor de proximidad.**  
   - El sensor de proximidad “ve” si hay un objeto cerca, como tu mano o una pelota pequeña.  
   - Cuando algo se acerca a cierta distancia, el sensor envía una señal al programa.

3. **Crea un programa sencillo.**  
   Pide apoyo a tu docente si lo necesitas. En WeDo 2.0:  
   - Coloca un bloque de inicio (por ejemplo, “al presionar reproducir”).  
   - Agrega un bloque que use el **sensor de proximidad** (bloque que detecta cuando algo está cerca).  
   - Después, agrega un bloque de **motor** para que gire cuando el sensor detecte el objeto.  
   - Ajusta el motor para que gire en un solo sentido durante un tiempo corto (por ejemplo, 1 segundo).

4. **Prueba el funcionamiento.**  
   - Coloca tu mano o un objeto pequeño frente al sensor, a unos pocos centímetros.  
   - Observa qué hace la pierna del robot cuando el sensor detecta el objeto.  
   - Retira el objeto y vuelve a acercarlo varias veces.

5. **Piensa en lo que está pasando.**  
   - El **sensor de proximidad** detecta que algo está cerca.  
   - El programa recibe esa información y **activa el motor**.  
   - El motor hace girar los **engranajes**, y estos mueven la pierna que patea.  
   - Los engranajes sirven para **transmitir el movimiento** del motor a la pierna.

**Preguntas para reflexionar:**

- ¿Qué sucede con la pierna cuando acercas un objeto al sensor?  
- ¿Qué pasa si el objeto está muy lejos del sensor?  
- ¿La pierna se mueve igual cada vez que el sensor detecta algo?  
- ¿Por qué crees que necesitamos engranajes y no solo el motor?

---

### Actividad 2 (Reto): ¿Puedes cambiar la fuerza de la patada?

Ahora que tu robot ya patea cuando detecta un objeto, vas a hacer un reto rápido:  
modificar los engranajes o la programación para que la patada sea **más fuerte** o **más suave**.

1. **Observa los engranajes de tu robot.**  
   - Identifica cuál engrane está conectado directamente al motor.  
   - Identifica cuál engrane mueve la pierna que patea.

2. **Reto mecánico (engranajes):**  
   - Cambia el tamaño de uno de los engranajes:  
     - Prueba usar un engrane **más grande** conectado al motor.  
     - Luego prueba usar un engrane **más pequeño** conectado a la pierna.  
   - Vuelve a probar el robot acercando un objeto al sensor.

3. **Reto de programación (opcional, si hay tiempo):**  
   - Sin cambiar los engranajes, modifica el bloque del motor:  
     - Aumenta la **potencia** del motor (por ejemplo, de 5 a 8).  
     - Disminuye la potencia (por ejemplo, de 8 a 3).  
   - Observa cómo cambia la fuerza de la patada.

4. **Compara los resultados.**  
   - ¿Cuándo la patada fue más fuerte?  
   - ¿Cuándo fue más suave?  
   - ¿Qué combinación te gustó más para que el robot patee como tú quieres?

**Preguntas detonadoras:**

- ¿Qué pasa con la pierna cuando usas un engrane más grande en el motor?  
- ¿Y cuando usas un engrane más pequeño en la pierna?  
- ¿Cómo cambia la patada cuando subes o bajas la potencia del motor en el programa?  
- Si quisieras que el robot patee muy suave, ¿qué tipo de engranajes y potencia elegirías?

---

## Concluyo

Responde las siguientes preguntas de opción múltiple.  
Rodea o marca la respuesta correcta.

1. ¿Para qué sirve el **sensor de proximidad** en tu robot “Pateador”?  
   a) Para que el robot cambie de color.  
   b) Para detectar cuando un objeto está cerca. ✅  
   c) Para que el robot haga sonidos.

2. ¿Qué ocurre cuando el sensor detecta un objeto cercano y el programa está bien hecho?  
   a) El robot se apaga solo.  
   b) El motor se activa y la pierna patea. ✅  
   c) El robot se queda quieto.

3. ¿Qué función tienen los **engranajes** en el mecanismo de patada?  
   a) Decorar el robot para que se vea bonito.  
   b) Guardar la energía del robot.  
   c) Transmitir el movimiento del motor a la pierna que patea. ✅

4. Si quieres que la patada sea **más fuerte**, ¿qué cambio podría ayudar?  
   a) Bajar la potencia del motor en el programa.  
   b) Usar una combinación de engranajes que haga girar más rápido la pierna. ✅  
   c) Apagar el sensor de proximidad.

5. Un robot que patea cuando detecta un objeto cercano nos ayuda a entender que:  
   a) Los robots solo se mueven si los empujamos con la mano.  
   b) Los robots pueden reaccionar a estímulos usando sensores y programas. ✅  
   c) Los robots no pueden cambiar su movimiento.

---

## Actividades complementarias (para el alumno)

Cada actividad está pensada para realizarse en aproximadamente 20 minutos.

1. **Actividad complementaria 1: “Portería robótica”**  
   - Coloca tu robot “Pateador” frente a una pequeña portería hecha con bloques o materiales del salón.  
   - Usa una pelota pequeña (o un objeto redondo) y colócala frente al sensor.  
   - Ajusta el programa para que el robot patee **dos veces seguidas** cuando detecte el objeto.  
   - Intenta anotar “goles” moviendo la pelota a diferentes distancias del sensor y observa desde dónde funciona mejor.

2. **Actividad complementaria 2: “Pateador educado”**  
   - Modifica tu programa para que, antes de patear, el robot emita un **sonido** o muestre un **color** (si tu kit lo permite) cuando detecte el objeto.  
   - Haz que el robot espere **un segundo** después del aviso y luego patee.  
   - Prueba el robot con tus compañeros, explicando que el sonido o color es la “señal” de que la patada está por venir.

---

## Instrucciones para el profesor

### Contextualizo
- Presenta la historia de Lucía y Bruno leyendo en voz alta, usando entonación para mantener la atención.  
- Pregunta al grupo si han visto puertas automáticas o robots que reaccionan solos y relaciona sus respuestas con el sensor de proximidad.  
- Muestra (en pantalla o impreso) la ilustración sugerida o una imagen similar para reforzar la idea del robot pateador.  
- Guía una breve lluvia de ideas sobre “¿para qué sirve que un robot reaccione cuando algo se acerca?”.

### Examino
- Proyecta o muestra la imagen del modelo “Pateador” completamente armado.  
- Repite con énfasis la frase: **“Observa con atención la imagen del proyecto que vas a armar.”**  
- Pide a los alumnos que identifiquen visualmente: sensor, motor, engranajes y pierna que patea.  
- Haz preguntas como: “¿Dónde creen que está el sensor?”, “¿Qué parte se moverá cuando el motor gire?”.

### Armo
- Entrega a cada equipo su kit de robótica y asegúrate de que todos tengan acceso a las instrucciones visuales (carrusel o impresos).  
- Indica que sigan el paso a paso en silencio relativo, ayudándose en equipo.  
- Recorre el salón para apoyar en conexiones de motor, sensor y Smarthub.  
- Verifica que todos los modelos queden firmes y que la pierna pueda moverse libremente sin trabarse.

### Exploro – Actividad 1
- Asegúrate de que todos los dispositivos tengan el software WeDo 2.0 listo y el Smarthub conectado.  
- Guía a los alumnos en la creación del programa básico: bloque de inicio, bloque de sensor de proximidad y bloque de motor.  
- Explica con lenguaje sencillo qué es un “estímulo” (objeto cerca) y qué es una “reacción” (patada).  
- Pide que los alumnos prueben varias veces acercando y alejando objetos del sensor, observando la respuesta del robot.  
- Facilita una breve discusión grupal sobre qué pasa cuando el objeto está muy lejos o muy cerca.

### Exploro – Actividad 2 (Reto)
- Muestra físicamente diferentes tamaños de engranajes y explica de forma simple que el tamaño influye en la velocidad y fuerza del movimiento.  
- Indica a los equipos que cambien solo una cosa a la vez (primero engranajes, luego potencia del motor) para que puedan comparar.  
- Supervisa que los alumnos manipulen los engranajes con cuidado y vuelvan a conectar correctamente el motor.  
- Pide que cada equipo comparta qué combinación hizo la patada más fuerte y cuál la hizo más suave.  
- Refuerza la relación entre tamaño de engranajes, potencia del motor y resultado del movimiento.

### Concluyo
- Lee cada pregunta de opción múltiple en voz alta y da tiempo para que los alumnos marquen su respuesta.  
- Revisa las respuestas en grupo, pidiendo que expliquen por qué creen que la opción correcta lo es.  
- Aclara dudas sobre el funcionamiento del sensor de proximidad y la transmisión de movimiento con engranajes.  
- Relaciona lo aprendido con ejemplos cotidianos (puertas automáticas, robots aspiradora, juguetes que reaccionan).

### Actividades complementarias
- Organiza el tiempo para que al menos una de las actividades complementarias se realice al final de la sesión o en una clase siguiente.  
- Para “Portería robótica”, delimita un espacio seguro en el salón o patio y controla el uso de pelotas u objetos.  
- Para “Pateador educado”, apoya a los alumnos en la búsqueda de bloques de sonido o color en el software WeDo 2.0.  
- Fomenta que los alumnos expliquen sus decisiones de diseño (por qué eligieron cierta fuerza de patada o cierto aviso).  
- Cierra pidiendo a algunos equipos que muestren su robot y describan cómo reacciona a los estímulos.