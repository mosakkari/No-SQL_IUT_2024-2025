# Exercice 1

## Installation de redis

```bash
sudo dnf install redis
sudo sustemctl start redis
```

## Vérifier que Redis fonctionne

```
$ redis-cli ping
PONG
```

## Ouvrire une invite

```
$ redis-cli
127.0.0.1:6379> ping
PONG
```

## Configuration

```
> CONFIG GET loglevel
1) "loglevel"
2) "notice"
```

La commande `CONFIG SET loglevel "notice"` signifie qu'on met la valeur de la configuration `loglevel` à `notice`.

## Commandes

### 1: Comment créer une clé (key) username avec la valeur (value) Alice dans Redis ?

```
set username Alice
```

### 2: Quelle commande utiliseriez-vous pour récupérer la valeur de la clé username ?

```
get username
```

### 3: Comment modifier la valeur de la clé username pour Bob ?

```
set username Bob
```

### 4: Comment vérifier la nouvelle valeur de la clé username ?

```
get username
```

### 5: Comment créer une liste (list) fruits et ajouter les éléments apple, banana, orange ?

```
rpush fruits apple banana orange
```

### 6: Quelle commande permet d'afficher tous les éléments de la liste fruits ?

```
lrange fruits 0 -1
```

### 7: Comment ajouter grape à la fin de la liste fruits ?

```
rpush fruits grapes
```

### 8: Comment afficher à nouveau tous les éléments de la liste fruits ?

```
lrange fruits 0 -1
```

### 9: Comment créer un ensemble (set) colors et ajouter les éléments red, blue, green ?

```
sadd colors red blue green
```

### 10: Que se passe-t-il si vous essayez d'ajouter red à l'ensemble colors ?

```
> sadd colors red
(integer) 0
```

### 11: Quelle commande permet d'afficher tous les membres de l'ensemble colors ?

```
smembers colors
```

### 12: Comment créer un ensemble trié (sorted set) scores avec les éléments Alice (100) et Bob (200) ?

```
zadd scores 100 Alice 200 Bob
```

### 13: Quelle commande utiliseriez-vous pour afficher les membres de l'ensemble trié scores avec leurs scores ?

```
zrange scores 0 -1 withscores
```

### 14: Comment ajouter Charlie avec un score de 150 à l'ensemble trié scores ?

```
zadd scores 150 Charlie
```

### 15: Comment afficher les membres de l'ensemble trié scores à nouveau ?

```
zrange scores 0 -1 withscores
```

### 16: Comment créer un hachage (hash) user:1001 avec les champs name (Alice) et age (30) ?

```
hset user:101 name Alice age 30
```

### 17: Quelle commande utiliseriez-vous pour récupérer le nom de l'utilisateur dans le hachage user:1001 ?

```
hget user:101 name
```

### 18: Comment ajouter un champ email à l'utilisateur dans le hachage user:1001 ?

```
hset user:1001 email ivan@midae.fr
```

### 19: Quelle commande permet d'afficher tous les champs du hachage user:1001 ?

```
hgetall user:1001
```

## Bases de données du SGBD Redis

```
> config get databases
1) "databases"
2) "16"
```

### 20: Tester et interpréter le résultat de la commande `INFO keyspace`

```
> info keyspace
# Keyspace
db0:keys=6,expires=0,avg_ttl=0
```

Dans db0, il y a 6 clés qui n'ont pas de date d'expiration.

### 21: Exécuter et interpréter les commandes

#### a

```
SET visites 10
get visites
incr visites
get visites
decr visites
get visites
```

On créer visites à 10 (`SET`), on l'incrémente (`INCR`) puis on le décrémente (`DECR`).

#### b

```
incrby visites 10
get visites
decrby visites 5
get visites
```

On incrémente visite de 10 (`INCRBY`) puis on le décrémente de 5 (`DECRBY`).

#### c

```
set hello "Hello World"
setrange hello 6 "Redis"
get hello
getrange hello 0 5
```

On crée hello avec la valeur `"Hello World"` (`SET`), on remplace 5 caractères à partir du caractère 0 pour les mettre à `"Redis"` (`SETRANGE`), et on regarde les caractères 0 à 5 (inclus) de hello (`GETRANGE`).

#### d

```
set hello "Hello World"
strlen hello
```

On crée hello avec la valeur `"Hello World"` (`SET`) et on lit la longueur de la chaîne (`STRLEN`).

#### e

```
set hello "Hello"
append hello " World !"
get hello
```

On crée hello avec la valeur `"Hello"` (`SET`) et on ajoute `" World !"` (`APPEND`).

### 22: Créer les clés

```
SET user:1 "Damien Faure"
SET user:1:city "La Rochelle"
SET user:1:age "35"
SET user:1:activity "Running"
EXPIRE user:1:activity 600
SET user:1:hobby "Course à pieds"
SET user:1:weight "74"
```

### 23: Lire les clés

```
> GET user:1
"Damien Faure"
> GET user:1:city
"La Rochelle"
> GET user:1:age
"35"
```

### 24: Lire les clés en une fois

```
> MGET user:1 user:1:city user:1:age
1) "Damien Faure"
2) "La Rochelle"
3) "35"
```

### 25: Définir si n'existe pas

```
SET user:1 "Thomas Davaut" NX
```

### 26: Définir si existe

```
SET user:1:city Bordeaux XX
```

### 27: Mise à jour de l'utilisateur

-   Ajouter un an
-   Retirer trois kilos
-   Àjouter "La Rochelle/" au début de city

```
incr user:1:age
decrby user:1:weight 3
```

Troisième pas possible.

### 28: Deuxième mise à jour de l'utilisateur

-   Ajouter "course hippique" aux hobbies
-   Lire la longueur de la clé hobby

```
append user:1:hobby ", course hippique"
strlen user:1:hobby
```

### 29: Récupérer une partie de la clé

Pour finir, récupérez juste le fragment de valeur "Bordeaux" de la clé city.

```
getrange user:1:city -10 -1
```

### 30: Soirée

Antoine et Thomas organisent une soirée.

Antoine veut inviter:

-   Sophie
-   Etienne
-   Hélène
-   Paul
-   Charles
-   Ethan
-   Pauline

Thomas souhaite inviter:

-   Etienne
-   Paul
-   Catherine
-   Ethan
-   Pauline
-   Sophia
-   Mickaël

Ayant un espace limité, ils souhaitent inviter uniquement leurs amis communs. Qui sont-ils ?

-   Etienne
-   Paul
-   Ethan
-   Pauline

La semaine suivante, ils souhaitent organiser une soirée avec les personnes qui n'ont pas été invité à la première.

À l'aide de la documentation, établissez une liste des invités d'Antoine et une liste des invités de Thomas dans deux nouveaux SET.

```
sadd invites:antoine Sophie Etienne Hélène Paul Charles Ethan Pauline
sadd invites:thomas Etienne Paul Catherine Ethan Pauline Sophia Mickaël
```

Quelle-est la liste finale des invités pour cette seconde soirée ? Une fois établie, exportez-là dans un nouveau set avec l'aide de la documentation.

```
SINTERSTORE invites:soiree:1 invites:thomas invites:antoine
SUNIONSTORE invites:all invites:thomas invites:antoine
> SDIFF invites:all invites:soiree:1
1) "Catherine"
2) "Sophia"
3) "Micka\xc3\xabl"
4) "Sophie"
5) "H\xc3\xa9l\xc3\xa8ne"
6) "Charles"
SDIFFSTORE invites:soiree:2 invites:all invites:soiree:1
```

# Exercice 2

## 1: Créer la clé User avec comme valeur Dario

```
SET User Dario
```

## 2: Créer 2 clés avec une seule commande

-   User:3 = Maud
-   User:4 = Xavier

```
MSET User:3 Maud User:4 Xavier
```

## 3: Lister toutes les clés définies dans la base

```
keys *
```

## 4: Lister toutes les clés commençant par User

```
keys User*
```

## 5: Lister les valeurs des différentes clés

```
mget invites:all scores User user:1 fruits invites:antoine user:1:weight user:1:city invites:thomas user:1:age invites:soiree:1 user:1001 user:101 User:4 User:3 colors user:1:hobby visites username hello invites:soiree:2
```

## 6: Ajouter un ‘e’ à la fin de valeur de la clé User:3

```
append User:3 e
```

## 7: Tester et interpréter la commande : SETNX User:3 "Aude"

```
> SETNX User:3 "Aude"
(integer) 0
```

Cette commande Crée l'utilisateur 3 avec le nom Aude s'il n'existe pas. L'utilisateur 3 existe donc la commande ne fait rien et renvoie 0.

## 8: Créer une clé temporaire User:5 avec comme valeur Toto de durée de vie 30 secondes

```
set User:5 Toto
EXPIRE User:5 30
```

## 9: Vérifier la durée de vie de la clé User:5

```
> ttl User:5
(integer) 28
```

## 10: Vérifier la durée de vie de la clé User:1

```
> ttl User:1
(integer) -2
```

## 11: Créer les clés

-   User:6 = Toto
-   User:6:City = Paris
-   User:6:Age = 25
-   User:6:Activity = Tutorial (10 minutes à vivre)

```
SET User:6 Toto
SET User:6:City Paris
SET User:6:Age 25
SET User:6:Activity Tutorial EX 600
> TTL User:6:Activity
(integer) 591
> TTL User:6:Activity
(integer) 586
> TTL User:6:Activity
(integer) 584
```

## 12: Ajouter à la User:6:Activity

Ajouter à User:6:Activity la valeur " Redis" (commande APPEND) et vérifier la valeur de User:6:Activity

```
APPEND User:6:Activity " Redis"
> GET User:6:Activity
"Tutorial Redis"
```

## 13: Tester les instructions et analyser leur résultat

```
127.0.0.1:6379> MSETNX User:6:Note 20 User:4:Time 5
(integer) 1
127.0.0.1:6379> MSETNX User:6:Note 20 User:4:Validation Redis
(integer) 0
127.0.0.1:6379> MSETNX User:5:Note 20 User:4:Validation Redis
(integer) 1
```

La première fonctionne car il n'y a pas encore `User:6:Note` ni `User:4:Time`. La deuxième ne fait rien car les deux clés existent déjà. La troisième fonctionne car `User:5:Note` n'existe pas.

## 14: Créer un utilisateur avec des champs similaires en utilisant les commandes HSET et HMSET.

```
HSET User:7 Age 20 City Niort Note 20
HMSET User:8 Age 19 City Niort Note 0
```

## 15: Tester les commandes HKEYS et HVALS sur ce nouvel utilisateur.

```
> HKEYS User:7
1) "Age"
2) "City"
3) "Note"
> Hvals User:7
1) "20"
2) "Niort"
3) "20"
```

## 16: SET JSON

Tester la commande suivante pour insérer une valeur en JSON: `SET User:8 {"nom":"Titi","age":23,"Activity":["Redis","MongoDB"]}`

```
SET User:8 '{"nom":"Titi","age":23,"Activity":["Redis","MongoDB"]}'
```

## 17: Créer une liste Cours en y ajouter la valeur NoSQL (cf. commande LPUSH)

```
lpush Cours NoSQL
```

## 18. Ajouter la valeur MicroServices dans la liste Cours (cf. commande LPUSH)

```
lpush Cours MicroServices
```

## 19: Lister les éléments de la liste

```
> lrange Cours 0 -1
1) "MicroServices"
2) "NoSQL"
```

## 20: Exécuter la commande MULTI

```
> multi
OK
```

## 21. Créer une liste Cours2 en y ajouter la valeur NoSQL

```
> lpush Cours2 NoSQL
QUEUED
```

## 22: Ajouter la valeur MicroServices dans la liste Cours

```
> lpush Cours MicroServices
QUEUED
```
