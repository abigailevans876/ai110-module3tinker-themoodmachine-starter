# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”

I used both the rule-based model and the machine learning model. The rule-based version in mood_analyzer.py uses a custom scoring system, while the ML version in ml_experiments.py trains a classifier on the expanded post/label dataset and compares its predictions to the rule-based approach.

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

This model is designed to classify short informal text posts into mood categories such as positive, negative, or neutral. The goal is to estimate the dominant emotional tone of a post, especially for social-media-style messages and brief personal updates.



**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).

The rule-based model assigns points for positive and negative words, then adjusts the score for negation, intensifiers, slang, emoji, and punctuation. For example, words like “happy,” “love,” or “😊” increase the score, while words like “sad,” “angry,” or “😞” decrease it. The final score determines whether the post is labeled positive, negative, or neutral.
The machine learning model uses a bag-of-words representation of the posts and learns patterns from labeled examples, rather than relying on manually written rules.

## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

SAMPLE_POSTS started as a small set of short, informal posts, and I expanded it by adding more examples that varied in tone, wording, punctuation, and emotion. I included both straightforward statements and more ambiguous posts so the model would be tested on realistic language, not just the original examples. The expanded dataset includes a mix of happy, sad, neutral, and mixed-emotion posts.



**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

I labeled each added post based on the dominant emotional tone of the message. If a post clearly expressed happiness or excitement, I labeled it positive; if it clearly conveyed sadness, anger, or frustration, I labeled it negative; if it was mostly neutral or ambiguous, I labeled it neutral. Some posts were difficult to label because they mixed positive and negative feelings, or because slang and emojis changed the tone in ways that were not obvious from the words alone.

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

Characteristics of my dataset include:

- Contains slang, casual phrasing, and internet-style language
- Includes emojis and emoticons
- Some posts express mixed feelings or contrastive tone
- Includes short, ambiguous messages with little context
- Contains a range of emotional intensity, from subtle to obvious


**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.

The dataset is still small and somewhat imbalanced, because many examples cluster around simple, clear emotions while fewer examples cover mixed or nuanced feelings. Some kinds of language are underrepresented, especially sarcasm, dialect, and highly informal slang. This makes it harder for the model to generalize beyond the patterns it has seen.

## 3. How the Rule Based Model Works (if used)
The rule-based model works by assigning numeric weights to positive and negative words and phrases. Positive words increase the score, while negative words decrease it. I also added rules for negation, so phrases like “not happy” or “never better” are treated differently from straightforward positive wording. Intensifiers such as “very,” “really,” or “so” increase the effect of nearby words, and emoji like “😊,” “😂,” or “😞” are treated as emotional signals. The system then compares the final score to a threshold and assigns a label such as positive, negative, or neutral.

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

My modeling choices include:

- Positive words increase the score
- Negative words decrease the score
- Negation flips the meaning of nearby sentiment words
- Intensifiers strengthen the emotional effect
- Emoji contribute additional sentiment
- A final threshold determines the label: positive, negative, or neutral


**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

This model works well on short, clear posts with direct emotional language. It is easy to interpret, easy to debug, and tends to perform reliably when the mood is obvious from the wording.

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

The model struggles with sarcasm, mixed emotions, and subtle or context-dependent wording. A sentence like “I’m so happy I could scream” may be interpreted too literally, while a phrase like “great, another bad day” can be over-weighted by a single strong word. It also has trouble with unfamiliar slang, short fragments, and posts where the emotional meaning depends more on context than on the specific words used.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

The machine learning model uses a bag-of-words representation of the post text, where each word is treated as a feature and the model learns which words are associated with different moods. In this project, the text is converted into numerical feature vectors and used to train a classifier.

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

The model was trained on the labeled examples in SAMPLE_POSTS and their corresponding labels in TRUE_LABELS. As I expanded the dataset with new examples, I also updated the label set to reflect the revised mood assignments.


**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

The learned model behaved differently from the rule-based one because it picked up patterns from repeated words and combinations rather than relying on manually designed scores. When I added more examples or adjusted labels, the model’s behavior changed noticeably, especially for borderline posts. This showed that the learned model was sensitive to the label definitions and to how balanced or noisy the training data was.


**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

A strength of the ML model is that it can learn general patterns automatically and sometimes handle wording that was not explicitly included in my hand-written rules. However, it is also more sensitive to overfitting, especially when the dataset is small or when certain labels are unevenly represented. It may also latch onto weak or misleading cues in the training data, which can lead to incorrect predictions on posts that are emotionally subtle or stylistically different.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

I evaluated both models on the labeled posts in dataset.py by comparing their predictions to the assigned labels and computing overall accuracy. The rule-based model performed well on clear, direct examples, while the learned model was more sensitive to the exact wording and label distribution in the training set.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

Examples of correct predictions:

- “I’m so happy today 😊” was classified correctly as positive because it contains a clear positive emotion and an emoji that reinforces the tone.
- “I feel exhausted and upset 😞” was classified correctly as negative because the words and emoji clearly point to a negative mood.
- “I’m fine today” was classified correctly as neutral or mildly positive depending on the final score, because it contains a low-intensity phrase without a strongly emotional signal.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

- “I’m not happy, but I’m trying to be” was likely misclassified because the model saw “happy” and treated the sentence as positive even though the overall meaning is mixed and negative.
- “This is amazing, but also awful” could be labeled too positively or too negatively because it contains conflicting emotional cues that the simple scoring system does not resolve well.
- “lol I’m miserable but pretending I’m fine” may be misclassified because the model may focus on the strongest emotional word without understanding the joke-like, mixed tone.

The failures were different across models: the rule-based system struggled most with context and mixed emotion, while the ML model could overfit to frequent words or labels and become unstable when the training examples were limited or unevenly distributed.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

The most important limitation is that the dataset is small and highly dependent on the specific words and labels I chose. This means the model may not generalize well to longer posts, different writing styles, or more realistic conversational text. It also struggles with sarcasm, ambiguity, and mixed emotions, because both the rule-based and learned models treat sentiment as a simplified pattern rather than a full understanding of context.

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

Mood detection can be useful for analysis, but it can also misclassify emotionally serious content. For example, a post expressing distress could be labeled as neutral or low-intensity if the wording is ambiguous, which could lead to harmful misunderstandings. It can also misinterpret mood for certain language communities if the model is trained on a narrow dataset that does not reflect the diversity of writing styles, dialects, or slang.

A practical ethical risk is that a mood classifier may be used on personal messages without enough context or consent. Even though this project is only a classroom example, it highlights how language-based prediction systems can produce biased or misleading results if they are applied in real-world settings.

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only


Ways to improve the models include:
- Expand the dataset with more labeled examples from a wider range of language styles
- Add better handling for sarcasm, negation, and mixed-emotion posts
- Use TF-IDF or other text representations instead of only a basic bag-of-words model
- Include slang dictionaries and emoji normalization
- Test on a separate validation set rather than relying only on the training examples
- Improve the rule-based scoring with phrase-level and context-aware logic
- Explore stronger models such as a small transformer or a larger sentiment classifier trained on a real dataset
