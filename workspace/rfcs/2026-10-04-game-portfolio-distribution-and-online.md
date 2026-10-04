---
name: rfc-game-portfolio-distribution-and-online
description: RFC — where to ship the browser game portfolio (Gladiator, Greatwall, The Ladder, Slope Lab), what to expect, and how to add storage, accounts and live play
metadata:
  type: rfc
  status: draft
  date: 2026-10-04
---

# RFC: Distribution and online features for the game portfolio

**Status:** Draft for discussion. Nothing here is decided.
**Scope:** four browser games built with [kirby-game-design](../../skills/kirby-game-design/SKILL.md):

- Gladiator (`kirbisity/boxer-simulator`);
- Greatwall (`kirbisity/greatwall`);
- The Ladder (`kirbisity/the-ladder`);
- Slope Lab (`kirbisity/slope-lab`).

> **On the numbers.** Audience sizes, revenue figures and probabilities below are rough. They
> come from public reporting known up to mid-2026 and from judgement, not from data gathered for
> this RFC. Treat them as orders of magnitude for comparing options. Before committing money or
> months to a channel, check that channel's current figures.

---

## 1. Summary

- **The plan is a moonshot portfolio.** Ship several small games cheaply, watch for the one that
  players pull on, and only then invest in it. The expected value of any single game is low. It is
  dominated by a small chance of a hit.
- **Recommended path:** one web codebase per game, shipped to low-maintenance web channels first:
  the PWA on GitHub Pages, one web game portal, and itch.io. Measure the same few signals for every
  game, then promote at most one game at a time to a costlier channel:
  - **Steam** for Gladiator or Greatwall;
  - **mobile app stores** for The Ladder or Slope Lab.
- **Online features:** start with *Option A*, a small invited group, with storage and identity as
  light as possible. Asynchronous competitions (submit an army, simulate the match, rank the
  result) come before live play. Live play is a different, much harder project; defer it until
  something shows traction.

## 2. Context

### 2.1 The games today

| Game | What it is | Session shape | Tech | Heaviest cost |
|---|---|---|---|---|
| **Gladiator** | Physics fighting sandbox: XPBD ragdolls, weapons, armour, 1 v 1 up to 50 v 50, set levels, Deadliest Warrior match-ups | 1–5 min fights; sandbox play is open-ended | ES modules + three.js r128 | CPU physics: about 30 ms a frame for 100 armed fighters on a laptop |
| **Greatwall** | Wall-building siege defence and an *Open Field* mode: budget-limited armies, a placement phase, then the battle | 5–20 min levels | Vanilla ES modules | Many units on screen |
| **The Ladder** | Career and life simulator, from first job to retirement or financial independence, with events, autopilot and a shareable ending page | 10–30 min per life; replayable | ES modules, mostly UI | Light |
| **Slope Lab** | Skiing physics game: jumps, moguls, tricks, crashes | 1–3 min runs | ES modules + WebGL | Moderate |

All four games:

- are static sites, live on GitHub Pages (pushing to `main` runs the tests and deploys);
- have a review copy published as a Claude artifact;
- have no backend, no accounts and no shared storage.

Gladiator saves a setup as JSON that the player copies and pastes by hand.

### 2.2 What prompted this RFC

1. **Reach.** Can another channel bring more players than GitHub Pages: WeChat mini games, the
   iOS App Store, Steam, web portals?
2. **Online features.**
   - Shared army builds, competitions and a leaderboard (needs storage).
   - Persistent characters and careers (needs accounts).
   - Live control of fights (needs a real-time server).
   - What else storage and accounts make possible.
3. **Strategy.** With similar maintenance effort per game, which market suits each game, and what
   outcome should be expected on average across the portfolio?

### 2.3 Goals and non-goals

**Goals**

- Pick channels that maximise the chance of one breakout game for a fixed, small upkeep per game.
- Keep one codebase per game, mobile-friendly, with no per-platform fork.
- Define the signals that decide when a game gets more investment.
- Choose a storage and identity approach that starts tiny (an invited group) and can grow.

**Non-goals (for now)**

- Public accounts with sign-up, password recovery and moderation at scale.
- Payments, in-app purchases, or anything that needs a business entity.
- Live multiplayer servers.
- Releasing in China (see §3.6).

---

## 3. Distribution channels

Each channel is scored on five axes:

- **Reach:** the size of the audience.
- **Fit:** how well that audience matches these games.
- **Difficulty:** the work and cost to launch.
- **Maintenance:** the recurring work afterwards.
- **Outcome:** what a typical game earns there, and what a hit earns.

### 3.1 Mobile web / PWA (the status quo)

- **Reach:** in principle every phone and computer with a browser, so the largest possible
  audience.
- **Fit:**
  - Every game can be played instantly from a link.
  - The Ladder's shareable ending page and Gladiator's match-ups suit sharing over chat.
- **Difficulty:**
  - Very low, because it is already done.
  - Making it a PWA (a web app manifest, a service worker for offline play, an install prompt)
    takes about a day per game.
- **Maintenance:** very low. Pushing to `main` deploys.
- **Outcome:**
  - **Discovery is the problem.** With no store, no charts and no recommendations, players arrive
    only through links shared elsewhere.
  - **Typical:** a handful of players, mostly friends.
  - **A hit:** only when content goes viral on another platform (a TikTok clip, a Reddit post) and
    links back.
- **Risks:**
  - Phone browsers (iOS Safari in particular) cap memory and slow down background tabs.
  - Heavy physics scenes need the large-fight settings on mid-range phones (see §5.3).

### 3.2 Web game portals (CrazyGames, Poki, itch.io, Newgrounds)

- **Reach:**
  - CrazyGames and Poki each report tens of millions of monthly players across desktop and
    mobile web.
  - itch.io is smaller and indie-focused.
  - Newgrounds is a niche community.
- **Fit:**
  - Very good for **Slope Lab** and **Greatwall**: short sessions, instant play, a familiar
    genre.
  - Good for **Gladiator**: physics combat and battle simulators are proven portal genres.
  - Moderate for **The Ladder**: text-heavy life sims draw a smaller but loyal portal audience.
- **Difficulty:**
  - Low to medium. You add the portal's SDK (ad breaks, a loading screen, sometimes an event
    API), meet its technical checks (load time, bundle size, no external links, a mobile mode) and
    pass a quality review.
  - Poki is selective: it accepts a small share of what it is sent and often runs its own tests.
  - CrazyGames has an open submission process with staged exposure.
  - itch.io has no review at all.
- **Maintenance:** low. Upload a new build when the game changes, and keep the SDK current.
- **Outcome:**
  - Payment is a share of ad revenue, and some portals pay for exclusivity.
  - **Typical:** tens to low hundreds of dollars a month, often less, plus playtime and retention
    figures you can't get from GitHub Pages.
  - **A hit:** thousands to more than $10k a month for a top title.
  - **Most valuable side effect:** portals report play time, return rate and completion for free.
    That is exactly the signal this strategy needs (§6).
- **Risks:**
  - Ad breaks clash with long sessions (The Ladder).
  - Gore may need a toggle on general-audience portals (Gladiator's dismemberment).
  - Exclusivity terms can conflict with other channels: read them before signing.

### 3.3 Steam (PC)

- **Reach:**
  - Around 130 million monthly active users and around 40 million peak concurrent.
  - PC only; the Steam Deck counts if the game supports controllers.
- **Fit:**
  - **The strongest genre fit for Gladiator.** Physics combat sandboxes are an established,
    actively searched Steam category: Totally Accurate Battle Simulator, Gang Beasts, Half Sword
    (whose free demo spread widely), Ultimate Epic Battle Simulator.
  - **Strong for Greatwall's Open Field mode**, as an army-battle strategy game.
  - **Weak for The Ladder** (life sims are a smaller niche on PC) and for **Slope Lab** (a crowded
    arcade-sports space).
- **Difficulty:** medium.
  - A $100 app fee per game, recoupable after $1,000 in revenue.
  - Wrap the web build in Electron or Tauri (a few days, including save files and full screen).
  - Controller support for the Deck (days to weeks).
  - Store page art and a trailer.
  - A free demo (strongly recommended).
  - Steam's review of the build and the store page.
- **Maintenance:** medium.
  - Patches, the community hub and reviews, Steam features (achievements, cloud saves), and
    responding to players.
  - Store visibility rewards regular updates, so maintenance is a big part of how a Steam game is
    seen.
- **Outcome:**
  - **Releases:** roughly 15,000–19,000 games launch each year.
  - **Typical:** about half of releases earn under a few thousand dollars over their lifetime, and
    many earn under $1,000. Revenue is heavily concentrated in the top few percent.
  - **Pre-launch signal:** wishlists. Around 7,000 at launch is commonly treated as a solid start,
    and Next Fest (Steam's demo festival) is the main free way to gather them.
  - **A hit** in this genre earns hundreds of thousands to millions of dollars.
- **Risks:**
  - A Steam game is judged as a product: polish, content depth and a trailer matter more than on
    the web.
  - Electron builds are large (hundreds of MB).
  - Physics performance must hold on low-end PCs.

### 3.4 iOS and Android app stores

- **Reach:** about 1 billion active iPhones and about 3 billion Android devices.
- **Fit:**
  - **Good for The Ladder.** Life sims are a large mobile genre; BitLife is the reference title.
  - **Good for Slope Lab.** One-thumb arcade sports.
  - **Moderate for Gladiator and Greatwall:** heavy scenes, and touch controls that suit
    watching and placing units more than fine combat.
- **Difficulty:** medium.
  - Wrap the web build with Capacitor (a WKWebView on iOS, a WebView on Android): a few days.
  - Developer accounts: Apple $99 a year, Google $25 once.
  - App review, with privacy labels and an age rating. Gore lowers the age rating.
  - Icons, screenshots and a store listing.
- **Maintenance:** medium to high.
  - Two stores, and new OS releases that break web views.
  - Apple's review times and policy changes.
  - Yearly SDK target updates on Google Play.
- **Outcome:**
  - Without paid advertising, a new app is close to invisible.
  - **Typical:** near zero.
  - **Hits:** almost always built with paid installs and tuned monetisation (ads, in-app
    purchases).
  - The app stores make sense only after a game has shown retention elsewhere.
- **Risks:**
  - **Wrapping a web site may be rejected.** Apple's guideline 4.2 rejects apps that are "just a
    website", so the app needs native-feeling features: offline play, haptics, Game Center.
  - **Revenue and payments.** Store fees are 15–30%, and in-app purchases need a payments setup.

### 3.5 Social platforms: Discord Activities, Telegram Mini Apps

- **Reach:**
  - Discord: about 150–200 million monthly users.
  - Telegram: about 900 million monthly users.
- **Fit:**
  - **Discord Activities** run HTML5 games inside voice channels, so friends play or watch
    together. This is a natural home for Gladiator's Deadliest Warrior bets and army competitions,
    and for watching a fight together.
  - **Telegram Mini Apps** suit casual games and have a viral referral culture.
- **Difficulty:**
  - Medium: the platform SDK, its authentication, and for Discord a small backend to exchange
    tokens.
  - **Bonus:** both platforms supply user identity, which partly solves accounts (§4.3).
- **Maintenance:** low to medium.
- **Outcome:**
  - An early-stage market; discovery depends on communities and servers adopting the game.
  - Hard to predict. The upside is social virality within a group.
- **Risks:**
  - Platform policy churn.
  - Activities still need a server for anything shared.

### 3.6 WeChat mini games (China)

- **Reach:** WeChat has about 1.3–1.4 billion monthly users, and mini games report hundreds of
  millions of monthly players. It is the largest single casual-game channel.
- **Fit:** technically good. Mini games run JavaScript and WebGL, three.js runs with an adapter,
  and short sessions suit Slope Lab and Greatwall.
- **Difficulty:** very high for a foreign individual developer.
  - **Entity:** publishing generally needs a mainland Chinese business entity or a publishing
    partner.
  - **Licence:** monetised games need a government game licence (版号), a long and uncertain
    process.
  - **Content:**
    - blood, dismemberment and some historical subjects are restricted, so Gladiator would need a
      no-gore build;
    - Sekigahara and other Japanese war scenes may draw scrutiny.
  - **Packaging:** the package has small size limits (a few MB for the main package; subpackages
    extend that).
  - **Language:** Chinese localisation.
- **Maintenance:** medium to high.
  - Platform reviews on every update.
  - A separate build.
- **Outcome:**
  - **Typical:** unreachable without a partner.
  - **With one:** potentially the largest audience of any option.
- **Recommendation:** out of scope until a game proves itself, and then only through a Chinese
  publisher.

### 3.7 Channel comparison

| Channel | Reach | Best-fit games | Difficulty to launch | Maintenance | Typical outcome | Upside |
|---|---|---|---|---|---|---|
| Web/PWA | Very large in principle, tiny in practice | All | Very low (done) | Very low | Friends only | Only through viral content elsewhere |
| Web portals | Tens of millions | Slope Lab, Greatwall, Gladiator | Low–medium | Low | $10–$300 a month | $1k–$10k+ a month |
| Steam | ~130M, actively searching | Gladiator, Greatwall | Medium | Medium | Under a few thousand dollars lifetime | Six to seven figures |
| App stores | Billions | The Ladder, Slope Lab | Medium | Medium–high | Close to zero without paid ads | Large, usually with paid ads |
| Discord / Telegram | Hundreds of millions | Gladiator (social), The Ladder | Medium | Low–medium | Hard to predict | Viral within groups |
| WeChat | ~1.3B | Slope Lab, Greatwall | Very high | Medium–high | Not reachable alone | Largest audience, with a partner |

### 3.8 Each game's best channels

| Game | First (cheap signal) | Promote to, if signal | Why |
|---|---|---|---|
| **Gladiator** | Web portal + itch.io; clips on TikTok, YouTube and Reddit | **Steam** (demo → Next Fest → launch) | A proven Steam genre; the clips sell it |
| **Greatwall** | Web portal | **Steam** (Open Field as an army-battle game) or stay on portals | Strategy players on PC; portals suit siege levels |
| **The Ladder** | Mobile web/PWA + a portal | **App stores** | The life-sim audience is on phones; the ending page spreads |
| **Slope Lab** | Web portal | **App stores** | Short sessions suit one thumb |

---

## 4. Online features: storage, accounts, live play

### 4.1 Scope by audience

| Option | Audience | Storage and identity | Load on you |
|---|---|---|---|
| **A** (chosen for now) | You and people you invite | The lightest that works | Close to none |
| **B** | The public | A real backend: sign-up, abuse and cheat protection, moderation | Ongoing: servers, security, support |
| **C** | A first, built so it can grow into B | As A, behind an interface | Low now, migration later |

Option A is chosen. Where it costs little extra, the designs below keep a path to B (in effect,
option C).

### 4.2 Storage options for Option A

| Option | How | Difficulty | Maintenance | Cost | Limits |
|---|---|---|---|---|---|
| **S1. Artifact runtime storage** | Publish the game as a Claude artifact with the shared-database and viewer-identity capabilities, where they are enabled for the account | Low: no server, identity built in | Very low | None | Only viewers the artifact is shared with; tied to claude.ai; size and feature limits; not available on GitHub Pages or other channels |
| **S2. Backend as a service** (Supabase, Firebase) | A hosted Postgres or document store, auth providers and row-level security, called from the static site | Low–medium | Low (the provider runs it) | Free tier, then per use | Vendor lock-in; security rules must be correct; works on every channel |
| **S3. Serverless functions + a key-value store** (Cloudflare Workers + D1/KV, Vercel) | Small API endpoints in front of storage | Medium | Low–medium | Free tier, then small | You write the API and auth; most flexible |
| **S4. Git as the database** (a JSON file per submission, sent as a PR or GitHub issue) | Players submit builds; a workflow validates them and runs the competition | Low | Low, but manual | None | Only for players with GitHub accounts; slow; friends only |
| **S5. Own server** (Node + Postgres on a VPS) | Full control | High | High: patching, backups, uptime | $5–$50 a month | Only worth it for live play (§4.5) |

**Recommendation for A:**

- **S1** to try it out within the group at no cost.
- Hide all storage behind a small `store` interface (`saveBuild`, `listBuilds`, `submitEntry`,
  `recordResult`, `leaderboard`), so a move to **S2** for web channels or Option B touches one
  module.
- **S4** is a viable fallback if S1 lacks a capability.

### 4.3 Identity and accounts

| Option | How | Difficulty | Maintenance | Notes |
|---|---|---|---|---|
| **I1. Platform identity** | The claude.ai viewer (S1), a Discord or Telegram user, a Steam account, Game Center | Low | Very low | Comes with the channel; no passwords for you to hold |
| **I2. Magic link or OAuth through a backend service** | Supabase or Firebase auth (Google, Apple, email link) | Low–medium | Low | Standard for B; needs privacy terms |
| **I3. Device ID + recovery code** | Anonymous ID in local storage, with a code shown to move between devices | Low | Low | Lose the code and the progress is gone; good enough for a career save in A |
| **I4. Own accounts** | Passwords, resets, sessions | High | High | Avoid: security risk with no benefit at this scale |

**Recommendation:** I1 for Option A (from S1); I2 when a game moves to the public; never I4.

### 4.4 Asynchronous competitions: shared builds, tournaments, leaderboard

The games already suit asynchronous competition:

- **Gladiator** fights are a deterministic simulation: a seed plus two rosters always give the
  same result.
- **Greatwall's Open Field** has budget-limited armies by design.

**Flow:**

1. A player builds an army within a budget and submits it as JSON, with a version and a checksum.
2. A runner simulates entries against each other: a round robin, a ladder, or a weekly cup.
3. Results and replays (seed + rosters + engine version) are stored.
4. The leaderboard ranks entries by Elo or Glicko, or by points in a season.

**Who runs the matches:**

| Option | How | Trust | Difficulty | Maintenance |
|---|---|---|---|---|
| **R1. The viewer's browser** | Whoever opens the page simulates the pending matches and writes the results | Low: a cheater can write false results (acceptable among friends) | Low | Very low |
| **R2. Scheduled runner** | A GitHub Action or cron job runs Node headless (the physics already runs in Node: `tools/*.js`) and writes the results | High | Low–medium | Low |
| **R3. Replay check** | A result is accepted only if a second, independent run reproduces it | High | Medium | Low |

**The determinism caveat:**

- Basic JavaScript arithmetic is IEEE 754 and gives the same result everywhere.
- `Math.sin`, `cos`, `exp`, `pow` and `hypot` may differ in the last bit between engines (V8,
  JavaScriptCore, SpiderMonkey).
- Chaotic physics turns a last-bit difference into a different winner.

So a result is only reproducible on the engine and **engine version** that produced it. This
leads to three rules:

- Make **R2** (one runner, pinned Node version) the authority for ranked results.
- Store replays as inputs, never as outcomes.
- Stamp every result with the game version. A physics change starts a new season.

**Difficulty:** low to medium for Gladiator. The JSON setups and the headless simulation exist
already; the work is the store, a runner script, a leaderboard page and a replay viewer.

### 4.5 Live play: controlling fights in real time

| Option | How | Difficulty | Maintenance | Cost | Fit |
|---|---|---|---|---|---|
| **L1. Same screen** | Two players on one device (split controls, or taking turns) | Low | Very low | None | A quick, cheap way to see whether live play is fun |
| **L2. Peer-to-peer lockstep** | Send only inputs over WebRTC; both browsers run the simulation | High | Medium | A signalling server, TURN relay | **Breaks on engine differences** (§4.4): Chrome against Safari drifts apart. Needs a fixed-point or engine-independent maths layer. The artifact frame blocks WebRTC. |
| **L3. Host-authoritative peer-to-peer** | One player's browser simulates and streams state to the others | Medium–high | Medium | Signalling + TURN | No drift; the host has the advantage and can cheat; ~15 particles × fighters × 60 Hz needs compression |
| **L4. Authoritative server** | Node runs the physics; clients send inputs and receive state snapshots | High | High | CPU-heavy: a 100-fighter fight is ~30 ms a frame, about one core per big match | Correct and cheat-proof; the most expensive to run; the standard for public PvP |
| **L5. Turn-based or command-based live play** | Players issue orders (formations, targets, retreat) at a slow tick; the simulation runs on one machine | Medium | Medium | Low | Suits Greatwall and army battles; tolerates latency |

**Recommendation:**

- Defer live play.
- If it is tried, start with **L1** to learn whether it is fun, then **L5** for army games.
- Consider **L4** only if a game reaches public scale with demand for PvP.
- Avoid **L2** unless the physics moves to engine-independent maths, which would be a large
  refactor.

### 4.6 What storage and accounts make possible

| Mechanism | Needs | Effort | Why it matters |
|---|---|---|---|
| **Cloud saves and career resume** | Storage + identity | Low | Replaces copy-paste JSON; enables a career mode (fighters with records, injuries, ageing) |
| **Shared builds** (a gallery of armies and fighters) | Storage | Low | Players create content; one player's design is another's opponent |
| **Asynchronous PvP** (submit a defence, others attack it) | Storage + runner | Medium | Competition without live servers; Greatwall siege defences suit it |
| **Daily or weekly challenge** (the same seed for everyone, one leaderboard) | Storage | Low | A reason to come back; cheap to make |
| **Seasons and ranked ladders** (Elo or Glicko, reset each version) | Storage + runner | Medium | Long-term goals; tidy handling of physics changes |
| **Replays and clip links** (a short link to seed + rosters + camera) | Storage | Low–medium | **The best growth lever:** a shareable clip of a fight brings players for free |
| **Ghosts** (race another player's run) | Storage | Low | Slope Lab: compete against friends' best runs |
| **Spectating and betting with play money** | Storage + live or async | Medium | Deadliest Warrior bets; Discord watch parties |
| **Telemetry for balance** (anonymous outcomes from real games) | Storage | Low | The balance tools today run bots; real outcomes calibrate them ([kirby-game-design](../../skills/kirby-game-design/SKILL.md), "Calibrate ratings by simulation") |
| **A profile across games** (one identity, achievements across all four) | Identity | Medium | Players of one game find the others |
| **Community curation** (likes, featured builds, remixes) | Storage + moderation | Medium | Content without writing it; needs moderation in Option B |

---

## 5. Difficulty, maintenance and performance across the portfolio

### 5.1 One-time work, per game

| Work | Gladiator | Greatwall | The Ladder | Slope Lab |
|---|---|---|---|---|
| PWA (manifest, offline, install) | 1 day | 1 day | 1 day | 1 day |
| Portal SDK and review | 2–4 days (+ gore toggle) | 2–4 days | 2–3 days | 2–3 days |
| Steam wrapper, store page, demo | 2–4 weeks | 2–4 weeks | — | — |
| App store wrapper and listing | 1–2 weeks (touch controls) | 1–2 weeks | 1 week | 1 week |
| Storage + identity (S1/S2, I1/I2) behind `store` | shared: 1 week once, then 1–2 days per game | | | |
| Async competitions + leaderboard | 1–2 weeks | 1–2 weeks | — | 1 week (ghosts) |

### 5.2 Ongoing upkeep, per game per month

| Channel | Upkeep |
|---|---|
| Web/PWA | ~0–2 h (deploys are automatic) |
| Portal | ~1–3 h (builds, SDK updates, reading the analytics) |
| Steam | ~8–20 h (patches, community, events, store) |
| App stores | ~5–15 h (two stores, OS updates, reviews) |
| Storage S1/S2 | ~1–2 h (quotas, schema changes); more under Option B (moderation, abuse) |
| Live server L4 | ~10–30 h + hosting (uptime, scaling, cheating) |

**Portfolio budget:**

- With all four games on web, PWA and a portal, upkeep is a few hours a month in total.
- Promoting one game to Steam or the app stores adds roughly a part-time week each month.
- Only one game should be promoted at a time.

### 5.3 Performance on phones (an estimate, to be measured)

- A phone's JavaScript is perhaps 2–4 times slower than the reference laptop.
- **Gladiator** at 80–100 fighters would need tier-4 settings or a lower cap on mid-range phones;
  1 v 1 to 16-fighter fights should be fine.
- **Greatwall's** unit counts need the same check.
- **The Ladder** and **Slope Lab** are likely fine.

Action: add a device-class check that caps crowd sizes, and measure on a real mid-range Android
phone before any mobile push.

---

## 6. Expected outcomes and the portfolio strategy

### 6.1 Base rates

These are judgement figures for a small, unmarketed indie game, to frame expectations, not to
forecast:

| Outcome per game (first year) | Rough chance | What it looks like |
|---|---|---|
| **Flop** | ~70–80% | Hundreds to low thousands of players; under $500 |
| **Modest** | ~15–25% | Tens of thousands of players; $1k–$20k; a small community |
| **Breakout** | ~1–5% | Hundreds of thousands of players or more; $50k to seven figures (Steam or app stores) |

With four games, the chance that **at least one** breaks out is roughly 1 − (0.97)^4 ≈ 10–15%,
assuming the chances are independent and a few percent each. Breakouts usually come from content
spreading in a way nobody can plan, so the strategy is to **give each game many cheap chances**:

- clips;
- portals;
- seasonal events;
- a social platform.

Big bets on any one game don't fit that.

### 6.2 Strategy options

| Strategy | What | Upside | Risk / cost |
|---|---|---|---|
| **P1. Funnel** (recommended) | All four on web, PWA and a portal; measure; promote the game with the strongest signal to Steam or the app stores | Cheap; signal-driven; reuses one codebase | Slower; a promoted game still needs polish |
| **P2. Single bet** | Take Gladiator to Steam now (demo + Next Fest) | Best genre fit; fastest to the biggest upside | Weeks of work before any signal; the other three stall |
| **P3. Everywhere at once** | Every game on every channel | Most chances | Maintenance multiplies (4 games × 4 channels); quality suffers |
| **P4. Mobile first** | The Ladder and Slope Lab into the app stores | The largest raw audience | Near zero without paid ads; review friction |
| **P5. Social first** | Discord Activity for Gladiator and Greatwall | Group virality; identity included | An early market; needs a small backend |

### 6.3 Signals that trigger promotion

Measured the same way for every game, mostly from portal analytics:

| Signal | Promote when (rough) |
|---|---|
| Average session length | Over 8–10 minutes |
| Day-1 return rate | Over 25–30% |
| Sessions per returning player per week | Over 3 |
| Organic shares (links, clips) per 100 players | Rising week on week |
| Gladiator and Greatwall only: Steam wishlists once a page exists | Over 2,000 before Next Fest; over 7,000 at launch |

If a game shows no improvement in these numbers after a fixed window (for example 6–8 weeks after
the portal launch), stop investing in it and fold its reusable parts into the shared base.

### 6.4 Raising the odds cheaply

- **Gladiator clips:**
  - an instant-replay button;
  - "save this fight" as a short link (§4.6);
  - match-ups that make people curious ("2 knights vs 20 peasants", "50 ashigaru vs 5 samurai").
- **The Ladder:** the shareable ending page is already the growth hook; make it one tap to share.
- **Slope Lab:** ghosts and a daily slope.
- **Greatwall:** weekly siege challenges with a leaderboard.
- **Across the games:** a shared "more games" link and cross-promotion.

---

## 7. Recommendation

1. **Now:**
   - Add PWA support to all four games.
   - Submit to one portal (CrazyGames first: open submissions with analytics) and to itch.io.
   - Add a gore toggle to Gladiator.
2. **Option A online (for Gladiator first):**
   - a `store` interface backed by S1 (artifact storage) with I1 identity;
   - shared armies;
   - an asynchronous weekly cup run by R2 (a pinned-Node GitHub Action);
   - a leaderboard;
   - replay links.
3. **Measure 6–8 weeks** against §6.3.
4. **Promote one game:**
   - Gladiator to a Steam demo and Next Fest if it shows signal;
   - otherwise whichever game leads, on its best channel (§3.8).
5. **Defer:**
   - live servers (L4);
   - public accounts (Option B, with S2/I2);
   - WeChat (only with a partner).

## 8. Open questions

1. **Option A build order:**
   - A1: shared armies and competitions first;
   - A2: personal career saves first;
   - A3: both together.
2. **Gore policy:** a toggle (default on or off?), or a separate no-gore build for portals and
   stores?
3. **Money:** is revenue a goal for the first phase, or only players and signal? This decides
   whether to add portal ad SDKs now.
4. **Steam timing:** does Gladiator aim for a specific Next Fest edition? That fixes a date for the
   demo.
5. **One identity across the four games** from the start, or per game?

## 9. Risks

| Risk | Mitigation |
|---|---|
| Physics changes invalidate stored results and replays | Version every replay; start a new season per engine version |
| Results differ between engines, causing disputes | Ranked results come only from the R2 runner on a pinned Node version |
| The storage provider's limits or terms change | The `store` interface keeps the backend replaceable |
| Gore blocks portal or store approval | A gore toggle; age ratings |
| Maintenance grows past the budget | One promoted game at a time; a fixed window, then stop |
| Phones can't run the big scenes | A device-class cap on fighter counts, measured on real hardware |
