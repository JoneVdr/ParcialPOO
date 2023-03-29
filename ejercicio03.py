"""Ejercicio 3 (2,5 puntos) Tiempo estimado: 20 minutos.


En este último ejercicio se pide que se implemente el módulo principal del juego. Este módulo principal va a implementar la partida que van a jugar los jugadores, los cuales se encuentran identificados como los entrenadores de los combatientes.


En este módulo main, lo primero que se hace es obtener la configuración deseada de los Pokemons por parte de cada entrenador. Hay que tener en cuenta, que cada entrenador solamente va a tener tres Pokémons al iniciar la partida.


Las características de cada uno de los grupos de Pokemons que va a poseer cada entrenador van a ser introducidas a través de archivos CSV. Los dos archivos CSV a utilizar por en este ejercicio han sido proporcionados:


coach_1_pokemons.csv
coach_2_pokemons.csv

Se deben crear los Pokémons leyendo los ficheros CSV para cada uno de los entrenadores (ver Flowchart).


Seguidamente, una vez que se tienen las configuraciones de cada uno de los equipos, cuya implementación debe realizarse en la función get_data_from_user(), el combate puede comenzar entre los entrenadores.


Los combates entre Pokemons se van a realizar secuencialmente. Además, un combate se entiende como aquel llevado a cabo por un Pokémon de cada uno de los equipos. Por lo tanto, en cada turno un Pokémon de uno de los equipos va a atacar a otro Pokémon del otro equipo. Una vez que dos Pokémons entran en combate, no se para este combate hasta que uno de los dos Pokémons es derrotado, momento en el que el siguiente Pokémon del entrenador debe entrar al combate seleccionando un Pokémon de aquellos que no estén derrotados. La función get_pokemon_in_a_list_of_pokemons() tiene que ser implementada para ayudar a que el usuario del juego pueda elegir algún Pokemon que todavía esté sin derrotar por parte de cada uno de los entrenadores. Implementar también la función coach_is_undefeated() para que esta función nos devuelva si todos los Pokémons de un entrenador han sido derrotados o queda alguno vivo.


Cuando uno de los dos entrenadores tenga ya todos sus Pokémon derrotados al acabar el turno, se acaba el juego, y se indica no solo quién es el ganador, sino también las estadísticas de cada equipo en base a los puntos de vida de los Pokémons. En el caso de que los dos acaben sin Pokémons en el mismo turno, el juego indicará un empate. En cada turno los dos Pokémons atacan con independencia de si en ese mismo turno es derrotado.


Recuerde utilizar las clases implementadas tanto en el ejercicio 4 como en el ejercicio 5 para implementar todos los componentes de este juego.


El diagrama de flujo de este módulo principal le ha sido proporcionado a modo de guía."""