# The World in One Image — 18 November 2026

Entry for make.fun's **news-image-20261118** bounty:
https://make.fun/bounty/news-image-20261118

A front-page poster that sums up Wednesday 18 November 2026's world news
in a single 1024×1024 image. Every headline on the page is drawn as real
text, so the story is readable from the image itself.

## What the image shows

- **APEC OPENS IN SHENZHEN** — the APEC summit opens in Shenzhen, China;
  Trump, Xi and Putin are set to hold their first-ever trilateral summit
  the next day on the sidelines.
- **QUAD MEETS IN MANILA** — Trump arrives in Manila for Quad talks with
  Australia, India and Japan ahead of his China visit.
- **UKRAINE HITS CRIMEA BRIDGE** — Ukraine strikes the Kerch/Crimea bridge
  a second straight night; a road span collapses.
- **IRAN DRONES STRIKE BAHRAIN RADAR** — Iran drones hit a US military
  radar in Bahrain; the US strikes Qeshm island and Kuwait intercepts
  more drones.
- **Also today** — Spain's general strike halts ports and factories; the
  Board of Peace warns the Gaza ceasefire "faces collapse"; North Korea
  fires a missile into the Sea of Japan.

Sources (checked 18 Nov 2026): jagranjosh.com, rajglobalstudies.com,
gtdaily.news, mediaalertpress.com, themunicheye.com, thewest.com.au.

## How it works

`main.py` (Python 3.13, standard library only) copies the vendored poster
`assets/entry.png` byte-for-byte to `/output/entry.png`. No network, no
clock, no randomness — two runs produce identical bytes.

The poster itself was drawn with code (Pillow) in `tools/render.py`:
flat-vector editorial style, real text throughout, no AI-generated imagery.

## Run it

```sh
python3 main.py        # writes /output/entry.png (1024x1024 PNG, ~104 KB)
python3 main.py        # second run: byte-identical output
sha256sum /output/entry.png
```

## License

MIT — see `LICENSE`.
