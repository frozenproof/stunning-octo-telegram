# Docker Q/A

# What happens if put files with main method into a single container?

The answer: Nothing happens.
Long answer: Docker won't know which file to execute.

We can use 3 methods to control this, but we focus on 2 specific methods:
## Method 1: dockerfile itself
```
ENTRYPOINT ["java", "-jar", "app.jar"]
```
This tell the docker the default command is running the app.jar

CMD works the same way, but ENTRYPOINT should not be overriden.

## Method 2: manually telling which main file to execute (doesnt work apparently if you use entrypoint in dockerfile)
```
docker run <image_name> java -jar app2.jar
```
```
docker run <image_name> java -jar app.jar
```
This method is more useful if you are using container like a toolset.

# What if I wrote both into a same app.jar?

The answer: The lastest command will overwrite the older commands. So you will lose the other jars.

# The file are too new to run on the docker???

The answer: Tell docker to pull new parent images down. This typically happens but don't fret, everything will be fine, as long as you don't look at new licenses.

For example, if the example jre in dockerfile is too old, try pulling new parent image of the jre
```
docker pull openjdk:21
```
and
```
docker pull openjdk:21-slim
```
or go nuclear
```
docker system prune --all
```