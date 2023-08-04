import numpy as np
from bertopic import BERTopic

def load_model(model_path):
    model = BERTopic.load(model_path)
    return model

def predict_topic(model, text, num_of_topics=3):
    similar_topics, similarity = model.find_topics(text, top_n=num_of_topics)
    for topic in similar_topics:
        topic_words = model.get_topic(topic)[:3]  # get the top 3 keywords
        print(f"Topic {topic} top {num_of_topics} keywords: {', '.join([word for word, freq in topic_words])}")
    print(f"The top {num_of_topics} similar topics are {similar_topics}, and the similarities are {np.round(similarity, 2)}")



# def predict_topic(model, text, num_of_topics=3):
#     similar_topics, similarity = model.find_topics(text, top_n=num_of_topics)
#     print(f"The top {num_of_topics} similar topics are {similar_topics}, and the similarities are {np.round(similarity, 2)}")

if __name__ == "__main__":
    model_path = "Analysis/BloomBerg_model" 
    model = load_model(model_path)
    while True:
        text = input("Enter text: ")
        predict_topic(model, text)

# if __name__ == "__main__":
#     model_path = "Analysis/BloomBerg_model" 
#     model = load_model(model_path)
#     num_of_topics = 3
#     # Example usage:
#     text = input("Enter text: ")
#     similar_topics, similarity = predict_topic(model, text)
#     print(f"The top {num_of_topics} similar topics are {similar_topics}, and the similarities are {np.round(similarity, 2)}")

