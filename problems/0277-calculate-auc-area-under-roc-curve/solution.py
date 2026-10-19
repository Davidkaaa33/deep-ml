import numpy as np

def calculate_auc(y_true, y_scores):
    fpr_l, tpr_l = [0], [0]
    thresholds = sorted(set(y_scores), reverse = True)
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
    auc = 0.0
    for i in range(1, len(fpr_l)):
        auc += (tpr_l[i] + tpr_l[i - 1]) * (fpr_l[i] - fpr_l[i - 1]) / 2
    return auc
        
