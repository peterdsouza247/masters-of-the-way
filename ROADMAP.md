# Masters of the Way — public roadmap

The browser game is playable now. This roadmap describes a direction, not a release
schedule or a promise that every idea will ship. Player feedback and available
funding will decide the order and scope.

## Now: browser playtest on itch.io

- Publish the current HTML5 game as a free browser playtest.
- Verify stalemate detection, forfeit, tutorial, Gauntlet, local two-player
  profile handoff, and profile export/import in itch's embedded player.
- Track where players get confused, whether they finish a duel, which arts they
  choose, and whether they return for another run.
- Improve balance and explain range, grappling, and submissions from real
  playtest reports. Keep keyboard, controller, touch, and reduced-motion support.
- Review martial-arts terminology and portrayals with practitioners before a
  commercial release.

## 1. Private online matches

- Start with invite-only two-player rooms: create a match, share a short code
  or link, choose decks, and play. Keep local two-player available.
- Move turn authority to a small server. It validates actions, keeps hands and
  deck order private, and sends each player only the information they may see.
  The browser clients render the same fight events and never decide the result
  independently.
- Add reconnect, a turn timer, forfeit, version checks, and sensible handling
  for a player who leaves. Save completed online fights to each profile's
  record with a clear distinction from local and AI matches.
- Test on phones and in the itch embed, including a disconnected player,
  duplicate taps, refreshes, and mismatched client versions. Public matchmaking,
  accounts, rankings, and moderation are separate decisions after private
  matches work. A live server brings hosting and support costs.

## 2. New fighting styles

- Add one style at a time only when it creates a different tactical problem
  across Far, Close, and Ground. Wrestling is the first candidate: pressure,
  takedown chains, and positional control should distinguish it from Judo's
  throws and BJJ's submissions.
- Prototype the passive, ten-card pool, mastery choices, AI behavior, tutorial
  explanation, portraits, and audio cues together. Check pure and mixed decks.
- Measure matchups, turn length, dead hands, and dominant combos before adding
  the next style. Potential later candidates include fencing-inspired footwork
  or a distinct striking art, subject to research and practitioner review.
  Avoid adding styles as cosmetic card packs.

## 3. Richer fight presentation

- Keep one combat ruleset and emit a consistent stream of events (move, block,
  hit, throw, submission, knockout). Renderers interpret those events without
  altering match outcomes or timing.
- Begin with a richer 16-bit-inspired sprite mode, readable silhouettes,
  stronger anticipation/impact frames, and stage animation. Retain the current
  compact pixel mode as an option.
- Explore 32-bit arcade-inspired, 64-bit early low-poly, and progressively
  richer 128-bit/256-bit-inspired presentations only if art and animation
  funding permits. These labels describe visual eras, not literal output
  resolution or a technical guarantee. Define each style with a small playable
  scene and budget before committing to a complete roster.
- Preserve clarity, reduced-motion settings, performance on modest phones,
  and parity of information across presentation modes. Cosmetics must never
  hide actionable cues.

## 4. Deeper character customization

- Start with profile-linked cosmetic choices: palette, outfit pieces, hair,
  portrait details, and introduction card. Give each choice a readable preview
  in the active presentation mode.
- Expand into earned cosmetics and fight introductions only after the base
  roster and online identities work. Keep unlocks portable through profile
  export/import, and keep all fighting stats and card access fair.
- Let players name and save multiple fighters or loadouts once the UI can
  distinguish them clearly in local and online match records.

## Possible board-game spin-off

Prototype a separate tactical board game built around martial-arts matchups.
Fighters occupy a compact board; a clash resolves from style, stance, stamina,
terrain, and a small tactical commitment. The outcome changes board control.
Use an original title, roster, rules, and presentation. First test it as a
short local two-player browser prototype with AI and a replayable match log;
consider online rooms only if the board play earns them. It may share profile
and accessibility components with Masters of the Way, but should remain its
own game and release.

## Possible premium desktop game

A paid edition needs a distinct experience beyond the free browser duels.
A career or tournament mode with rivals, progression, and meaningful deck
decisions between fights remains the leading candidate. Package a focused
desktop demo and scope it from playtest results.

## Other possibilities

- An Android edition tested for sustained touch play on phones.
- Public online matchmaking and competitive seasons if private matches
  demonstrate enough demand to support ongoing operations.

This page will change as the game changes. Feedback: peterbrendanwrites@gmail.com.
