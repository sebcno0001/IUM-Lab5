# Laboratorium 5 - konteneryzacja pipeline'u ML

Pipeline klasyfikacji zbioru Wine uruchamiany w kontenerze Docker.

## Zadanie 1 - obraz bazowy i zależności

Plik `Dockerfile` tworzy obraz na podstawie `python:3.11-slim`. Zależności z `requirements.txt` są instalowane przed skopiowaniem modułów, dzięki czemu Docker może ponownie wykorzystać warstwę z bibliotekami.

```bash
docker build -t ium-lab5:base .
```

## Zadanie 2 - usługa treningowa i wolumeny

Usługa `train` wczytuje ustawienia z `.env.train`. Katalogi `data`, `models` i `results` są montowane z hosta do kontenera.

```bash
docker compose build train
docker compose config
```
