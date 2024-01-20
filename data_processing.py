'''
Data Processing python script for machine translation
'''

import string
import re
import tensorflow as tf


global strip_chars
strip_chars = string.punctuation  # punctuation we want to eliminate in token
# exclude '[' or ']' because output language has [start] and [end] as tokens for text generation
strip_chars = strip_chars.replace("[", "")
strip_chars = strip_chars.replace("]", "")

# text preprocessing function
def text_standardization(input_str, **kwargs):
    lowercase = tf.strings.lower(input_str)
    return tf.strings.regex_replace(lowercase, f"[{re.escape(strip_chars)}]", "")
