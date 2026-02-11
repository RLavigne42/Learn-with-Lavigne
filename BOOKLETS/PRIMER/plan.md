# PRIMER Plan

## Objective
Build the `BOOKLETS/PRIMER/PUBLICATIONS` primer booklet series with beginner-friendly introduction prompts.

## Scope
- Create 10 PRIMER booklets.
- Each booklet includes one `01_prompt.md` prompt-spec section file.
- Preserve both a short question and long-form guidance question.
- Maintain a canonical JSON representation of booklet metadata/content.

## Rules
- Ignore `model`.
- Ignore `temperature`.
- Preserve specific instructional constraints in each long-form question.

## Checklist
| Booklet number/title | Target folder | File path | Status (Not Started / In Progress / Complete) |
| --- | --- | --- | --- |
| 01 — What AI Really Is: An Intuitive Guide to LLMs | `BOOKLETS/PRIMER/PUBLICATIONS/01_What_AI_Really_Is_An_Intuitive_Guide_to_LLMs` | `BOOKLETS/PRIMER/PUBLICATIONS/01_What_AI_Really_Is_An_Intuitive_Guide_to_LLMs/01_prompt.md` | Complete |
| 02 — Understanding the Building Blocks: Language, Tokens, and Data | `BOOKLETS/PRIMER/PUBLICATIONS/02_Understanding_the_Building_Blocks_Language_Tokens_and_Data` | `BOOKLETS/PRIMER/PUBLICATIONS/02_Understanding_the_Building_Blocks_Language_Tokens_and_Data/01_prompt.md` | Complete |
| 03 — How LLMs Get Smart: A Gentle Intro to Model Training | `BOOKLETS/PRIMER/PUBLICATIONS/03_How_LLMs_Get_Smart_A_Gentle_Intro_to_Model_Training` | `BOOKLETS/PRIMER/PUBLICATIONS/03_How_LLMs_Get_Smart_A_Gentle_Intro_to_Model_Training/01_prompt.md` | Complete |
| 04 — Thinking With Machines: How LLMs Generate Answers | `BOOKLETS/PRIMER/PUBLICATIONS/04_Thinking_With_Machines_How_LLMs_Generate_Answers` | `BOOKLETS/PRIMER/PUBLICATIONS/04_Thinking_With_Machines_How_LLMs_Generate_Answers/01_prompt.md` | Complete |
| 05 — Intro to Prompting: Talking to AI Effectively | `BOOKLETS/PRIMER/PUBLICATIONS/05_Intro_to_Prompting_Talking_to_AI_Effectively` | `BOOKLETS/PRIMER/PUBLICATIONS/05_Intro_to_Prompting_Talking_to_AI_Effectively/01_prompt.md` | Complete |
| 06 — Intro to RAG: Helping AI Learn From Your Information | `BOOKLETS/PRIMER/PUBLICATIONS/06_Intro_to_RAG_Helping_AI_Learn_From_Your_Information` | `BOOKLETS/PRIMER/PUBLICATIONS/06_Intro_to_RAG_Helping_AI_Learn_From_Your_Information/01_prompt.md` | Complete |
| 07 — Beginner Agents: How AI Can Take Actions for You | `BOOKLETS/PRIMER/PUBLICATIONS/07_Beginner_Agents_How_AI_Can_Take_Actions_for_You` | `BOOKLETS/PRIMER/PUBLICATIONS/07_Beginner_Agents_How_AI_Can_Take_Actions_for_You/01_prompt.md` | Complete |
| 08 — The Ecosystem: Intro to AI Tools & Workflows | `BOOKLETS/PRIMER/PUBLICATIONS/08_The_Ecosystem_Intro_to_AI_Tools_Workflows` | `BOOKLETS/PRIMER/PUBLICATIONS/08_The_Ecosystem_Intro_to_AI_Tools_Workflows/01_prompt.md` | Complete |
| 09 — Beginner AI Evaluation: How to Know If AI Is Working | `BOOKLETS/PRIMER/PUBLICATIONS/09_Beginner_AI_Evaluation_How_to_Know_If_AI_Is_Working` | `BOOKLETS/PRIMER/PUBLICATIONS/09_Beginner_AI_Evaluation_How_to_Know_If_AI_Is_Working/01_prompt.md` | Complete |
| 10 — Safety, Ethics & Responsible AI for Beginners | `BOOKLETS/PRIMER/PUBLICATIONS/10_Safety_Ethics_Responsible_AI_for_Beginners` | `BOOKLETS/PRIMER/PUBLICATIONS/10_Safety_Ethics_Responsible_AI_for_Beginners/01_prompt.md` | Complete |

## Artifacts
- Canonical JSON: `BOOKLETS/PRIMER/PUBLICATIONS/primer_booklets.json`
- Prompt specs: `BOOKLETS/PRIMER/PUBLICATIONS/*/01_prompt.md`
- Final outputs: `BOOKLETS/PRIMER/PUBLICATIONS/*/README.md`
- URL-slug outputs: `BOOKLETS/PRIMER/PUBLICATIONS/*/<url-slug>.md`

## Change Log
- 2026-02-11: Renamed prompt spec files from `01_introduction.md` to `01_prompt.md` and added url_slug-named markdown outputs per booklet.
- 2026-02-11: Executed PRIMER plan by generating 10 publication folders, section prompts, and canonical JSON metadata under `BOOKLETS/PRIMER/PUBLICATIONS`.
- 2026-02-11: Generated final-answer `README.md` content for each booklet section under `BOOKLETS/PRIMER/PUBLICATIONS/*/README.md`.

## Notes
- Source JSON fields `model` and `temperature` were intentionally omitted per request to disregard model information.


## Backup
- Original pre-publication plan preserved at `BOOKLETS/PRIMER/plan.original.backup.md` for future comparison.
