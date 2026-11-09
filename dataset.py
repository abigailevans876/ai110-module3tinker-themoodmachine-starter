"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
# Keep these aligned: each post must match the label at the same index.
SAMPLE_POSTS = [
    "i love this class so much",
    "today was a terrible day",
    "feeling tired but kind of hopeful",
    "this is fine",
    "so excited for the weekend",
    "i am not happy about this",
    "i am feeling great today",
    "this lecture was surprisingly good",
    "i feel okay about the plan",
    "the lecture was surprisingly good",
    "i am exhausted",
    "this assignment is frustrating",
    "i am extremely disappointed",
    "today was horrible",
    "i am upset and frustrated",
    "i hate this",
    "this is awful",
    "i am sick",
    "i am tired of this job",
    "this is just okay",
    "i feel okay about it",
    "the plan is okay",
    "nothing happened today",
    "i am overwhelmed but hopeful",
    "i am disappointed but trying to stay positive",
    "i am nervous but excited",
    "it was not great but acceptable",
    "i am tired and stressed but still hopeful",
]

# Human labels for each post above.
# Allowed labels:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "i love this class so much"
    "negative",  # "today was a terrible day"
    "mixed",     # "feeling tired but kind of hopeful"
    "neutral",   # "this is fine"
    "positive",  # "so excited for the weekend"
    "negative",  # "i am not happy about this"
    "positive",  # "i am feeling great today"
    "positive",  # "this lecture was surprisingly good"
    "neutral",   # "i feel okay about the plan"
    "positive",  # "the lecture was surprisingly good"
    "negative",  # "i am exhausted"
    "negative",  # "this assignment is frustrating"
    "negative",  # "i am extremely disappointed"
    "negative",  # "today was horrible"
    "negative",  # "i am upset and frustrated"
    "negative",  # "i hate this"
    "negative",  # "this is awful"
    "negative",  # "i am sick"
    "negative",  # "i am tired of this job"
    "neutral",   # "this is just okay"
    "neutral",   # "i feel okay about it"
    "neutral",   # "the plan is okay"
    "neutral",   # "nothing happened today"
    "mixed",     # "i am overwhelmed but hopeful"
    "mixed",     # "i am disappointed but trying to stay positive"
    "mixed",     # "i am nervous but excited"
    "mixed",     # "it was not great but acceptable"
    "mixed",     # "i am tired and stressed but still hopeful"
]

# TODO: Add more posts and labels as needed.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, add one matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)