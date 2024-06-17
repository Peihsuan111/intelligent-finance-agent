def load_prompt_from_md(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
