import numpy as np

def compute_roc_curve(y_true: list, y_scores: list) -> tuple:
    thresholds = sorted(set(y_scores), reverse = True)
    tpr_l, fpr_l = [0], [0]
    for a in thresholds:
        tp, fp, tn, fn = 0, 0, 0, 0
        for true, score in zip(y_true, y_scores):
            pred = int(score >= a)
            if true and pred:
                tp += 1
            elif true and not pred:
                fn += 1
            elif not true and not pred:
                tn += 1
            else:
                fp += 1
        tpr = tp / (tp + fn) if (tp + fn) != 0 else 0
        fpr = fp / (fp + tn) if (fp + tn) != 0 else 0
        tpr_l.append(tpr)
        fpr_l.append(fpr)
    return fpr_l, tpr_l
