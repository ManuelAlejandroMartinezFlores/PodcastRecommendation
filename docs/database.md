# Base de Datos

La base de datos consiste de 3 tablas principales y 2 tablas con atributos de entrenamiento. 

## Tablas Principales

Las tablas principales son: 

- [categories.sample.csv](#categories-sample)
- [podcast_sample_title.csv](#podcast-sample-title)
- [ratings_sample.csv](#ratings-sample)

### Categories Sample
La tabla consta de 3 columnas:

- podcast_id: id para el podcast
- category: nombre de la categoria
- category_id: id de la categoria

Esta tabla es utilizada para generar las relaciones ```IsA``` en Neo4j. <br>
[Acceder archivo](https://github.com/ManuelAlejandroMartinezFlores/PodcastRecommendation/blob/main/src/podcast_recommendation/data/categories_sample.csv)


### Podcast Sample Title
La tabla consta de 2 columnas:

- podcast_id: id del podcast
- title: título del podcast

La tabla es utilizada para mostrar los títulos en las recomendaciones. <br>
[Acceder archivo](https://github.com/ManuelAlejandroMartinezFlores/PodcastRecommendation/blob/main/src/podcast_recommendation/data/podcast_sample_title.csv)


### Ratings Sample
La tabla consta de 4 columnas:

- podcast_id: id del podcast evaluado
- user_id: id del usuario realizando la evaluación
- rating: rating del podcast entre 1 y 5
- liked: si rating es mayor a 2 o no

Esta tabla es utilizada para generar las relaciones ```Rating``` en Neo4j. <br>
[Acceder archivo](https://github.com/ManuelAlejandroMartinezFlores/PodcastRecommendation/blob/main/src/podcast_recommendation/data/ratings_sample.csv)


## Tablas de entrenamiento
Las tablas de entrenamiento son:

- [x_train.csv](#x-train)
- [y_train.csv](#y-train)

### X Train
La tabla consta de 13 columnas:

- podcast_id: id del podcast
- user_id: id del usuario
- cat_based: suma de ratings obtenidos en paths de la forma ```(User)->(Podcast)<-(Category)->(Podcast)```
- cat_cnt: cuenta de paths de la forma ```(User)->(Podcast)->(Category)<-(Podcast)``` 
- user_based: suma de ratings obtenidos en paths de la forma ```(User)->(Podcast)<-(User)->(Podcast)```
- user_cnt: cuenta de paths de la forma ```(User)->(Podcast)<-(User)->(Podcast)```
- adamic_adar: multiplicación de rating con la métrica Adamic Adar entre podcasts de la forma ```(User)->(Podcast)--()--(Podcast)```
- resource_allocation: multiplicación de rating con la métrica Resource Allocation entre podcasts de la forma ```(User)->(Podcast)--()--(Podcast)```
- link_cnt: cuenta de paths de la forma ```(User)->(Podcast)--()--(Podcast)```
- cat_avg: cat_based dividido entre cat_cnt
- user_avg: user_based dividido entre user_cnt
- adar: adamic_adar dividido entre link_cnt
- ra_avg: resource_allocation dividido entre link_cnt

Esta tabla es utilzada para entrenar el modelo de regresión logística <br>
[Acceder archivo](https://github.com/ManuelAlejandroMartinezFlores/PodcastRecommendation/blob/main/src/podcast_recommendation/data/x_train.csv)

### Y train
Esta tabla contiene una única columna:
<ul>
<li> liked: si el rating es mayor o igual a 3 </li>
</ul>

Esta tabla es el objetivo del entrenamiento del modelo <br>
[Acceder archivo](https://github.com/ManuelAlejandroMartinezFlores/PodcastRecommendation/blob/main/src/podcast_recommendation/data/y_train.csv)

