---
name: rfc-game-marketing-framework
description: RFC — a staged decision framework for marketing a portfolio of small browser games, from a friends beta to paid tests, with tradeoffs, budgets, metrics and creative tactics
metadata:
  type: rfc
  status: draft
  date: 2026-10-04
---

# RFC: A marketing decision framework for the game portfolio

**Status:** Draft for discussion. This is a framework for making marketing decisions, not a
decision about any one game.
**Companion:** [Distribution and online features](2026-10-04-game-portfolio-distribution-and-online.md).
That RFC decides *where* games are published; this one decides *how players find them* and
*when to spend*.
**Applies to:** any game in the portfolio. Today that is Gladiator, Greatwall, The Ladder and
Slope Lab.

> **On the numbers.** Costs, rates and sample sizes are rough orders of magnitude from public
> reporting known up to mid-2026 and from judgement. They exist to compare options and set
> stop-loss limits, not to forecast. Replace them with your own measurements after the first test
> on each channel.

---

## 1. Summary

- Marketing a portfolio of small games is a search under uncertainty. The job is to learn **which
  game, which message and which channel** pull players, at the lowest cost per lesson, and then
  push only what has shown pull.
- **The framework has five stages:**
  1. friends beta;
  2. strangers playtest;
  3. free community seeding;
  4. paid tests;
  5. scale.

  Each stage has a question it answers, metrics, a budget, entry criteria and stop criteria. A game
  moves forward only when the current stage's signal clears its bar.
- **Paid ads come late and start small.** The games earn little per player (§6.2), so early paid
  ads buy *information*, not profit. Four budget options (§6.4), from nothing to about $2,000,
  differ in what they can tell you.
- **Several creative, low-cost tactics** suit these games (§5). The strongest: automated clips from
  the deterministic simulation, audience-voted match-ups, history and hobby communities, and the
  "built with AI" development story.

## 2. Context and constraints

- **Starting point:**
  - four browser games, live on GitHub Pages;
  - no audience, no mailing list, no social accounts dedicated to the games;
  - no revenue.
- **Time is the scarce resource.** One person, with games also still being developed. Any tactic
  is priced in hours a week as well as dollars.
- **Content constraints:**
  - Gladiator has blood and dismemberment. Ad platforms (Meta, TikTok, Google) restrict graphic
    violence in ad creative, so paid ads need gore-free cuts.
  - Organic posts on some communities need content warnings.
- **Distribution:** the companion RFC recommends the web/PWA version, one portal and itch.io first,
  and Steam or the app stores for a game that shows signal. Marketing should send players to
  wherever the game can be measured.

### Goals

- A repeatable way to decide where the next hour or dollar of marketing goes.
- Kill criteria fixed in advance, so no game or channel drains time on hope alone.
- Comparable measurements across games.

### Non-goals

- Brand building, press relations at scale, paid user acquisition for profit (until §4.5's
  conditions hold).
- Choosing the lead game. The framework's measurements choose it.

---

## 3. Metrics: what is measured, the same way for every game

| Stage of the player funnel | Metric | Where it comes from | Rough "good" for a small web game |
|---|---|---|---|
| **Seen** | Impressions, views | Platform analytics (Reddit, TikTok, YouTube, portal) | — |
| **Interested** | Click-through rate (CTR) | Platform analytics | Ads: 0.5–2%; organic posts vary widely |
| **Arrived** | Cost per visitor (CPV) or per install (CPI) | Ad platform + game analytics | Web: $0.05–0.50; mobile install: $0.50–5 (lower outside the US and western Europe) |
| **Played** | Started a session; first-session length | Game telemetry | More than 60% start; first session over 5 minutes |
| **Returned** | Day-1 / day-7 return | Game telemetry or portal | D1 over 25–30%, D7 over 8–10% |
| **Spread** | Shares per player (K-factor); links followed | Share links with tags (`?src=`) | K over 0.1 is notable; over 0.5 is viral |
| **Wanted** (Steam) | Wishlists; cost per wishlist | Steamworks | $0.50–3 per wishlist from ads; 7,000+ at launch is solid |
| **Earned** | Revenue per player (ARPU) | Portal or ad network; store | Web ads: ~$0.01–0.05 per player; paid PC game: price × conversion |

**Instrumentation needed (one time, shared across games):**

- a share link carrying a source tag;
- a minimal anonymous event log: session start, session length, return visit, share;
- a per-game dashboard.

The storage options in the companion RFC (S1/S2) cover this. Portal analytics cover the rest for
portal players.

**The rule:** judge by **behaviour** (returns, session length, shares), not opinions. Friends say
they like it; returns tell you whether they do.

---

## 4. The staged framework

```
[1] Friends beta ──► [2] Strangers playtest ──► [3] Community seeding ──► [4] Paid tests ──► [5] Scale
     free               free / tiny                 free (time)              $0–2k            only if paid
     is it fun?         is it fun to people         which message and         what does a       players pay back
                        who don't know you?         community pulls?          player cost?
```

At every stage:

- run 1–4 games in parallel;
- move a game on only when it clears the stage's bar;
- stop at the stop criteria.

### 4.1 Stage 1: Friends beta

**The question:** is it understandable and fun enough to show strangers?

**Options:**

| Option | How | Pros | Cons | Effort |
|---|---|---|---|---|
| **1a. Open link** | Send the link to 10–30 friends: "tell me what you think" | Zero setup | Polite feedback; little data; most won't play | ~1 h |
| **1b. Structured playtest** (recommended) | 5–10 friends, a short task ("try to win Sekigahara as red"), watched live or screen-recorded, a 3-question survey afterwards | Shows confusion and drop-off points; high signal per person | Scheduling; 30–60 min each | ~5–10 h per game |
| **1c. Private Discord or group chat** | A beta channel per game, with builds posted and feedback threads | Ongoing; becomes the core of a community | Must be tended; can go quiet | ~1–2 h a week |
| **1d. Telemetry-only beta** | Share widely; measure session length and returns, ask nothing | Unbiased behaviour | No "why" | Needs instrumentation (§3) |

**Biases to correct for:**

- Friends are kind, aren't the target audience, and try harder than strangers.
- So watch **what they do** rather than what they say.
- Ask questions that are hard to answer politely:
  - "Would you send this to someone? Who?"
  - "What would you search for to find this game?"
  - "What almost made you stop?"

**Move on when:**

- most testers understand the goal without help;
- at least one tester plays again unprompted;
- the stop-points are fixed.

**Stop or rework when:** testers can't say what the game is after five minutes, even after two
rounds of fixes.

### 4.2 Stage 2: Strangers playtest

**The question:** does it hold people who owe you nothing?

**Options:**

| Option | How | Cost | Signal |
|---|---|---|---|
| **2a. Playtest communities** | r/playmygame, r/WebGames, r/indiegaming feedback threads, itch.io devlogs, Discord playtest servers | Free | Medium: other developers, good with feedback |
| **2b. Portal soft launch** | CrazyGames' staged release: a small exposure test with real numbers | Free | High: real players, real retention |
| **2c. Steam Playtest** (Steam games only) | A free sign-up playtest on the store page | Free (after the $100 app fee) | High for PC fit; builds wishlists |
| **2d. Paid testers** (PlaytestCloud and similar) | Recorded sessions from target players | ~$30–60 per tester | Very high per person; costly |

**Move on when:**

- first-session length is over 5 minutes;
- D1 is over 20% in a portal soft launch or with telemetry;
- some testers share or return unprompted.

**Stop or rework when:** D1 is under 10% after two rounds of changes.

### 4.3 Stage 3: Free community seeding

**The question:** which message, clip or community brings players back?

Free in money, costly in time. Tactics are listed in §5 with their fit and effort. The discipline
here:

- **One message per post.**
- **A tagged link for every post.**
- **A log of results:** views → visits → returns.

**Move on when:** a message or community repeatedly brings visitors who return, and the cost in
hours per returning player is falling.

**Stop or rework when:** ten or more varied posts, across at least three communities, bring no
returning players.

### 4.4 Stage 4: Paid tests

**The question:** what does a player (or a wishlist) cost, which creative works, and does a paid
player behave like an organic one?

**Principles:**

- **Test, don't buy.** Each test has one hypothesis, one variable, a fixed budget and a stop-loss.
- **Reuse proven organic creative.** A clip that did well in Stage 3 is the best first ad.
- **Choose geography deliberately:**
  - cheaper regions (Latin America, South-East Asia, eastern Europe) cost a fraction per player and
    are good for testing engagement;
  - the US and western Europe for Steam wishlists and revenue.
- **Use gore-free cuts** for Gladiator ads (platform policy).
- **Minimum sample:**
  - estimating D1 to about ±7–10 points needs roughly 100–200 players per group;
  - comparing two versions needs two such groups.

  Below that, read only CTR and cost per click.

**Platform options:**

| Platform | Suits | Rough cost | Notes |
|---|---|---|---|
| **TikTok** | Gladiator clips, Slope Lab crashes | CPM ~$3–10; CPC ~$0.20–1 | Creative is everything; violence policy |
| **Reddit** | Niche targeting by community (history, HEMA, FIRE, skiing, strategy) | CPC ~$0.20–1 | Communities dislike obvious ads; native-looking posts do better |
| **YouTube Shorts / Google** | Clips; broad reach | CPV low; CPI varies | Google's app campaigns for mobile apps only |
| **Meta (Instagram/Facebook)** | Broad; The Ladder (life-sim audience) | CPM ~$5–15 | Strict on violence; good optimisation once there is data |
| **Apple Search Ads** | App store games only | CPT ~$0.50–2 | Only after an iOS launch |
| **Micro-creators** (sponsored) | A short video by a small YouTuber or streamer | $50–500 per creator | Often better than ads for niche games; must be disclosed as sponsored (FTC / ASA rules) |

### 4.5 Stage 5: Scale

Spend beyond tests only when the economics are clear:

- **Paid PC game:** cost per wishlist × the wishlist-to-sale rate (often 10–20% in the first year)
  is below net revenue per sale.
- **Ad-funded web or mobile:** cost per player is below lifetime revenue per player (LTV).
- **Or by explicit choice:** a capped budget for a launch moment (Next Fest, a store launch, a
  featuring), treated as an investment with a stated ceiling.

For web games earning ~$0.01–0.05 per player, paid acquisition almost never pays back. It is only
for learning or for driving Steam wishlists.

---

## 5. Creative and low-cost tactics

Rated on four axes:

- **Fit:** which games it suits (G = Gladiator, W = Greatwall, L = The Ladder, S = Slope Lab).
- **Reach:** the size of the audience it can find.
- **Effort:** hours to set up, plus hours a week to keep going.
- **Lasting:** whether the work keeps paying off after the post or event.

| # | Tactic | Fit | Reach | Effort | Lasting | Notes |
|---|---|---|---|---|---|---|
| **C1** | **Automated clip factory.** The simulation is deterministic and runs headless, so script match-ups ("1 samurai vs 10 peasants"), render clips, and post one a day to Shorts, TikTok and Reddit | G, W | High | Medium setup (a headless renderer + captions), then low | High | The cheapest way to make a lot of content; every clip links to the same fight in the game |
| **C2** | **Audience-voted match-ups.** "Who wins: 3 knights or 12 ashigaru?" — a poll, then the clip of the result | G, W | High (engagement-driven) | Low | Medium | Comments boost reach; viewers suggest the next match-up |
| **C3** | **Reply bot.** Comment a match-up on a post or in Discord and get a rendered clip back | G | Medium–high | Medium | High | A novelty that spreads; needs rate limits and moderation |
| **C4** | **Communities that already care about the subject** | All | Medium, but well targeted | Low | Medium | Gladiator: HEMA, history, samurai and medieval subreddits. Greatwall: strategy, Total War, Chinese and Mongol history. The Ladder: personal finance and FIRE communities. Slope Lab: skiing, in season |
| **C5** | **"Built with AI" development story** | All | Medium–high (tech audience) | Low–medium | High | Posts like "an AI-built physics fighting game" on Hacker News, X, LinkedIn and dev.to; the process itself is the story |
| **C6** | **Shareable results** | L, G | Medium | Low (exists for The Ladder) | High | The Ladder's ending page and Gladiator's "my army beat yours" card, each with a challenge link |
| **C7** | **Challenge links and weekly cups** | G, W, S | Medium | Medium (needs online features) | High | A friend challenges a friend; the leaderboard brings people back |
| **C8** | **Game jams and festivals** | All | Medium | Medium | Medium | itch.io jams with a themed variant, Steam festivals (Next Fest, themed sales), web game showcases |
| **C9** | **Creator outreach** (free keys or links) | G, W | Medium–high | Medium | Medium | Keymailer and Woovit-style services, or direct emails to small history and physics-game YouTubers; physics sandboxes make good streams |
| **C10** | **Seasonal and news timing** | S, L, G | Medium | Low | Low | Ski season for Slope Lab; tax and job-hunting season for The Ladder; anniversaries for Gladiator's levels (Sekigahara is 21 October) |
| **C11** | **Cross-promotion between the games** | All | Low–medium | Low | High | A "more games" page, a shared profile later; each game's players find the others |
| **C12** | **Educational angle** | W, G, L | Medium | Medium | High | History teachers (Sekigahara, the Great Wall, the Peasants' Revolt) and personal-finance teachers (The Ladder); educator newsletters |
| **C13** | **Physics "what if" posts** | G, S | Medium | Low | Medium | "What a war hammer does to plate vs a katana": numbers from the simulation, as an explainer post |
| **C14** | **Small prizes for leaderboard events** | G, W, S | Low–medium | Low | Low | Gift cards for a weekly cup; check local contest rules |
| **C15** | **Mod and setup sharing** | G, W | Medium | Medium | High | Setups as files and links (already in Gladiator), a gallery of community armies |

**Tactic fit by stage:**

- **Stage 1:** C6.
- **Stage 2:** C4, C8.
- **Stage 3:** C1, C2, C4, C5, C10, C13.
- **Stage 4:** C1 creative reused as ads; C9 as paid micro-creators.
- **Retention throughout:** C7, C11, C15.

---

## 6. Budget options for the first paid round

### 6.1 Options

The cost per lesson is the total spend divided by the decisions the test can support.

| Option | Total | What it can test | What it can't tell you | Cost per lesson |
|---|---|---|---|---|
| **A. Under $100** | ~$50–100 | One platform; 2 creatives; CTR and cost per click; a rough cost per visitor | Retention (too few players per group); creative winners beyond large differences | Low cost, low confidence |
| **B. $100–500** | ~$300 | 2 platforms or 3–4 creatives; first D1 read in a cheap region (~150–300 players); compare games by cost per returning player | Steam wishlist economics; small differences | Good balance for a first round |
| **C. $500–2,000** | ~$1,000 | Retention by game and creative with usable samples; a Steam wishlist campaign in high-value regions; 2–3 micro-creator sponsorships | Profitability at scale (still too small) | Highest confidence before committing |
| **D. $0** | $0 | Only organic channels (Stages 1–3); paid tests deferred | Anything about paid economics | Free, but slower; reach depends on luck and content |

### 6.2 What paid ads can and can't buy here

- **Revenue per player** for a web game with portal ads is roughly $0.01–0.05. A visitor costing
  $0.10–0.50 **loses money** by design, so this spend is for **learning**.
- **Steam:** paid wishlists at $0.50–3 can pay back for a $10–20 game if 10–20% buy, but only for a
  game that already converts organically.
- **Mobile:** installs at $1–5 pay back only with tuned ad or in-app monetisation. That is out of
  scope for now.

### 6.3 How to split a budget across games

Treat the games as a multi-armed bandit, a standard method for spending under uncertainty:

1. Start with an even split across the games that cleared Stage 3, with a minimum per game so each
   test gives a readable result.
2. After each round, move about 70% of the next budget to the game with the best **cost per
   returning player** (or cost per wishlist).
3. Keep about 30% exploring the others.
4. A game below its stop criteria gets nothing next round.

### 6.4 Stop-loss rules, fixed before spending

- End a creative after about 1,000–2,000 impressions if its CTR is under half the platform's
  typical rate.
- End a game's paid test once spend reaches 2× the planned cost per returning player with no
  returning players.
- No round may exceed its budget. No "one more day".

---

## 7. Tradeoffs

| Tradeoff | Leaning one way | Leaning the other | Framework default |
|---|---|---|---|
| **Time vs money** | Organic tactics cost hours | Paid ads cost dollars, save hours, but buy little here | Spend time first (Stages 1–3); money only to answer questions time can't |
| **Friends vs strangers** | Friends: easy, fast, deep "why" | Strangers: honest behaviour, the real audience | Friends for understanding; strangers for the decision |
| **Breadth vs depth across games** | All four marketed at once: more chances | One game: deeper push, more polish | Breadth in Stages 1–3 (cheap); depth from Stage 4 (by signal) |
| **Organic vs paid** | Organic results compound and last | Paid stops when the money stops | Organic first; paid as a probe and a launch boost |
| **Content volume vs polish** | Many quick clips (C1) | A few crafted trailers | Volume to find what works, then polish the winner for ads and the store |
| **Building features vs marketing** | Features (online, PWA) raise retention | Marketing raises arrivals | Fix retention before buying arrivals; never pay to fill a leaky game |
| **Platform reach vs control** | Big platforms (TikTok) reach far, but their rules change | Your own community (Discord, mailing list) is small but yours | Use the big platforms to feed your own community |
| **Personal identity vs studio name** | Personal: authentic; the dev story works | Studio: separates the games from you; looks professional | Open question (§10) |

---

## 8. Expected outcomes by stage

These are judgement figures for a small unmarketed portfolio, to set expectations.

| Stage | Typical result | Good result | Time |
|---|---|---|---|
| 1 Friends beta | 5–15 players per game; 2–5 fixes found | A friend shares it unprompted | 1–2 weeks |
| 2 Strangers | 50–300 players; D1 10–20% | D1 over 25%; organic comments | 2–4 weeks |
| 3 Seeding | 1–3 posts get traction out of 20; hundreds to a few thousand visitors | One clip reaches 100k+ views and a few thousand players | 4–8 weeks |
| 4 Paid (option B) | A cost per returning player per game; one creative winner | A game whose paid players return as well as organic ones | 2–4 weeks |
| 5 Scale | Rare at this stage | Steam wishlists past 7,000; or a portal featuring | Months |

Across the portfolio, the realistic payoff of the first quarter is **knowing which game and
message pull**, plus a small core community. A viral clip is the main source of upside and can't
be planned, so the framework maximises the number of cheap attempts at one.

---

## 9. Effort and upkeep

| Activity | Setup | Ongoing |
|---|---|---|
| Instrumentation (tagged links, event log, dashboard) | 2–4 days, shared | ~1 h a week |
| Friends beta (1b) | ~5–10 h per game | — |
| Beta Discord (1c) | 1 h | 1–2 h a week |
| Clip factory (C1) | 3–5 days | ~1–2 h a week (curating, posting) |
| Community posting (C4) | — | 2–4 h a week |
| Dev story posts (C5) | — | 2–3 h per post |
| Creator outreach (C9) | 1 day for the list and template | 1–2 h a week |
| Paid test round | 2–4 h setup | ~30 min a day monitoring; 2 h review |

A sustainable baseline is about **5–8 hours a week** of marketing across the portfolio.

---

## 10. Open questions

1. **Paid test budget:** A (under $100), B ($100–500), C ($500–2,000) or D ($0 for now)? The
   framework works with any; it changes only what Stage 4 can tell you.
2. **Time budget:** how many hours a week go to marketing rather than development?
3. **Public identity:** your personal name and the dev story, or a studio or brand name?
4. **Gore policy for marketing:** a gore-free cut for ads only, or for all public clips?
5. **Who the friends beta is for:** which games first (all four, or the two most finished)?
6. **Order with online features:** do Stage 2 tests wait for the minimal telemetry and
   challenge-link features (companion RFC, Option A), or run with portal analytics only?

## 11. Risks

| Risk | Mitigation |
|---|---|
| Friends' kindness gives false confidence | Judge by behaviour (§3); strangers decide (Stage 2) |
| Self-promotion rules get posts removed or accounts banned | Read each community's rules; take part beyond your own posts; follow the 10%-self-promotion norm |
| Ad platforms reject violent creative | Gore-free cuts; review the policy before producing |
| Spending on a game that doesn't keep players | Retention bar before Stage 4; stop-loss rules |
| A viral moment arrives before the game is ready (no retention features, slow on phones) | Keep the PWA, the device-class cap and a share loop ready before Stage 3 |
| Sponsored content without disclosure | Always label sponsorships (FTC / ASA) |
| Marketing time crowds out development | A fixed weekly hour budget (§9) |
| Platform dependence (an algorithm change wipes out reach) | Feed every channel into your own Discord and mailing list |
