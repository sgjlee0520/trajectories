# Roster membership verification — wave 4

Copy everything below the line into Antigravity (use Opus 4.6) or any assistant with web search. Save the result as `roster-verify-w4.md` in `~/trajectories/`.

---

## TASK

Below are 25 people. For EACH, determine whether that person genuinely appears on the source list credited to them. Return a verdict and a URL that actually names the person.

This is a fraud check, not a formality. A previous roster in this project cited list membership for 18 people and three of them were on no list at all — they had to be thrown out after being fully researched. At least one entry below is suspected to be **entirely fabricated**: a real person's name attached to a company they have nothing to do with.

## WHAT COUNTS AS CONFIRMATION

- A page that **names the person** (or names their company, where the list ranks companies) as being on that list, ideally with a year or rank.
- A generic link to the list's homepage or a blog post that does not mention them does **NOT** count. Neither does a profile that merely says they are successful.
- If the person is real but is on a *different* list than the one credited, say so — that is useful and fixable.
- If the person appears not to exist in the role described, say so plainly.

## VERDICTS — use exactly one per person

- `CONFIRMED` — found a page naming them on the credited list. Give the URL and quote the naming sentence.
- `WRONG LIST` — real person, real career, but not on the credited list. Say which list does name them, if any.
- `UNCONFIRMED` — real person, but two genuine attempts found no page placing them on any qualifying list.
- `FABRICATED` — the person does not appear to exist in the role described, or the described company does not exist.

## THE PEOPLE

| id | name | bucket | credited source list |
|---|---|---|---|
| p86 | Vidit Aatrey | software_internet | Y Combinator Top Companies |
| p87 | Aadit Palicha | software_internet | Y Combinator Top Companies |
| p88 | Wade Foster | software_internet | Y Combinator Top Companies |
| p89 | Wei Deng | software_internet | Y Combinator Top Companies |
| p90 | Eugenio Pace | software_internet | Endeavor Entrepreneur network (emerging markets) |
| p91 | Karim Beguir | software_internet | Endeavor Entrepreneur network (emerging markets) |
| p92 | Mudassir Sheikha | software_internet | Endeavor Entrepreneur network (emerging markets) |
| p93 | Sophie Wilson | hardware_deeptech | Computer History Museum Fellow Awards |
| p94 | Jeff Hawkins | hardware_deeptech | Computer History Museum Fellow Awards |
| p95 | Frank Wang | hardware_deeptech | Forbes World's Billionaires (self-made) |
| p96 | Lei Jun | hardware_deeptech | Forbes World's Billionaires (self-made) |
| p97 | Betsie Larkin | consumer_retail_industrial | Y Combinator Top Companies |
| p98 | Chip Wilson | consumer_retail_industrial | Forbes World's Billionaires (self-made) |
| p99 | Ismael Belkhayat | consumer_retail_industrial | Endeavor Entrepreneur network (emerging markets) |
| p100 | Colson Whitehead | media_creators | Pulitzer Prize |
| p101 | Jane Campion | media_creators | Academy Awards |
| p102 | Angélique Kidjo | media_creators | Grammy Awards |
| p103 | Alain Aspect | science_research | Nobel Prizes (Physics) |
| p104 | Carolyn Bertozzi | science_research | Nobel Prizes (Chemistry) |
| p105 | Dennis Gaitsgory | science_research | Breakthrough Prize |
| p106 | Leonard Schleifer | healthcare_biotech | Forbes World's Billionaires (self-made) |
| p107 | Alice Zhang | healthcare_biotech | Fortune 40 Under 40 |
| p108 | Laurel Bowden | investors_finance | Midas List Europe |
| p109 | Ondrej Bartos | investors_finance | Midas List Europe |
| p110 | John Fredriksen | trade_import_logistics | Forbes World's Billionaires (self-made) |

## PARTICULAR ATTENTION

**p97 Betsie Larkin** is the suspected fabrication. She is credited as a "shapewear founder" from Y Combinator Top Companies. The only prominent person by that name appears to be an American trance/EDM vocalist. Determine whether any YC-backed shapewear or apparel company has a founder by this name. If not, mark `FABRICATED`.

## OUTPUT

Start with a table:

```
| id | name | verdict | URL that names them |
|---|---|---|---|
| p86 | Vidit Aatrey | CONFIRMED | https://... |
```

Then one short paragraph per person that is not `CONFIRMED`, explaining what you searched and what you found. Be blunt. A `FABRICATED` or `UNCONFIRMED` verdict is a useful result, not a failure — these rows get removed before they waste research effort.
