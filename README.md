# Masters of the Way
## Game Design Document

| | |
|---|---|
| **Genre** | 1v1 card battler / deck builder |
| **Theme** | Real martial arts, treated with respect and mechanical honesty |
| **Platform** | HTML5, single file, desktop and mobile browsers |
| **Session length** | 5 to 10 minutes per duel |
| **Players** | Solo vs AI; local 2P pass-and-play |
| **Status** | Playable proof of concept (`[masters_of_the_way.html](https://peterdsouza247.github.io/masters-of-the-way/)`) |

---

## 1. High Concept

One-on-one martial arts duels where decks are built from six real arts, each with a genuine mechanical identity drawn from how the art actually works. The central tension is the oldest argument in martial arts: master one way, or take what works from everywhere. Both are viable. Neither is free.

---

## 2. Design Pillars

1. **Real arts, real identities.** Karate is precision first strikes. Judo converts standing position into ground dominance. BJJ wins the floor. Boxing owns the pocket. Muay Thai traps you in the clinch and bleeds you. Taekwondo snipes from range. Techniques use real names (Uchi-mata, Dwi Chagi, Juji-gatame).
2. **Purity versus cross-training is the meta.** A deck 75 percent one art earns that art's mastery passive plus two master cards. A mixed deck masters nothing but draws a bigger hand (4 + 1 per art, capped at 7) and covers every range. Same-art cards played consecutively also combo for bonus damage.
3. **Range is the battlefield.** Far, Close, Ground (with top position). Cards are range-gated; arts fight to drag the duel into their range. Winning the range argument is winning the fight.
4. **Styles make fights.** Seven AI opponents with distinct personalities (aggression, preferred range) that drive visibly different behavior.

---

## 3. Core Loop

```
Deck build (or pick prebuilt)
  -> Duel: per turn draw to hand size, spend 3 stamina on cards
     -> strikes, guards, movement, grapples, submissions
     -> statuses: stagger, bleed, clinch, grip, control, counter
  -> Win by KO (30 HP) or submission (tap threshold)
  -> Fight recorded to persistent Fight Record
```

---

## 4. Systems

### 4.1 The six arts
Each art has 8 base cards (max 2 copies) plus 2 master cards (max 1, purity-locked), and one mastery passive:

| Art | Identity | Mastery passive |
|---|---|---|
| Boxing | Cheap fast hands, guards, counters | +1 Guard each turn |
| Karate | Decisive single strikes, distance control both ways | First strike each turn +2 |
| Taekwondo | Far-range kick chains, guard breaking | Strikes at Far +1 |
| Muay Thai | Clinch control, elbows, bleed | Bleed effects +1 |
| Judo | Grips and throws; standing becomes ground on your terms | Takedowns also stagger |
| BJJ | Sweeps, positional control, submissions | Submissions +2 |

Plus 4 neutral Fundamentals cards that never count against purity.

### 4.2 Combat model
20-card decks, 30 HP, 3 stamina per turn, guard resets at the start of your own turn. Submissions deal damage and force a tap if the opponent falls at or below a card-specific threshold. Bonds of statuses give each art its texture: the Plum prevents range changes, leg kicks stagger on repeat, Kumi-kata powers the next throw, Control amplifies ground offense.

### 4.3 AI
Greedy scorer over playable cards with personality weights: aggression scales damage value, preferred range scores movement, lethal lines get finisher bonuses, submissions spike when a tap is live. Rosa pulls guard and sweeps; Somchai hunts the clinch; Reyes counters in the pocket.

### 4.4 Persistence
Multiple named deck slots (save / load / delete, overwrite confirmation), and a Fight Record of the last 25 bouts storing result, method, length, and the complete turn-by-turn log, reviewable any time. Full fight log also available live during a duel and from the result screen.

---

## 5. Content Inventory (current build)

52 unique cards, 6 mastery passives, 7 prebuilt decks (6 pure, 1 MMA mix), 7 AI fighters with bios and signature quotes, SVG portrait set, hotseat mode with hand-hiding pass screen.

---

## 6. UX and Presentation

Dojo-dark palette with per-art card colors. SVG fighter portraits. Turn banners, KO / Tap Out punch-in on the result screen, impact flashes, screen shake, card play animations, pulsing low-HP bars. Mobile: 3-across cards, full-width end turn, 44px+ touch targets. Reduced-motion supported.

---

## 7. Balance Framework

- Pure deck baseline: hand 5, mastery, easy combos. Mixed 3-art deck: hand 7, full range coverage, no mastery. Target within 5 percent win rate of each other across matchups.
- Range dominance should decide about 60 percent of duels; raw curve efficiency the rest.
- Submissions are the aggressive-BJJ win condition; tap thresholds (6 to 8 HP) keep them finishers, not openers.
- Known watch items for the next pass: Widowmaker plus Boxing burst; Judo grip-throw tempo; whether Clinch needs a counter beyond Break Posture.

---

## 8. Production Roadmap (post-POC)

1. **More arts:** Wrestling (takedown chains), Aikido (redirection counters), Kyokushin, Capoeira (movement tricks). Each must bring a new verb, not a new number.
2. **Career mode:** tournament ladder, deck rewards between rounds, rival storylines.
3. **Async or live multiplayer** once the loop is validated with real players.
4. **Presentation:** fighter animation vignettes on big hits, crowd audio, stadium themes per fighter.

## 9. Risks

Cultural respect is non-negotiable: technique names and art identities need review by practitioners before any commercial release. Balance across purity levels is the permanent live-ops workload. Grappling legibility for players who don't train is the biggest onboarding risk; the tutorial fight should be vs Rosa for exactly this reason.
