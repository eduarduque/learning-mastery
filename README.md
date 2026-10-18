# Learning Mastery Protocol

A 12-week, evidence-based training system for learning how to learn. It runs as a single static page with no build step and no backend.

**Live app:** https://eduarduque.github.io/learning-mastery/

## Class practice
The **My classes** tab has multiple-choice practice for Biology, C++, Discrete Math and Ethics. The questions were written from Fall 2026 lecture materials, and the course files themselves are not included in this repo. How it picks questions:
- Topics are taken in turn, starting with the least-mastered and least-recently-practiced ones.
- Questions you haven't seen come before repeats.
- Missed questions come back after about 12 hours. Correct answers come back at growing intervals: 1, 3, 7, 16, 35 and 80 days.
- No question repeats within a session, and answer order is reshuffled each time.

Modes: Smart mix, Weak topics, My mistakes, Exam simulation.

**Adaptive difficulty:** each topic has its own level (Recall → Understand → Apply). Two correct answers in a row (not marked as guesses) move that topic up a level, and two misses in a row move it back down.

**Analytics** (My classes › Analytics) shows:
- coverage, accuracy and mastery for every class
- recommended topics to practice next
- daily accuracy over the last 30 days
- accuracy by difficulty level and how often your guesses were right
- a sortable topic table with status and current level
- your most-missed questions

To update the questions, edit `classes/*.json` and run `python build_classes.py`. That validates the banks and regenerates `classes/data.js`.

## What's inside
- **Intake and obstacles:** your habits and available time, mapped to your three biggest obstacles
- **Diagnostic:** 12 questions with confidence ratings that measure both knowledge and calibration
- **Exercise 1:** baseline free recall with retests at days 1, 3, 7 and 30 (your personal forgetting curve)
- **Week 1 plan:** what to do, how, why it works and how to measure success for every block
- **Review queue:** spaced repetition with adaptive intervals
- **Dashboard:** retention, calibration, study time and mastery per hour, with JSON export and import
- **12-week roadmap:** four phases with objectives, exercises, assessments and gate criteria
- **Principles and science:** methods graded by strength of evidence, common myths, and how memory works

Progress is saved in your browser after every answer, so it's still there after you close the tab. On the Dashboard, **Connect backup file** (Chrome/Edge) also keeps a JSON file on your disk up to date automatically.
