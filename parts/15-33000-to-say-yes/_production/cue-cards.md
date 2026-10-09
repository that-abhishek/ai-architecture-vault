# Part 15: $33,000 to Say Yes (cue cards, verbatim)

One card per take. Every card is word for word, and captions are cut from these lines.
Read the card once, look at the lens, say it. Three takes back to back, keep the third.

Each card is tagged with how it's shot:
- `TALKING HEAD`: face to camera, at home. Cards 1, 12, 14.
- `SCREEN + VO`: voice-over read at home (audio only), laid over a screen recording of the canvas building up. The *Board* line says what appears while the card plays. Cards 2–11, 13.

---

## CARD 1 · HOOK · `TALKING HEAD`

Your app sends out a million AI answers.

Before each one ships, a second model reads it and says yes or no.

At frontier prices, that one word costs you thirty-three thousand dollars.

---

## CARD 2 · PANEL 1 · `SCREEN + VO`

*Board:* answer + source → FRONTIER JUDGE → yes

You are the judge. An answer comes in with its source, and you check whether it stays inside the source.

You run on a frontier model, so you pay frontier price for one word.

---

## CARD 3 · `SCREEN + VO`

*Board:* $33,000 / 1M checks, then the two yes words into if (yes)

There are two problems.

a) The bill grows with every answer you check.

b) Your yes carries no weight. A sure yes and a coin-toss yes look the same to the code that reads it.

---

## CARD 4 · T1 · `SCREEN + VO`

*Board:* RULE 1 writes in

Move yes-or-no checks off the frontier model.

---

## CARD 5 · PANEL 2 · `SCREEN + VO`

*Board:* question → yes / no boxes, bars fill to 0.93 and 0.07

Now you are not allowed to write. You get two boxes, yes and no, and you put a number on each.

Yes 0.93, no 0.07.

---

## CARD 6 · `SCREEN + VO`

*Board:* hold on the two bars

That is a System One model, and Jev from TypeSafe is the first one.

You declare the boxes up front, and every box comes back with a probability in one pass.

---

## CARD 7 · `SCREEN + VO`

*Board:* Jev · 91.5% agree, then $160

On six thousand checks of financial research answers, Jev agreed with the frontier judge 91.5 percent of the time.

At that rate, a million checks cost a hundred and sixty dollars instead of thirty-three thousand.

---

## CARD 8 · `SCREEN + VO`

*Board:* $33,000 struck out

A cheap open model costs two hundred and sixty, so most of the saving is leaving the frontier model.

What Jev adds is the number on each box.

---

## CARD 9 · `SCREEN + VO`

*Board:* scale 0 → 1, gold line at 0.95, person / ship brackets

Draw a line at 0.95. Above it ships, and between 0.6 and 0.95 goes to a person.

---

## CARD 10 · T2 · `SCREEN + VO`

*Board:* RULE 2 writes in

Route on the probability, not on the word.

---

## CARD 11 · PANEL 3 · `SCREEN + VO`

*Board:* cake → billing / technical 0.94 / account, then 0 / 30 flagged

It always picks one of your boxes.

Testers sent a ticket classifier thirty messages that fit no box. A cake recipe came back as a technical issue at 0.94.

Not one of the thirty was flagged.

---

## CARD 12 · LIMIT · `TALKING HEAD`

It cannot return a wrong type. It can return a wrong answer in the right type, with 0.94 on it.

---

## CARD 13 · T3 · `SCREEN + VO`

*Board:* none of these box, then RULE 3 writes in

Give every question a "none of these" box.

---

## CARD 14 · END · `TALKING HEAD`

How many labelled examples you need to place that line is the next part.

Engineering track, vault link in bio.

---

## Shoot order

**Session 1, home, camera (3 cards):** 12, 14, then 1 last, warm. Stand, one person on the other side of the lens, a second of silence before and after every take.

**Session 2, home, audio only (11 cards):** 2–11, then 13, in order. Same mic, same room, straight after session 1 so the voice matches. Ten-second audio test clip first; TX auto-record on.

**Session 3, café or anywhere, screen recording:** build the canvas in board order (panel 1 → 3), pausing after each *Board* line so it can be cut to the VO takes. No voice needed.

## Captions

Cut `captions.srt` from these cards, timed to the takes. Colour tags: cyan `#00FFFF` concepts (judge, boxes, probability, System One) · red `#FF5252` the frontier bill, the weightless yes, the cake recipe · green `#4ADE80` Jev, $160, "none of these" · gold `#FFD700` T1–T3 and CTA.
