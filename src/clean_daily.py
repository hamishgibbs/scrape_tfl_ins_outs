import sys
import json 
import pandas as pd

def get_fn_params(fn):
    fn_split = fn.split('/')
    type = fn_split[-3]
    station = fn_split[-1].split('.')[0]
    return {"type": type, "station": station}

def main():

    params = get_fn_params(sys.argv[1])
    
    with open(sys.argv[1]) as f:
        data = json.load(f)
    
    counts = data["results"][0]["result"]["data"]["dsr"]["DS"][0]["PH"][0]["DM0"]

    res = []

    for i, count in enumerate(counts):

        if i:
            prev_count = res[i-1][1]

        if "R" in count["X"][0].keys():
            value = prev_count
        else:
            value = count["X"][0]["M0"]
        
        res.append((count["G0"], value))

    df = pd.DataFrame.from_records(res, columns=["date", "count"])
    df['type'] = params['type']
    df['station'] = params['station']

    df.to_csv(sys.argv[-1], index=False)

if __name__ == "__main__":
    main()

def test_get_fn_params():
    fn = "data/tfl/ins/raw/belsize_park.json"
    res = get_fn_params(fn)
    assert res["type"] == "ins"
    assert res["station"] == "belsize_park"