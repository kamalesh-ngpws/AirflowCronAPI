# Steps to run

- build image 

``` docker build --pull --rm -f "dockerfile" -t hellofastapiws:latest "." ```

- run container 

``` docker run --rm -it -p 8000:8000/tcp hellofastapiws:latest ```
