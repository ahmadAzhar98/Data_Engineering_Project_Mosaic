import csv
import pandas as pd

PATH = "/Users/ahmadazhar/Desktop/Assignment1/datasets/raw/players_performace_2008_2023.csv"
CLEAN_PATH = "/Users/ahmadazhar/Desktop/Assignment1/datasets/clean/players_performace_2008_2023.csv"

# READ DATA
def read_ipl_data(path):
    df = pd.read_csv(path)
    return df

# DATA PREPROCESS
def data_preprocessing(input_file, output_file):
    df = read_ipl_data(input_file)
    
    # Check for null
    null_val = df.isnull().sum().sum()
    print("Total null values {} ".format(null_val))
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print("Total duplicate values {} ".format(duplicates))
    print("Data is cleaned no further preprocessing needed")
    
    df.to_csv(output_file, index=False)

def summarize_date(input_file):
    df = pd.read_csv(input_file)
    most_centuries_player = df.loc[df['Centuries'].idxmax(), ['Player', 'Centuries']]
    print(f" 🏆 Player with most centuries: {most_centuries_player['Player']} ({most_centuries_player['Centuries']} centuries) 🏆")
    
    # Find the player with the highest batting average
    highest_batting_avg_player = df.loc[df['Avg'].idxmax(), ['Player', 'Avg']]
    print(f"🔥 Player with highest batting average: {highest_batting_avg_player['Player']} ({highest_batting_avg_player['Avg']}) 🔥")
    
    most_runs_player = df.loc[df['Runs'].idxmax(), ['Player', 'Runs']]
    print(f"🏏 Player with most Runs: {most_runs_player['Player']} ({most_runs_player['Runs']} runs) 🏏")
    
    highest_sr_player = df.loc[df['SR'].idxmax(), ['Player', 'SR']]
    print(f"🚀 Player with highest Strike Rate: {highest_sr_player['Player']} ({highest_sr_player['SR']}) 🚀")
    
  


    
        
 
    
if __name__ == "__main__":
    # ipl_data = read_ipl_data(PATH)

    data_preprocessing(PATH,CLEAN_PATH)
    print("Data preprocessing completed successfully")
    print("📊 IPL Batter's Summary 📊")
    summarize_date(CLEAN_PATH)

    