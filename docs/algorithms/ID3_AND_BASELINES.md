# 🌳 ID3 Filename and Majority-Class Baseline

id3.py creates a synthetic dataframe with four numeric features and a three-class integer target. train_model selects the most frequent class; evaluate_model predicts that class for every row.

No entropy or information gain is calculated, no attribute is selected, and no decision tree is constructed. The file name ID3 does not reflect current behavior.

The score is calculated on the same labels used to select the majority class. It is in-sample resubstitution, not holdout or cross-validation. It equals the majority-class frequency.

A real ID3 implementation needs defined split strategy, entropy, information gain, stopping criteria, missing-value behavior, tie-breaking, tree representation and separate evaluation data.
