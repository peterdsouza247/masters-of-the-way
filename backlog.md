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

**Status: FIXED IN CODE (needs a live playtest to confirm).**

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
Turn 6 to 27 (and onward): neither fighter plays a card, range never changes.

(Bug found by Kevin and Shanna - many thanks)

**Root cause.** Two fighters can end up at a range where every card in hand is gated to a different range, with no movement card drawn, so both sides legally play nothing turn after turn. There was no cap on turn count and no mechanism to break a stalemate, so the loop was unbounded. (Reyes' boxing strikes are all Close-only; stuck at Far with no footwork card in hand, she plays nothing. The player can be in the same spot.)

**Implementation (done).**

1. Track consecutive "no-action" turns on the match state (`M.stall`), reset whenever a fighter plays any card.
2. After each completed turn, `advanceStall()` runs:
   - If `M.stall` reaches `STALL_LIMIT` (3) and the fight is not already at Close, the referee pulls the fighters together: range is forced to Close, top/control/grip cleared, and a log line is shown ("Nothing doing at range. The referee brings them together."). The stall counter resets. This lands the fight in a range where in-close arts finally have legal cards.
   - If the stall limit is hit again while already at Close (nobody acting even in the pocket), the fight goes to the judges via `endByDecision()`.
3. Hard backstop: `MAX_TURNS` (120). If a fight ever reaches it, it resolves by decision regardless.
4. New end states: `finishMatch(winnerIdx)` and a `Decision` method. Decision winner is the higher HP; ties break on higher guard, then on the fighter not currently on the clock. No true draw state is produced, so the result/record/gauntlet flows are unaffected.
5. The same stall logic runs inside the headless balance simulator, so AI-vs-AI matchups can no longer deadlock either.

**Acceptance criteria.**

1. A fight can never continue indefinitely: a hard turn cap guarantees termination. PASS (by construction).
2. A no-progress standoff at range is broken automatically by moving the fight to Close within a few turns. PASS (by construction; needs playtest confirmation).
3. If no progress is possible even at Close, the fight ends by decision on HP. PASS (by construction).
4. The reported Reyes-at-Far scenario resolves rather than looping. NEEDS PLAYTEST.

---

## TI-002: Forfeit option

**Status: DONE IN CODE (needs a live playtest to confirm).**

**Priority:** P0

**Problem.** There is no way to forfeit a fight.

**Implementation (done).**

1. The in-duel pause menu (the "Menu" button) now offers **Forfeit the fight** in place of the old silent quit.
2. Choosing it opens a warning screen: it states that forfeiting ends the fight now and records it as a loss by knockout for the forfeiting player, with no undo, and asks for explicit confirmation ("Forfeit and take the loss" vs "Keep fighting"). The safe option is focused by default.
3. On confirm, `forfeitDuel()` sets the forfeiting player's HP to 0, sets the method to "Forfeit", and ends the match with the opponent as winner. It works in single-player (the human always forfeits, whoever's turn it is) and pass-and-play (the currently active player forfeits).
4. The fight is recorded to the fight record as a loss, updates career stats, and in a Gauntlet run a forfeit ends the run. Result screen and audio behave as for any KO.

**Acceptance criteria.**

1. A forfeit option is available during a fight (single player and pass-and-play). PASS.
2. A screen warns the player about the cost of forfeiting before allowing confirmation. PASS.
3. The player is asked to confirm. PASS.
4. A forfeit results in a KO loss for the forfeiting player (recorded). PASS.

---

## TI-003: Allow two profiles in pass-and-play mode

**Status: IMPLEMENTED (proposed design; open to change; needs a live playtest).**

**Priority:** P0

**Problem.** There is no way for a player to load his profile in his friend's browser, play a game against that friend, and then have both players retain their individual game data (stats).

**Design implemented.** The game stores one profile per browser, so "two profiles" is handled as two in-memory **seats** for the duration of a pass-and-play match, plus explicit per-profile career stats that travel in the exported profile file.

1. **Per-profile stats.** Added a `stats` block ({w, l, ko, sub}) to the profile bundle (new `motw-stats-v1` key, included in export/import). Career stats now come from this counter (with a legacy fallback deriving from the fight record). Solo and Gauntlet results increment the device profile's stats.
2. **Two-seat setup.** Choosing "Two Players" opens a setup screen with Player 1 and Player 2. Player 1 defaults to this device's profile (name, stats, decks). Either seat can **Load profile** from a `.json` file or a pasted code, which pulls in that player's name, stats, and decks for the match without touching the device's saved data. Each seat can also just be a named guest.
3. **Per-seat decks.** Deck selection for each seat offers the prebuilts plus that seat's own custom decks, so a guest brings their decks along.
4. **Stats retained after the match.** On the result screen, both seats' records are updated (winner +1 win with KO/submission split, loser +1 loss). The device seat is written back to this device automatically. Each guest seat gets **Save profile** and **Copy code** buttons to carry their updated stats away. Re-importing later merges stats (per-field max, to avoid double counting on re-import).

**Open design questions (for your call).**

- Whether hotseat results should also appear in the shared on-device Fight Record (currently yes, tagged as a two-player bout, but they do not affect the device's solo career line beyond the device seat's own stats).
- Whether to add named, persistent local profile slots (so two people who share one machine do not have to re-load files every time). This is the natural follow-up if file juggling proves annoying.

**Acceptance criteria (proposed).**

1. Each of the two players in a pass-and-play match can be a distinct profile (device or loaded). PASS.
2. Each player can bring their own decks into the match. PASS.
3. After the match, each player's individual stats are updated and can be taken away (device seat persists locally; guest seats export). PASS.
4. Loading a guest profile never overwrites the host device's saved decks or stats. PASS (guest data is in-memory only until they export).

---

# P2: Features

## TI-004: Reset stance (mulligan) when a hand is fully greyed out

**Status: DONE IN CODE (needs a live playtest to confirm).**

**Priority:** P2 (also reduces how often TI-001 can occur)

**Problem / idea.** When every card in hand is greyed out (nothing is playable at the current range), a player has no move but to end the turn, which is the situation that feeds the TI-001 standoff. Give the player a way to dig out of it.

**Design shipped.** A hand reset, not deck editing, so the deckbuilding and range-coverage meta stays intact.

1. A **Reset stance** button appears in the duel controls only when the active player has no playable card in hand.
2. Pressing it costs **1 stamina**, discards the whole hand, and redraws to hand size. It is limited to **once per turn** (`turnFlags.reset`).
3. The AI does the same automatically: when it has no legal play and has stamina to spend, it resets once before ending the turn. This is the part that actually breaks the reported Reyes-at-Far loop, since in that bug it was the AI that was stuck.
4. The referee / turn-cap backstop from TI-001 remains as the guarantee for the rare case where a reset does not help (for example both decks genuinely cannot damage each other).

**Acceptance criteria.**

1. The reset is only offered when no card is playable. PASS.
2. It costs stamina and can be used at most once per turn. PASS.
3. Both the player and the AI can use it. PASS.
4. A fighter stuck at range can escape a standoff without waiting for the referee. PASS (needs playtest).

**Watch-item.** Keep an eye on whether free-ish resets make weak-coverage decks feel too safe. If so, raise the cost or add a per-fight cap.

---
