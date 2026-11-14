from evaluate import main as evaluate
from train import main as train


def main():
    print("[1/3] Wczytanie danych i trening", flush=True)
    train()
    print("[2/3] Ewaluacja modelu", flush=True)
    accuracy = evaluate()
    print(f"[3/3] Pipeline zakończony, accuracy={accuracy:.4f}", flush=True)


if __name__ == "__main__":
    main()
