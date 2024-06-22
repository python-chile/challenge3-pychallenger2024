Desafío 3: Camilo, el marino de telecomunicaciones
==================================================
## Contexto:
Camilo es un marino encargado de la radio en el acorozado del que es parte. Acaba de recibir un importante mensaje encriptado. El algoritmo de desencriptación es el siguiente:
* Modifica cada letra por su consecutiva, es decir la letra "A" debe cambiarse por "B". El último caracter de un rango pasa a ser el primero del siguiente (Ver tabla debajo), por ejemplo "Z" pasa a ser "a", "z" pasa a ser "Á", 9 para a ser "A", etc.
* Elimina los 5 caracteres más populares del mensaje (sensible a mayusculas)
* Los 2 caracteres más populares siguientes se cambian por espacio (los espacios consecutivos pasan a ser un espacio)
Los caracteres que contiene el mensaje está en estos rangos:

| Caracter |Código Unicode|
|-|-|
|,|44|
|.|46|
|0-9|48-57|
|A-B|65-90|
|a-b|97-122|
|Á|193|
|É|201|
|Í|205|
|Ñ|209|
|Ó|211|
|Ú|218|
|á|225|
|é|233|
|í|237|
|ñ|241|
|ó|243|
|ú|250|

Luego descubrirás que el mensaje contiene nombres de entidades, profesiones y edades. Deberás identificar esas palabras clases y listar. Se sabe que todos los sustantivos son palabras claves y todos los números son edades.
¿Puedes ayudar a Camilo a desencriptar el mensaje? (en caso de que utilice bibliotecas externas debe agregarlas en requirements.txt)
## Parte 1: Desencriptar el mensaje
Implementa función decrypt_message en utils.py recibiendo como parámetro el mensaje encriptado y retornando el string desencriptado
## Parte 2: Clasifica morfologicamente las palabras
Implementa función categorize_words en utils.py para categorizar las palabras morfólogicamente (Sugerencia: Usar biblioteca spacy y propiedades pos_ o tag_ de los tokens), retornando una lista de tuplas de 2 items, donde el primer elemento es la palabra y el segundo el tipo morfológico.
## Parte 3: Listar información
Implementar función list_info en utils.py que recibe como parámetro el string encriptado y retorna un diccionario cuya claves son nombres de entidades (lista de PROPN) y valores otro diccionario con 2 items:
* Profession: Profesión de la persona (lista de NOUN y ADJ, es decir sustantivos y adjetivos. Se omiten sustantivos extras como años en los mensajes)
* Age: Edad de la persona (número observado)

Una buena idea para separar entidades es observar los signos de puntuación.

BONUS: ¿Y si el mensaje contiena más información? Juega agregando más información al mensaje desencriptado (como parientes, direcciones, etc.) y ve que tal te va recogiendo la información.

Corre los tests con:

python armada.py
