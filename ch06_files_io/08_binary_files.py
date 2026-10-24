"""6.8 Binary files and bytes.

Real-world comparison: text files are letters written in a language;
binary files are raw recordings, like a photo or a song. You copy
them byte for byte without trying to "read" them as words.
"""

from pathlib import Path

out = Path(__file__).parent / "output"
out.mkdir(exist_ok=True)

# Text and bytes are different. encode() turns text into bytes.
word = "café"
raw = word.encode("utf-8")
print("Text:", word, "| bytes:", raw, "| length", len(word), "vs", len(raw))
print("Back to text:", raw.decode("utf-8"))

# Write and read bytes with mode "wb" / "rb".
data = bytes(range(10))
(out / "numbers.bin").write_bytes(data)
print("Read back:", list((out / "numbers.bin").read_bytes()))

# Build a tiny valid image file by hand: a 2x2 pixel BMP picture.
width, height = 2, 2
pixels = bytes([0, 0, 255, 0, 255, 0, 0, 0,      # red, green, padding
                255, 0, 0, 255, 255, 255, 0, 0])  # blue, white, padding
header_size = 14 + 40
bmp = b"BM" + (header_size + len(pixels)).to_bytes(4, "little") + b"\0\0\0\0" \
    + header_size.to_bytes(4, "little") \
    + (40).to_bytes(4, "little") + width.to_bytes(4, "little") \
    + height.to_bytes(4, "little") + (1).to_bytes(2, "little") \
    + (24).to_bytes(2, "little") + b"\0" * 24 + pixels
(out / "tiny.bmp").write_bytes(bmp)
print("Wrote a", len(bmp), "byte image: output/tiny.bmp")

# Real use: copy any file in chunks (works for huge videos too).
def copy_file(src, dst, chunk_size=4096):
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while chunk := fin.read(chunk_size):
            fout.write(chunk)


copy_file(out / "tiny.bmp", out / "tiny_copy.bmp")
same = (out / "tiny.bmp").read_bytes() == (out / "tiny_copy.bmp").read_bytes()
print("Copy identical?", same)
