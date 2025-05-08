def read_file(filename: str) -> bytearray:
    with open(filename, "rb") as file:
        return bytearray(file.read())


def main() -> None:
    before_file: str = input("Enter the before file: ")
    after_file: str = input("Enter the after file: ")

    # The ref file can be used to compare to your main save file. Only changes in the after file that also match your main save file will be printed.
    # Uncomment the code as needed to enable this functionality.
    #after_ref_file: str = input("Enter the after reference file: ")

    before_bytes = read_file(before_file)
    after_bytes = read_file(after_file)
    #after_ref_bytes = read_file(after_ref_file)

    min_length: int = min(len(before_bytes), len(after_bytes))
    max_length: int = max(len(before_bytes), len(after_bytes))
    #min_length: int = min(len(before_bytes), len(after_bytes), len(after_ref_bytes))
    #max_length: int = max(len(before_bytes), len(after_bytes), len(after_ref_bytes))

    if min_length != max_length:
        print("[WARN] The length of the files do not match. Only comparing the minimum!\n")

    #entries: int = 0
    for i in range(min_length):
        if before_bytes[i] != after_bytes[i]:
        #if before_bytes[i] != after_bytes[i] and after_ref_bytes[i] == after_bytes[i]:
            print(f"Found difference at offset {i} ({hex(i)}): {hex(before_bytes[i])} --> {hex(after_bytes[i])}\n")
            #entries += 1
            #if entries == 100:
            #    break


if __name__ == "__main__":
    main()
