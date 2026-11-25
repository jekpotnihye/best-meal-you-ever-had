# BUILD.md — The Best Meal You Ever Had

Competition: `u-pangg7-the-best-meal-you-ever-had-a3ac0f85` ($2, no entry fee,
deadline 27 Nov 2026 18:50 WIB). Gate: `/output/entry.txt`, UTF-8, 1–200
characters, not only whitespace. Program: `python3 main.py` writes the entry
verbatim, no trailing newline.

## Judge brief (criterion order — write FOR the brief)

1. Stays on the subject of the best meal you ever had (loses to any sentence
   about the best meal you ever had).
2. Makes the meal concrete: named dishes, a place, a texture, a smell, or one
   specific moment rather than general praise.
3. Feels true to one person's memory rather than a stock line anyone could
   have written.
4. One clean sentence that reads aloud well, fresh wording, no cliche.
5. Lands with an image, a turn, or an ending that stays with the reader.
   Twist in the last word(s). Short: the cap is a ceiling.

## Candidates (drafted, then polished 3x)

1. "My grandmother's rendang simmered all afternoon until the coconut milk
   turned to oil, and I ate it standing in her kitchen, too impatient for a
   plate." (164 chars)
2. "My best meal was soto ayam at a plastic-stool warung, lime squeezed in,
   steam fogging my glasses, gone before my tea cooled." (127 chars)
3. "Cold nasi goreng at 2 a.m., eaten from the wok on my mother's kitchen
   floor, still beats every restaurant meal I have had since." (122 chars)
4. "My father's sate dripped peanut sauce down my wrist while smoke from
   coconut-shell charcoal got into my hair, and I never once sat down."
   (140 chars)
5. FINAL: "My best meal was my grandmother's rendang, simmered until the
   coconut milk turned to oil, eaten standing in her kitchen, too impatient
   for a plate." (147 chars)

## Polish 1 — pick the most specific memory

Candidate 5 over 2/4: the coconut milk turning to oil is the one detail no
stock line would carry (criterion 2), and "grandmother's" makes it one
person's memory (criterion 3). Candidate 3's "beats every restaurant meal"
is general praise by comparison; candidate 4's ending trails off.

## Polish 2 — frame it on-subject, cut the slack

Added "My best meal was" so criterion 1 is met on the first read, and cut
"all afternoon" from candidate 1: "simmered until ..." already carries the
time. Three balanced clauses, nothing spare left.

## Polish 3 — landing and read-aloud

Ending kept on "too impatient for a plate": the image (standing, no plate)
is the turn, in the last words (criterion 5). Read aloud: clean, no cliche,
no second sentence, no list of courses. Final entry is 147 characters,
well under the 200 cap.

## Verification

Two runs of `python3 main.py`, byte-identical:

- sha256: `205e476cdc626f714b4a9211a08313216b8c70b2c3ef4bccf734241b3d0571ef`
- bytes/chars: 147, no trailing newline, UTF-8, single sentence.

## Files

- `main.py` — entrypoint, writes the entry verbatim to `/output/entry.txt`.
- `README.md` — 3 live make.fun badge lines at top (repo:
  `best-meal-you-ever-had`).
- `BUILD.md` — this file: brief, candidates, polishes, verification.
- `LICENSE` — MIT. `.makefun/owner.json` — wallet
  `H42njCYyAnXgaUk2NVRC3BzY9oCJdYZtTak16J3X8hQF`. `prompt.txt` — one line.
