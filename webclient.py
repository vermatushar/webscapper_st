from flask import Flask, request, jsonify, Response
import pandas as pd
from io import StringIO
_data = None
app = Flask(__name__)


@app.route('/receive-json', methods=['POST'])
def receive_json():
    global _data
    data = request.get_json()

    # Process the received JSON data

    # Example: Echo the received JSON data
    print(data)
    str_data = StringIO(data)
    df = pd.read_json(str_data)
    cols = ['Sr.','Stock Name','Symbol','Links','% Chg','Price','Volume','Timestamp']
    df.columns = cols
    print(df)
    return 'Data Rec'


if __name__ == '__main__':
    app.run()
