# Masters of the Way: Engineering Backlog

Site: https://peterdsouza247.github.io/masters-of-the-way/

## How to read this document

Every ticket has: a problem statement, implementation notes, named free services where third parties are needed, and acceptance criteria. Acceptance criteria are the contract. A ticket is not done until every criterion passes.

Priorities:

- **P0**: blocks credibility of the product or breaks the page. Ship before anything else.
- **P1**: revenue and audience infrastructure.
- **P2**: differentiating features. Build in listed order.
- **P3**: deferred.

Global constraint: the site is static and hosted on GitHub Pages. No server-side runtime is available. Anything dynamic must be either build-time generated, a third party embed, or a client-side call to an external API.

---

# P0: Bugs

## TI-001: A fight gets stuck in an infinite loop with players being out of range of each other

**Status: OPEN.**

**Priority:** P0

**Problem.** A fight gets stuck in an infinite loop with players being out of range of each other.

You vs Marisol "Lights Out" Reyes
You vs Marisol "Lights Out" Reyes. Touch gloves. Or don't.
Turn 1 · You · Far
You: Teep (2)
You: Low Kick (2)
Turn 2 · Marisol "Lights Out" Reyes · Far
Marisol "Lights Out" Reyes: Peek-a-Boo Guard
Marisol "Lights Out" Reyes: Bob and Weave
Marisol "Lights Out" Reyes: High Guard
Turn 3 · You · Far
You: Iron Shins
You: Long Guard
Marisol "Lights Out" Reyes counters for 3!
You: Low Kick (4)
Turn 4 · Marisol "Lights Out" Reyes · Far
Marisol "Lights Out" Reyes: Slip & Counter
Turn 5 · You · Far
You: Breathe
Turn 6 · Marisol "Lights Out" Reyes · Far
Turn 7 · You · Far
Turn 8 · Marisol "Lights Out" Reyes · Far
Turn 9 · You · Far
Turn 10 · Marisol "Lights Out" Reyes · Far
Turn 11 · You · Far
Turn 12 · Marisol "Lights Out" Reyes · Far
Turn 13 · You · Far
Turn 14 · Marisol "Lights Out" Reyes · Far
Turn 15 · You · Far
Turn 16 · Marisol "Lights Out" Reyes · Far
Turn 17 · You · Far
Turn 18 · Marisol "Lights Out" Reyes · Far
Turn 19 · You · Far
Turn 20 · Marisol "Lights Out" Reyes · Far
Turn 21 · You · Far
Turn 22 · Marisol "Lights Out" Reyes · Far
Turn 23 · You · Far
Turn 24 · Marisol "Lights Out" Reyes · Far
Turn 25 · You · Far
Turn 26 · Marisol "Lights Out" Reyes · Far
Turn 27 · You · Far

(Bug found by Kevin and Shanna - many thanks)

**Implementation.**

Need to rethink design in this case.

**Acceptance criteria.**

Need to rethink design in this case.

---

## TI-002: Forfeit option

**Status: OPEN.**

**Priority:** P0

**Problem.** There is no way to forfeit a fight.

**Implementation.**

1. Provide a forfeit option during a fight (single player mode, and pass-and-play mode).
2. Warn the player about the cost of forfeiting.
3. Ask for confirmation from the player.
4. A forfeit results in a KO for the forfeiting player (Maybe we implement another end state later, but I think a KO would deter players from forfeiting).

**Acceptance criteria.**

1. A forfeit option is available during a fight (single player mode, and pass-and-play mode).
2. A screen should warn the player about the cost of forfeiting, before allowing the player to confirm the forfeit.
3. Ask for confirmation from the player.
4. A forfeit should result in KO for the forfeiting player.

---

## TI-003: Allow two profiles in pass-and-play mode

**Status: OPEN.**

**Priority:** P0

**Problem.** There is no way for a player to load his profile in his friend's browser, play a game against that friend, and then have both players retain their individual game data (stats)

**Implementation.**

Need to rethink design in this case.

**Acceptance criteria.**

Need to rethink design in this case.

---
