from nltk import word_tokenize, pos_tag

# determine tense counts of string
def determine_tense_input(sentence):
    text = word_tokenize(sentence)
    tagged = pos_tag(text)

    tense = {}
    tense["future"] = len([word for word in tagged if word[1] in ["MD", "VBF", "VBC", "VB", "VBN"]])
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]]) 
    return(tense)

# get count of time objects
def determine_time_input(sentence):
    text = word_tokenize(sentence)
    tagged = pos_tag(text)

    time_count = len([word for word in tagged if word[1] in ["NNP", "CD"]])  
    return(time_count)

# get count of subject objects
def determine_subject_input(sentence):
    text = word_tokenize(sentence)
    tagged = pos_tag(text)

    subject_count = len([word for word in tagged if word[1] in ["PRP", "NNP", "NNS"]])  
    return(subject_count)


def get_action_strings(df, text_col_name, filter_strings = True):
    """
    This function takes two arguments as input:
    - df: Your dataframe containing a column of strings
    - text_col_name: The name of the column that contains the strings
    - filter_strings: True or False, if True it will filter the dataframe for the following:
    -- Tense == 'future'
    -- subject_count > 0
    -- time_object_count > 0 
    
    This function will update the dataframe with three new columns:
    - tense: Past/Present/Future
    - subject_count: Number of subjects present in string
    - time_object_count: Number of time related objects in string

    """
    
    # lists to store tense's, count of subjects, and count of time-objects
    tense_col = []
    subject_count = []
    time_object_count = []
    
    # process the df
    df_list = list(df[text_col_name])

    
    for i in range(len(df)):
        text = df_list[i]
        
        # Tense
        tagged = pos_tag(text)

        tense = {}
        tense["future"] = len([word for word in tagged if word[1] in ["MD", "VBF", "VBC", "VB", "VBN"]])
        tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
        tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]]) 
        
        tense_dict = determine_tense_input(text)
        final_tense = max(tense_dict, key=tense_dict.get)
        tense_col += [final_tense]
        
        # Subject Count
        subject_count += [determine_subject_input(text)]
        
        # Time object count
        time_object_count += [determine_time_input(text)]
    
    # add column of tense's to df
    df = df.assign(tense = tense_col)
    
    # add column of subject counts to df
    df = df.assign(subject_count = subject_count)
    
    # add column of time-related object count
    df = df.assign(time_count = time_object_count)
    
    # FILTER
    
    if filter_strings == True:
    
        # filter for those rows that contain future tense strings
        df = df[df["tense"].str.contains("future")]

        # filter for those rows that contain at least one subject
        df = df[df["subject_count"] > 0]

        # filter for those rows that contain at least one time object
        df = df[df["time_count"] > 0]
    
    
    # return the updated df
    return df