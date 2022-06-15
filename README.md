# Intent Classifier

The purpose of this project is to classify strings that are action points. The team has determined an action point is a sentence that has at least one subject, is of the future tense, and has some reference to time. 

The program utilizes NLP techniques to classify strings based on tense (past, present, future). I use the Natural Language Toolkit (NLTK) library to capture the different parts of speech in each sentence/string and then hand-engineer the features. Lastly, I classify a given string by the corresponding score. 

For instance, consider the sentence, "We will attend the meeting in one hour." This sentence is in the future tense, there is at least one subject, "we", and their is a mention to a time related object, "hour". This sentence satisfies the given conditions, so the sentence is classified as an action point. Now consider the sentence "It’s not always smooth sailing, and sometimes the team will run into a roadblock, challenge, or bottleneck." The sentence is in the future tense, there is a mention to a subject, "I", and there is a mention to at least one subject, but there is no reference to a deadline or a date/time. So this sentence is not an action point.

There are many parts of speech, but below is a guide to the grammer tenses and their corresponding parts of speech codes.

```
- Future_Perfect_Continuous: {<MD><VB><VBN><VBG>}
- Future_Continuous:         {<MD><VB><VBG>}
- Future_Perfect:            {<MD><VB><VBN>}
- Past_Perfect_Continuous:   {<VBD><VBN><VBG>}
- Present_Perfect_Continuous:{<VBP|VBZ><VBN><VBG>}
- Future_Indefinite:         {<MD><VB>}
- Past_Continuous:           {<VBD><VBG>}
- Past_Perfect:              {<VBD><VBN>}
- Present_Continuous:        {<VBZ|VBP><VBG>}
- Present_Perfect:           {<VBZ|VBP><VBN>}
- Past_Indefinite:           {<VBD>}
- Present_Indefinite:        {<VBZ>|<VBP>}
```

