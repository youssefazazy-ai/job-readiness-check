# Job Readiness Check

A free, bilingual (Arabic-first) web tool for junior developers. Paste a job post, rate yourself on each requirement, note your evidence, and see what you can prove, what's missing, and a prioritized plan.

Privacy-first: no server, no database, no analytics. Everything runs in the visitor's browser. The only thing stored is the language choice (in `localStorage`).

## Files

```
index.html          The whole app: HTML, CSS and JavaScript in one file
tests/corpus.py     37 realistic job posts with the expected result for each
tests/suite.py      Runs every post in headless Chrome and checks the results
tests/*.txt         Longer test posts used by the corpus
```

## Run it locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Run the tests

```bash
pip install playwright
python3 -m playwright install chromium
cd tests
python3 suite.py
```

The suite checks, for every post:

- required and nice-to-have skills are detected with the right priority
- trap words are not detected (e.g. "react quickly", "rest of the team", "JSON")
- the minimum years of experience are read correctly
- lines that couldn't be mapped stay below a noise limit
- no JavaScript errors and no horizontal scrolling at 390px and 1280px, in Arabic and English

Expected output ends with: `37 posts, 37 pass on detection; 0 total issues`.

## How it works (inside `index.html`)

| Part | What it does |
| --- | --- |
| `SK` | The skill dictionary: id, label, category, regex pattern, and whether matching is case-sensitive |
| `HEADS` | Section heading phrases: `skip` (about us, benefits, deliverables), `pref` (nice to have), `req` (requirements), `resp` (responsibilities) |
| `detect(text)` | Pure function: returns detected skills (priority + best source line), unmapped requirement lines, and minimum years |
| `minYears(text)` | Pure function: reads "1+ years", "at least two years", "up to 2", "0–1", Arabic phrasing |
| `cls(id)` | Classifies a rating: evidence / self-rated / missing / not assessed. "I can prove it" only counts as evidence when the user wrote what the evidence is |
| `compute()` | Verdict rules and the ordered plan |
| `STR` | All interface text in Arabic and English, including skill-specific proof ideas (`proofIdea`) |

### Adding a skill

Add a row to `SK`, for example:

```js
["rust","Rust","be","rust"],
```

Then add a post that uses it to `tests/corpus.py` and run the suite.

### Sign-up button

Set `OPT_IN_URL` near the top of the script to a Google Form link to show the "Register interest" box under the result.
