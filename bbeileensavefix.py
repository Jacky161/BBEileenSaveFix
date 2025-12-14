# https://github.com/Noxde/Bloodborne-save-editor/blob/8f86be4d4d37db9c4902bab200836c8edfd2f736/src-tauri/src/data_handling/constants.rs
USERNAME_TO_INV_OFFSET: int = 469
USERNAME_TO_AOB: int = 68545

AOB_SIZE: int = 150816  # Length of AOB is actually unknown, this is a best guess

EILEEN_THE_CROW: dict[int, tuple[int, int]] = {0x417  : (0x10, 0x00),
                                               0x418  : (0x00, 0x40),
                                               0x441  : (0x00, 0x04),
                                               0x1C29 : (0x00, 0x30),
                                               0x3DC9 : (0x00, 0x02),
                                               0x134E6: (0x00, 0x80),
                                               0x134E7: (0x00, 0x01)}
# Patch format is: offset into AOB --> (before_aggression byte, after_aggression byte)


def read_file(filename: str) -> bytearray:
    with open(filename, "rb") as file:
        return bytearray(file.read())


def output_file(filename: str, the_bytes: bytearray) -> None:
    with open(filename, "wb") as file:
        file.write(bytes(the_bytes))


def find_username_offset(the_bytes: bytearray) -> int:
    # https://github.com/Noxde/Bloodborne-save-editor/blob/8f86be4d4d37db9c4902bab200836c8edfd2f736/src-tauri/src/data_handling/offsets.rs
    inv_start_bytes: list[int] = [0x40, 0xf0, 0xff, 0xff]
    inv_start_bytes: bytearray = bytearray(inv_start_bytes)

    for i in range(len(the_bytes) - len(inv_start_bytes)):
        test_bytes: bytearray = the_bytes[i:(i + len(inv_start_bytes))]

        if inv_start_bytes == test_bytes:
            username_offset: int = i - USERNAME_TO_INV_OFFSET
            return username_offset

    raise Exception("No username found")


def export_save(filename: str, save_data: bytearray, aob_start: int, aob_bytes: bytearray) -> None:
    final_bytes: bytearray = save_data[0:aob_start] + aob_bytes + save_data[aob_start + AOB_SIZE:]
    output_file(filename, final_bytes)


def main() -> None:
    save_file: str = input("Enter the filename of your save file (userdata0000): ")
    if save_file == "":
        save_file = "userdata0000"

    save_data: bytearray = read_file(save_file)
    username_offset: int = find_username_offset(save_data)

    print(f"[INFO] Found username offset at {username_offset} bytes.")
    aob_start: int = username_offset + USERNAME_TO_AOB
    print(f"[INFO] AOB starts at {aob_start} bytes.")

    usr_input_msg: str = """1. Extract AOB
2. Import AOB
3. Patch Eileen the Crow
The Eileen the Crow patch will turn him non-aggressive ONLY IF you attacked him at the cathedral ward (Location 2).
This also assumes you interacted with him at Location 1 (Central Yharnam). See https://bloodborne.wiki.fextralife.com/Eileen+the+Crow

Choose from the options: """

    usr_input: int = int(input(usr_input_msg))
    aob_bytes: bytearray = save_data[aob_start: aob_start + AOB_SIZE]

    if usr_input == 1:
        output_file(f"{save_file}_AOB", aob_bytes)
        print(f"[INFO] AOB saved to {save_file}_AOB")

    elif usr_input == 2:
        new_aob_file: str = input(f"Enter the filename of your new AOB file ({save_file}_AOB): ")
        if new_aob_file == "":
            new_aob_file = f"{save_file}_AOB"

        aob_bytes: bytearray = read_file(new_aob_file)

        export_save(f"{save_file}_newAOB", save_data, aob_start, aob_bytes)
        print(f"[INFO] New save exported to {save_file}_newAOB")

    elif usr_input == 3:
        mismatch: bool = False
        for offset, change in EILEEN_THE_CROW.items():
            if aob_bytes[offset] != change[1]:
                print(f"[ERROR] Offset at {hex(offset)} does not match. Expected {hex(change[1])} but got {hex(aob_bytes[offset])}.")
                mismatch = True
            aob_bytes[offset] = change[0]

        if not mismatch:
            print(f"[INFO] No issues found! Patching!")
            export_save(f"{save_file}_newAOB", save_data, aob_start, aob_bytes)
            print(f"[INFO] New save exported to {save_file}_newAOB")
        else:
            print(f"[ERROR] Issues detected. Cannot patch file.")


if __name__ == "__main__":
    main()
