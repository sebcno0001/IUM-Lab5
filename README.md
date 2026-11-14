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

## Zadanie 3 - trening w kontenerze

Moduł `src/pipeline.py` uruchamia kolejno trening i ewaluację. Model oraz raport pozostają w katalogach hosta dzięki wolumenom.

```bash
docker compose up --build
ls -lh models results
```

## Zadanie 4 - druga usługa i limity zasobów

Usługa `visualize` udostępnia zapisane wyniki na porcie 8080. Jej uruchomienie zależy od usługi `train`, dla której ustawiono limit 512 MB pamięci i jednego rdzenia procesora.

```bash
docker compose up --build -d
docker stats --no-stream l5-train-1
curl http://localhost:8080/wyniki.txt
```
