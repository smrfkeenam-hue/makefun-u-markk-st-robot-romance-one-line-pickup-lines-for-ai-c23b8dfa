import os

# Robot Romance: one joke pickup line aimed at an AI.
# The laugh comes from autocomplete -- the machine finishing your
# sentences better than you do -- not from a generic compliment.
ENTRY = "You must be my autocomplete, because you keep finishing my sentences, and honestly, yours are better."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
