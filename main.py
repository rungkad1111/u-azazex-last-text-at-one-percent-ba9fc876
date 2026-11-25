import os

TEXT = "1% left so quick: tell my charger I loved it, delete my 3am search history, and tell your mum I DID see her text, I just chose peace. If I die mid-send, I forgave the toilet drop."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
