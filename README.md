# Laboratorium 5 - konteneryzacja pipeline'u ML

Pipeline klasyfikacji zbioru Wine uruchamiany w kontenerze Docker.

## Zadanie 1 - obraz bazowy i zależności

Plik `Dockerfile` tworzy obraz na podstawie `python:3.11-slim`. Zależności z `requirements.txt` są instalowane przed skopiowaniem modułów, dzięki czemu Docker może ponownie wykorzystać warstwę z bibliotekami.

```bash
docker build -t ium-lab5:base .
```
