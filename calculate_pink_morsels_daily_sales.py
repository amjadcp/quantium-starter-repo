import pandas as pd
import glob
import os

input_path = './data'
output_file = './processed_data/pink_morsels_daily_sales.csv'
all_files = glob.glob(os.path.join(input_path, "*.csv"))
print(f"Found {len(all_files)} files to process.")

totals = {}

for file in all_files:
    # 1. Stream the file in chunks (e.g., 100,000 rows at a time)
    for chunk in pd.read_csv(file, chunksize=100000):
        # 2. Filter for 'pink morsel' immediately to clear memory
        pink_chunk = chunk[chunk['product'] == 'pink morsel'].copy()
        
        if not pink_chunk.empty:
            pink_chunk['price'] = pd.to_numeric(pink_chunk['price'].str.replace('$', '', regex=False), errors='coerce')
            pink_chunk['quantity'] = pd.to_numeric(pink_chunk['quantity'], errors='coerce')
            
            # 3. Calculate sales and group within the chunk
            pink_chunk['sales'] = pink_chunk['price'] * pink_chunk['quantity']
            grouped = pink_chunk.groupby(['region', 'date'])['sales'].sum()
            
            # 4. Update the global accumulator
            for (region, date), sales in grouped.items():
                totals[(region, date)] = totals.get((region, date), 0) + sales

# 5. Convert results to DataFrame and save
if totals:
    final_df = pd.DataFrame([
        {'region': r, 'date': d, 'sales($)': s} 
        for (r, d), s in totals.items()
    ])
    final_df.to_csv(output_file, index=False)
    print(f"Done! Saved to {output_file}")
else:
    print("No 'pink morsel' products found.")
