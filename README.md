# PodcastRecommendation 
### ```0.1.8``` 
Podcast Recommendation Algorithm


## Instalar

```
python3 -m pip install podcast-recommendation
```
```
pip install podcast-recommendation
```
```
pip install podcast-recommendation==0.1.8
```

## Uso
### Import
```py
from podcast_recommendation.algorithm import PodcastRecommendation
```

### Crear objeto
Para utilizarlo debe tener una DataBase abierta en Neo4j con el plugin de Data Science
![db](img/neo4j-db.png)
```py
pr = PodcastRecommendation('bolt://localhost:7687', ('neo4j', 'password'), verbose=True)
```
```
Reading x_train
Reading y_train
Training model
Training complete
```

### Generar grafo
```py
pr.build_graph(verbose=True)
```
```
Reading categories
Reading ratings
Creating categories, categories and IsA
Creating users, categories and ratings
Build complete
```

Se genera un grafo como el siguiente:
![grafo](img/neo4j-graph.png)

### Generar recomendaciones
Para recomendar podcast al usuario ```6C561484AED5C02```
```py
pr.recommend(user_id='6C561484AED5C02')
```
```
       proba                                              title
47  0.999225                                Noah Kagan Presents
31  0.999216                              The Model Health Show
30  0.999042                       Mind Pump: Raw Fitness Truth
42  0.999038                                      Jocko Podcast
43  0.998779            The Learning Leader Show With Ryan Hawk
32  0.998615                             Ben Greenfield Fitness
...
```
### Eliminar el grafo
```py
pr.delete_all()
```

### Eliminar rating
Eliminar rating entre usuario ```6C561484AED5C02``` y podcast ```a3a535f66c7e8004e7dc54c2b2829a9e```
```py
pr.delete_rtg(user_id='6C561484AED5C02', podcast_id='a3a535f66c7e8004e7dc54c2b2829a9e')
```

### Crear rating
Crear rating de 5 entre usuario ```6C561484AED5C02``` y podcast ```a3a535f66c7e8004e7dc54c2b2829a9e```
```py
pr.create_rtg(user_id='6C561484AED5C02', podcast_id='a3a535f66c7e8004e7dc54c2b2829a9e', rating=5)
```

### Crear usuario
Crear usuario de id ```A1A1A1A1A1A1A1```
```py
pr.create_user(user_id='A1A1A1A1A1A1A1')
```

### Crear podcast
Crear podcast de id ```a1a1a1a1a1a1a1a1a1a1a1``` y t??tulo ```prueba```
```py
pr.create_podcast(podcast_id='a1a1a1a1a1a1a1a1a1a1a1', title='prueba')
```

### Crear categoria
Crear categoria de nombre ```cat``` e id ```99``` 
```py
pr.create_category(category='cat', category_id=99)
```

### Crear relaci??n IsA
Crear relaci??n podcast de id ```a1a1a1a1a1a1a1a1a1a1a1``` IsA categoria de nombre ```cat```
```py
pr.create_IsA(podcast_id='a1a1a1a1a1a1a1a1a1a1a1', category='cat')
```

### Cerrar driver
```py
pr.close()
```
