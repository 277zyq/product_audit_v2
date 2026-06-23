import pandas as pd

def build_risk_summary(file_path,output_path):
    df = pd.read_csv(file_path)
    summary = df.groupby('risk').size().reset_index(name='count')
    summary.to_csv(output_path,index=False)

    return True
