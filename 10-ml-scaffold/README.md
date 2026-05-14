# Block 10 — ML Scaffold

**Time:** 30 min hands-on
**Goal:** Have Claude scaffold a working classifier on a real dataset. Read the numbers like an AI engineer.

---

## Setup

```bash
pip install scikit-learn
```

---

## The task

Build a text classifier on a 4-topic subset of the 20-newsgroups corpus.

1. Open Claude Code in this folder.
2. Tell it (in plan mode):
   > Build me a text classifier. 20 newsgroups, pick four topics with little semantic overlap. TF-IDF + LinearSVC. Report test accuracy + confusion matrix. Save metrics to `results.json`. No fine-tuning. No deep learning. Train must complete in under a minute.
3. Read Claude's plan. Critique:
   - Does it justify the model choice?
   - Are the four topics chosen on purpose, or by accident?
   - Will the test set be honestly held out?
4. Approve. Implement.
5. Run it. Verify the numbers.

---

## The reading

After it trains, **don't** ask Claude what the numbers mean. **You** read them:

- What's the test accuracy?
- Which classes does it confuse most?
- Is the gap between train accuracy and test accuracy big? (overfit)
- Which class has the worst recall? Why might that be?

Tell Claude your conclusions. Have it push back.

---

## Reference

`demos/05-ml-classifier/train.py` is what "good" looks like — 89.5% test accuracy, four topics, three minutes of training time. Don't peek until you've tried.

---

## Stretch

After it works:

1. Swap LinearSVC for ComplementNB. Does accuracy change?
2. Add 4 more topics. How does macro-F1 react?
3. Have Claude scaffold a confusion-matrix heatmap (matplotlib). Add it to `results/`.
