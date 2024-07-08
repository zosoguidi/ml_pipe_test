import uvicorn
from fastapi import FastAPI
# from model import SentimentModel
import pandas as pd
import os

#model = SentimentModel()

#@app.post('/predict')
# def predict(input_sentence):
#     polarity, subjectivity, result = model.get_sentimentanalysis(input_sentence)
#     return { 'Sentiment': result
#     }


def check_file_in_folder(folder, filename):
    # Construct the full file path
    file_path = os.path.join(folder, filename)
    
    # Check if the file exists
    if os.path.isfile(file_path):
        print(f'The file "{filename}" exists in the folder "{folder}".')
        return True
    else:
        print(f'The file "{filename}" does not exist in the folder "{folder}".')
        return False




if __name__ == '__main__':
 
    # Define the folder and file name
    folder = 'input_folder'
    filename = 'data_ingestion.csv'

    # Call the function
    file_check=check_file_in_folder(folder, filename)
    # if file_check:
    text_file = open("/app2/Output.txt", "w")
    text_file.write("Purchase Amount:"+ str(file_check))
    text_file.close()
    
    
    
#  #   uvicorn.run(app, host='0.0.0.0', port=8000)
#     # load data
#     data_input=pd.read_csv('data_ingestion.csv')
#     print(data_input)
#     sentences=data_input['sentences']

#     # to store results
#     results=[]

#     # process sentances through model
#     for sentence in sentences:
#         analysis=model.get_sentimentanalysis(sentence)
#         results.append(analysis)

#     # Convert the results into a DataFrame
#     results_df = pd.DataFrame(results)

#     # Concatenate the original sentences with their analysis results

#     # Optionally, save the results to a new CSV file
#     output_csv_path = 'sentences_with_sentiment.csv'  # Replace with your desired output file path
#     results_df.to_csv(output_csv_path, index=False)
    

