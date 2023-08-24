import pandas as pd
from flask import Blueprint,request,jsonify
import json

def create_stock_bp():
    bp = Blueprint('stock',__name__)
    
    @bp.route("/stock-info",methods = ['POST'])
    def stock_info():
        stk_code = request.get_json()
        print(stk_code)
        stock_code = stk_code.get('stock_code')
        df = pd.read_csv('all_us_stk_20221216.csv')
        stk_df = df[df.stk_code==stock_code]
        print(stk_df)
        data = stk_df.to_json(orient='records',force_ascii=False)
        return jsonify(json.loads(data))
    
    return bp
        