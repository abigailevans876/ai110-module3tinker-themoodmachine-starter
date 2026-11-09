"""
Rule based mood analyzer for short text snippets.

This class starts with a simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute separate positive and negative scores
  - Convert the scores into a mood label
"""

import re
from typing import List, Optional, Tuple

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A simple rule-based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens.
        """
        if text is None:
            print("Input was None")
            return []

        text = str(text)
        text = text.replace("’", "'").replace("“", '"').replace("”", '"')
        text = text.lower().strip()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[^a-z0-9\s']", " ", text)
        text = text.replace("can't", "cannot").replace("won't", "will not")

        tokens = text.split()

        print(f"Raw input: {text!r}")
        print(f"Tokens: {tokens}")

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a net mood score for the given text.
        Positive and negative counts are tracked separately, then combined.
        """
        tokens = self.preprocess(text)
        if not tokens:
            return 0

        positive_score = 0
        negative_score = 0
        negation_active = False
        saw_but = False

        for i, token in enumerate(tokens):
            if token == "but":
                saw_but = True
                negation_active = False
                continue

            if token in {"not", "never", "no", "cannot", "dont", "don't"}:
                negation_active = True
                continue

            if token in self.positive_words:
                if negation_active:
                    negative_score += 1
                    negation_active = False
                else:
                    positive_score += 1
                continue

            if token in self.negative_words:
                if negation_active:
                    positive_score += 1
                    negation_active = False
                else:
                    negative_score += 1
                continue

            # reset negation if the next token is not sentiment-related
            negation_active = False

        net_score = positive_score - negative_score

        # If both positive and negative signals are present, treat it as mixed
        # especially when "but" appears.
        if saw_but and positive_score > 0 and negative_score > 0:
            return 0

        return net_score

    def score_components(self, text: str) -> Tuple[int, int]:
        """
        Return (positive_count, negative_count) for debugging and explain().
        """
        tokens = self.preprocess(text)
        if not tokens:
            return (0, 0)

        positive_score = 0
        negative_score = 0
        negation_active = False
        saw_but = False

        for token in tokens:
            if token == "but":
                saw_but = True
                negation_active = False
                continue

            if token in {"not", "never", "no", "cannot", "dont", "don't"}:
                negation_active = True
                continue

            if token in self.positive_words:
                if negation_active:
                    negative_score += 1
                    negation_active = False
                else:
                    positive_score += 1
                continue

            if token in self.negative_words:
                if negation_active:
                    positive_score += 1
                    negation_active = False
                else:
                    negative_score += 1
                continue

            negation_active = False

        return positive_score, negative_score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Map sentiment scores to a mood label.
        """
        tokens = self.preprocess(text)
        if not tokens:
            return "neutral"

        positive_score, negative_score = self.score_components(text)

        if "but" in tokens and positive_score > 0 and negative_score > 0:
            return "mixed"

        if positive_score > negative_score:
            return "positive"
        if negative_score > positive_score:
            return "negative"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short human-readable explanation of the model's decision.
        """
        tokens = self.preprocess(text)
        positive_score, negative_score = self.score_components(text)

        if "but" in tokens and positive_score > 0 and negative_score > 0:
            label = "mixed"
        elif positive_score > negative_score:
            label = "positive"
        elif negative_score > positive_score:
            label = "negative"
        else:
            label = "neutral"

        return (
            f"Score = {positive_score - negative_score}; "
            f"label = {label}; "
            f"positive_words = {positive_score}, "
            f"negative_words = {negative_score}"
        )