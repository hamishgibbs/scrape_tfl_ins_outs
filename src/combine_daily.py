import sys
import pandas as pd

def main():

    df = pd.concat([pd.read_csv(x) for x in sys.argv[1:-1]])

    df = df.pivot(index=['date', 'station'], columns='type', values='count').reset_index()

    df['date'] = pd.to_datetime(df['date'], unit='ms')

    df.fillna(0, inplace=True)
    
    df.to_csv(sys.argv[-1], index=False)

if __name__ == "__main__":
    main()
