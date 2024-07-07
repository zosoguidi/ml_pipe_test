import uvicorn
from fastapi import FastAPI
from model import SentimentModel
import pandas as pd

app = FastAPI()
model = SentimentModel()



#@app.post('/predict')
def predict(input_sentence):
    polarity, subjectivity, result = model.get_sentimentanalysis(input_sentence)
    return { 'Sentiment': result
    }

if __name__ == '__main__':
 #   uvicorn.run(app, host='0.0.0.0', port=8000)
    # load data
    data_input=pd.read_csv('data_ingestion.csv')
    print(data_input)
    sentences=data_input['sentences']

    # to store results
    results=[]

    # process sentances through model
    for sentence in sentences:
        analysis=model.get_sentimentanalysis(sentence)
        results.append(analysis)

    # Convert the results into a DataFrame
    results_df = pd.DataFrame(results)

    # Concatenate the original sentences with their analysis results

    # Optionally, save the results to a new CSV file
    output_csv_path = 'sentences_with_sentiment.csv'  # Replace with your desired output file path
    results_df.to_csv(output_csv_path, index=False)
    

