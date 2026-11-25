**API desplegada en Render:** https://taller3fbd-s6a7.onrender.com

## Parte 1: Modelado de datos

**1. ¿Qué estrategia se utilizó para modelar cada entidad de DrinkAdvisor dentro de la base de datos documental? ¿Cuáles relaciones se modelaron como objetos embebidos y cuáles se modelaron como referencias?**

Se usó un modelo híbrido. Bares, bebidas y bebedores se quedaron en Oracle, y en MongoDB solo se modelaron comentarios y eventos, cada uno en su propia colección. La relación con el bar es una **referencia** (`bar_id` apunta a `BARES.ID`). No se embebieron en el bar porque crecen sin límite y el bar está en otra base de datos.

**2. ¿Qué estrategia se utilizó para modelar cada entidad dentro de la base de datos documental? ¿Cuáles relaciones se modelaron como objetos embebidos y cuáles se modelaron como referencias?**

Cada comentario y cada evento es un documento independiente con sus atributos **embebidos**: en los comentarios, `texto`, `autor`, `calificacion` y `fecha`; en los eventos, `nombre` y los campos libres de cada tipo. La única **referencia** es `bar_id`. Gracias al esquema flexible, cada evento puede tener campos distintos.
